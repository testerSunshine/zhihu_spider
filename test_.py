# coding=utf-8
# def reverse(x):
#     s = cmp(x, 0)
#     r = int(`s*x`[::-1])
#     return s*r if (r < 2**31) else 0
import json
import re

# def maopao(_list):
#     for i in range(1, 10):
#         r_list = []
#         for j in range(1, i+1):
#             r_list.append("{0}*{1}={2}".format(i, j, i*j))
#         print r_list
#
# maopao([4,5,3,5,6,9,8])

# def f(func):
#     def waper(*args, **kwargs):
#         print "aaa"
#         print "*args is {}".format(args)
#         print func(*args, **kwargs)
#
#     return waper
#
#
# @f
# def a(c, d):
#     return c+d
#
#
# a(1, 2)
#
# def fab(max):
#     n, a, b = 0, 0, 1,
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n += 1
#
# for f in fab(5):
#     print f

# def print_file_path(r_path):
#     import os
#     for this_path in os.listdir(r_path):
#         child_path = os.path.join(r_path, this_path)
#         if os.path.isdir(child_path):
#             print "this file is dir {0}".format(child_path)
#             print_file_path(child_path)
#         else:
#             print this_path
#
# print_file_path("/usr/local")

# def strStr(haystack, needle):
#     """
#     :type haystack: str
#     :type needle: str
#     :rtype: int
#     """
#     l_haystack = list(haystack)
#     l_needle = list(needle)
#     for i in range(len(l_haystack)):
#         if "".join(l_haystack[i:i + len(l_needle)]) == needle:
#             return i
#     return -1
#
#
# from bs4 import BeautifulSoup
#
# a = '<div class="item"><div class="blk">\n<a target="_blank" href="\\/topic\\/19587670">\n<img src="https:\\/\\/pic4.zhimg.com\\/289534a20_xs.jpg" alt="\xe7\x9b\x9b\xe5\xa4\xa7\xe6\x8e\xa8\xe4\xbb\x96">\n<strong>\xe7\x9b\x9b\xe5\xa4\xa7\xe6\x8e\xa8\xe4\xbb\x96<\\/strong>\n<\\/a>\n<p><\\/p>\n\n<a id="t::-12466" href="javascript:;" class="follow meta-item zg-follow"><i class="z-icon-follow"><\\/i>\xe5\x85\xb3\xe6\xb3\xa8<\\/a>\n\n<\\/div><\\/div>'
#
#
#
#
#
# soup = BeautifulSoup(a, "html.parser")
# print soup.find("a")["href"].replace("\\", "")
# print soup.find("img")["src"].replace("\\", "")
# print soup.find("img")["alt"].replace("\\", "")
# print soup.find("p").text.split("\n")[0]

# def istestFnally():
#     try:
#         return 1
#     except Exception as e:
#         return 2
#     finally:
#         print 3
#
# def a(*args):
#     print ",".join(args)
#
# a("1", "2", "3", "4)
# a = "{} hahah"
# print a.format("me is")
# print a.format("me1 is")
#
# a = json.loads()
# for i in a["data"]:
#     print i

# import unittest
#
#
# class TestAlwaysTrue(unittest.TestCase):
#     def test_assertTrue(self):
#         """
#         always_true returns a truthy value
#         """
#         print "testSart..."
#         self.assertTrue(1 == 2, msg="not == !")
#
#
# if __name__=='__main__':
#     unittest.main()

#
# import redis
#
# r = redis.Redis(host='localhost', port=6379, db=0)
# # r.set('guo', 'shuai')
# # r.set('guo', 'shuai1')
# r.lpush("guo1", 1)
# # r.lpush("guo2", 1, 2, 3, 4, 5,6)
# print r.get('guo')
# print r.lpop("guo2")
# from selenium.webdriver.common import by
# from selenium.webdriver.common.by import By
#
#
# def call_def(element):
#     num = 0
#     try:
#         webdr
#         print ("这里正常的功能")
#     except Exception as e:
#         print ("这里点击那个状态框")
#         num += 1
#         if num > 10:
#             raise (Exception, "没有找到功能")
#         call_def()
#
#
# call_def(element=By.ID("xxxxxx"))
class test___:
    def recall(self, b):
        print(b)
        self.recall(b)
t = test___()
t.recall(1)