from flask import *
from markdown import Markdown

import re

app = Flask(__name__)
md = Markdown(extensions=['markdown.extensions.extra', 'markdown.extensions.toc', 'markdown.extensions.codehilite'])


@app.route('/', defaults={'path': 'README.md'})
@app.route('/<path:path>')
def root(path):
    if re.match('.+\.md$', path, re.IGNORECASE):
        return render_template('index.html', body=md2html(path), title=path)
    elif app.debug:
        return send_from_directory('src', path)
    else:
        abort(403)


def md2html(path):
    with open('src/' + path, encoding='UTF-8') as markdwon:
        return md.convert('[TOC]\n' + markdwon.read())


if __name__ == '__main__':
    app.run(debug=True)
