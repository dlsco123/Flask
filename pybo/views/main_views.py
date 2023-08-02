from flask import Blueprint
bp = Blueprint('main',__name__,url_prefix='/')

@bp.route('/')
def hello_pybo():
    return 'Hello Pybo!'


@bp.route('/ai')
def main_ai():
    return 'ai'