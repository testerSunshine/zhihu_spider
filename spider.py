# coding=utf-8
from config.yaml_info import _get_yaml_local
from proxy.proxy_tools import proxy
from spider.comments import ZHComments
from spider.login import zhlg
from spider.question import ZHQuestion
from spider.topic import ZHTopic


def getlogin():
    """
    知乎登陆
    :return: zhlg 对象
    """
    login_info = _get_yaml_local("zhihu_login.yaml")
    lg = zhlg(user=login_info["name"][0], password=login_info["passwd"][0])
    # lg.signup()
    # return lg.login()
    return lg.get_token()


def startSpider():
    """
    爬去页面标签
    :return:
    """
    token = getlogin()
    topic = ZHTopic(token)
    topic.get_topic_all()


def startQuestion():
    """
    爬去话题
    :return:
    """
    token = getlogin()
    question = ZHQuestion(token)
    question.topic_spider()


def startComments():
    """
    爬取评论
    :return:
    """
    token = getlogin()
    comments = ZHComments(token)
    comments.comments_spider()


if __name__ == "__main__":
    # startSpider()
    startQuestion()
    # startComments()