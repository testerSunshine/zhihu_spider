# coding=utf-8
from bs4 import BeautifulSoup


def soup_tool(htmls):
    """
    解析成soup对象
    :param html: 返回的网页字符串
    :return: soup对象
    """
    return BeautifulSoup(htmls, 'html.parser')
