from sys import exit as sys_exit
from sys import argv as sys_argv

def get_account():
    """
    获取账号信息
    """
    uid, psw = sys_argv[1].strip().split(' ')
    return uid, psw

gl_info = "快去手动填写！"
if __name__ == '__main__':
    uid, psw = get_account()

    print(uid)
    print(psw)
