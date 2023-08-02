from flask import Blueprint
bp = Blueprint('classification',__name__,url_prefix='/classification')

@bp.route('/catdog')
def catdog():
    return '고양이 입니다!'

@bp.route('/birdflower')
def birdflower():
    return '비둘기 입니다!'

@bp.route('/manwoman')
def manwoman():
    return '여성입니다!'