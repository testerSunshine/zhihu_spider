# -*- coding: utf8 -*-
import hashlib
import hmac
import time


def get_signature(timestamp=None):
    """
    获取signature加密字符串
    :return:
    """
    h = hmac.new(key="d1b964811afb40118a12068ff74a12f4", digestmod=hashlib.sha1)
    h.update("password")
    h.update("c3cef7c66a1843f8b3a9e6a1e3160e20")
    h.update("com.zhihu.web")
    h.update(str(timestamp if timestamp else round(time.time() * 1000)))
    _signature = h.hexdigest()
    return _signature


if __name__ == "__main__":
    print get_signature(1520241638962)

