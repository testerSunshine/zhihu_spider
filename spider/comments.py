# coding=utf-8
import copy

from config import logger
from config.db_tools import MysqlConn


class ZHComments:
    def __init__(self, token):
        self.conn = MysqlConn()
        self.token = token

    def comments_spider(self):
        """
        评论爬虫
        :return:
        """
        question_list = self.conn.select_for_table("zhihu_question", "question_is_spider=0", "id", "question_id")
        self.get_comments(question_list)

    def get_comments(self, question_list):
        """
        爬取评论
        :return:
        """
        for id, question_id in question_list:
            url = copy.deepcopy(self.token.url)
            while 1:
                comments_result = self.par_url_by_comments(question_id, url)
                logger.log(u"当前评论爬取完毕，正在入库")
                next_url = self.insert_comments(id, comments_result)
                if next_url:
                    url["comments"]["req_url"] = next_url
                else:
                    logger.log(u"当前question 评论已到末尾，正在将其置为已爬取评论")
                    self.conn.update_for_table("zhihu_question", "id={}".format(id),
                                               "question_is_spider=1")  # 更新爬取过的url
                    break

    def par_url_by_comments(self, question_id, url):
        """
        comments 请求方法
        :param question_id: question id
        :param url: url 实例
        :return:
        """
        url["comments"]["req_url"] = url["comments"]["req_url"].format(question_id)
        comments_result = self.token.httpClint.send(url["comments"])
        return comments_result

    def insert_comments(self, id, comments_result):
        """
        评论入库
        :param question_id: 问题id
        :param comment_result: 评论结果
        :return:
        """
        if comments_result and "data" in comments_result and comments_result["data"]:
            for data in comments_result["data"]:
                comments_url = data.get("url", "")
                comments_content = data.get("content", "")
                comments_time = data.get("created_time", "")
                comments_author_avatar = data.get("vote_count", "")
                if "author" in data and data["author"]:
                    author = data["author"]["member"]
                    comments_author_name = author.get("name", "")
                    comments_author_describe = author.get("headline", "")
                    self.insert_user(author)  # 用户信息入库
                else:
                    comments_author_name = ""
                    comments_author_describe = ""
                self.conn.insert_for_comments(question_id=id,
                                              comments_url=comments_url,
                                              comments_content=comments_content,
                                              comments_time=comments_time,
                                              comments_author_avatar=comments_author_avatar,
                                              comments_author_name=comments_author_name,
                                              comments_author_describe=comments_author_describe)
            next_url = comments_result["paging"]["next"] if comments_result["paging"]["is_end"] else False
            return next_url

    def insert_user(self, author):
        """
        爬取用户信息
        :param author: 用户信息
        :return:
        """
        user_name = author.get("name", "")
        user_gender = author.get("gender", 3)
        user_token = author.get("url_token", "")
        user_avatar = author.get("avatar_url", "")
        user_id = author.get("id", "")
        user_type = author.get("type", "")
        self.conn.insert_for_user(user_name=user_name,
                                  user_gender=user_gender,
                                  user_token=user_token,
                                  user_avatar=user_avatar,
                                  user_id=user_id,
                                  user_type=user_type)