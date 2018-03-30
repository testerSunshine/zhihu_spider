# -*- coding: utf8 -*-
import time

from config import urlConf, logger, signature
from myUrllib import httpUtils


class zhlg(object):
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.signature = signature.get_signature()
        self.url = urlConf.urls
        self.httpClint = httpUtils.HTTPClient()

    def signup(self):
        urls = self.url["signup"]
        self.httpClint.send(urls=urls)

    def captcha(self):
        urls = self.url["captcha"]
        captcha_data = self.httpClint.send(urls)
        if captcha_data and "show_captcha" in captcha_data and captcha_data["show_captcha"]:
            logger.log(u"需要验证码")
            return False
        else:
            logger.log(u"不需要验证码")
            return True

    def get_token(self):
        return self

    def login(self):
        timestamp = int(round(time.time() * 1000))
        urls = self.url["auth"]
        data = {
            "client_id": "c3cef7c66a1843f8b3a9e6a1e3160e20",
            "grant_type": "password",
            "timestamp": str(timestamp),
            "source": "com.zhihu.web",
            "signature": signature.get_signature(timestamp),
            "username":	"+86{}".format(self.user),
            "password":	self.password,
            "captcha": "",
            "lang":	"cn",
            "ref_source": "homepage",
            "utm_source": "",
        }
        while 1:
            if self.captcha():
                rep = self.httpClint.send(urls=urls, data=data)
                if "user_id" in rep and rep["user_id"]:
                    # self.httpClint.setHeaders({"content-type": "application/x-www-form-urlencoded; charset=UTF-8"})
                    # self.httpClint.del_cookies_by_key("authorization")
                    self.httpClint.resetHeaders()
                    self.httpClint.del_cookies()
                    logger.log(msg=rep)
                    return self
                if "message" in rep and rep["message"]:
                    if rep["message"].find("密码错误") != -1:
                        logger.log(u"当前登录账号密码设置错误， {0}".format(rep["message"]))
                        break
                    else:
                        logger.log(u"当前登录账号异常，{0}".format(rep["message"]))
                        break
                else:
                    self.httpClint.del_cookies()
                    time.sleep(60)
                    logger.log(rep, func="error")
            else:
                self.httpClint.del_cookies()
                logger.log(u"检测登录需要验证码，停止一分钟", func="info")
                time.sleep(60)


if __name__ == "__main__":
    lg = zhlg("", "")
    lg.signup()
    lg.login()
