from flask import Blueprint
bp = Blueprint('chat',__name__,url_prefix='/chat')

@bp.route('/chatgpt')
def chat_chatgpt():
    return 'GPT입니다!'

@bp.route('/lama2')
def chat_lama2():
    return 'lama2 입니다!'

# @bp.route('/manwoman')
# def manwoman():
#     return '여성입니다!'