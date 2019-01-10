import random as rd


# 请求成功
def trueReturn(data):
    return {
        "code": 0,
        "data": data,
        "msg": "请求成功"
    }


# 内部错误
def falseReturn(msg):
    return {
        "code": 1,
        "data": '',
        "msg": msg
    }


# 无权限
def VaildReturn(data):
    return {
        "code": 4,
        "data": data,
        "msg": "无效验证"
    }


# 状态异常
def abnormal_return(msg):
    return {
        "code": 10000,
        "data": "",
        "msg": msg
    }


# 自定义错误码
def error_return(code, data, msg):
    return {
        "code": code,
        "data": data,
        "msg": msg
    }


# 数据库操作错误
def MongoReturn():
    return {
        "code": 2,
        "msg": "数据库操作错误"
    }


# 错误判断
def catch_exception(origin_func):
    def wrapper(self, *args, **kwargs):
        from flask import current_app
        try:
            u = origin_func(self, *args, **kwargs)
            return u
        except Exception as e:
            current_app.logger.error(e)
            result = repr(e)
            return abnormal_return(result)
    return wrapper


def ms(d):
    import time
    # 给定时间元组,转换为秒
    return int(time.mktime(d.timetuple()))


# 生成4位手机验证码
def gen_verify_code(l=4):
    code = ""
    for i in range(l):
        code += str(rd.randint(0, 9))
    return code


def createNonceStr(n):
    # 获取noncestr（随机字符串）
    import random
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    str = ""
    for i in range(0, n):
        s = random.randint(0, len(chars)-1)
        str += chars[s:s+1]
    return str
