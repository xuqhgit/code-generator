

from web import app
from flask import render_template, request

from web.util import template_util


@app.errorhandler(403)
def internal_error(error):
    return render_template('html/403.html'), 403


@app.errorhandler(404)
def internal_error(error):
    return render_template('html/404.html'), 404


@app.errorhandler(405)
def internal_error(error):
    return render_template('html/405.html'), 405


@app.errorhandler(500)
def internal_error(error):
    return render_template('html/500.html'), 500



@app.route('/')
@app.route('/index', methods=['get','post'])
def index():
    return render_template('html/index.html', ctx={"menu":template_util.read_module()})

