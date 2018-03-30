# coding=utf-8
import copy
import re
import threading

from config import logger
from config.db_tools import MysqlConn


class ZHQuestion:
    def __init__(self, token):

        self.token = token

    def get_conn(self):
        return MysqlConn()

    def topic_spider(self):
        """
        获取所有question spider
        :return: url list
        """
        conn = self.get_conn()
        url_list = conn.select_for_table("zhihu_topicinfo", "topic_is_spider=0", "id", "topic_little_url")
        conn.close_session()
        size = len(url_list)/2 + 1
        split_url_list = [url_list[i: i+size] for i in range(0, len(url_list), size)]
        threadList = []
        for _url_list in split_url_list:
            conn = self.get_conn()
            t = threading.Thread(target=self.get_question, args=(_url_list, conn,))
            t.setDaemon(True)
            threadList.append(t)
        for t in threadList:
            t.start()
        for t in threadList:
            t.join()
        # self.conn.close_session()

    def get_question(self, url_list, conn):
        """
        爬去提问
        :return:
        """
        for topic_id, topic_url in url_list:
            url = copy.deepcopy(self.token.url)
            hot_result = self.par_url_by_top(topic_url, url)
            if hot_result:
                try:
                    _topic_url, _range_number = self.topic_re(hot_result)
                    if _topic_url and _range_number:
                        url["top-activity"]["req_url"] = url["top-activity"]["req_url"].format(_topic_url, _range_number)
                        while 1:
                            question_result = self.token.httpClint.send(url["top-activity"])
                            logger.log(u"{} 已爬取完毕, 正在入库".format(topic_id))
                            next_url = self.insert_question(topic_id, question_result, conn)
                            if next_url:
                                url["top-activity"]["req_url"] = next_url
                            else:
                                logger.log(u"{} 已爬取已达末尾，设置topic为已爬去状态".format(topic_id))
                                conn.update_for_table("zhihu_topicinfo", "id={}".format(topic_id), "topic_is_spider=1")  # 更新爬取过的url
                                break
                except TypeError as e:
                    logger.log(e)
                except KeyError as e:
                    logger.log(e)
                # except Exception as e:
                #     logger.log(e)
            else:
                logger.log(hot_result)
        conn.close_session()

    def insert_question(self, topic_info_id, question_result, conn):
        """
        提问入库
        type: article 代表文章，里面没有带question字典
              answer 里面带question字典,
              normal 代表正常，里面没有author字典
        :return:
        """
        if question_result and "data" in question_result and question_result["data"]:
            for target in question_result["data"]:
                question_name = target["target"]["question"]["title"] if target["target"]["type"] == "answer" else target["target"]["title"]
                question_content = target["target"]["excerpt"] if "excerpt" in target["target"] else ""
                question_author_name = target["target"]["author"]["name"] if target["target"]["type"] != "normal" else ""
                question_author_describe = target["target"]["author"]["headline"] if target["target"]["type"] != "normal" else ""
                question_vote = target["target"]["voteup_count"]
                question_comments = target["target"]["comment_count"]
                question_url = target["target"]["question"]["url"] if target["target"]["type"] == "answer" else target["target"]["url"]
                question_created_time = target["target"]["created_time"] if target["target"]["type"] == "answer" else ""
                question_updated_time = target["target"]["updated_time"] if target["target"]["type"] == "answer" else ""
                question_id = target["target"]["id"]
                conn.insert_for_question(topic_info_id=topic_info_id,   # 提问入库
                                              question_name=question_name,
                                              question_content=question_content,
                                              question_author_name=question_author_name,
                                              question_author_describe=question_author_describe,
                                              question_vote=question_vote,
                                              question_comments=question_comments,
                                              question_url=question_url,
                                              question_created_time=question_created_time,
                                              question_updated_time=question_updated_time,
                                              question_id=question_id)
                if "author" in target and target["author"]:
                    self.insert_user(target["author"], conn)
            next_url = question_result["paging"]["next"].replace("http://www.zhihu.com", "") if not question_result["paging"]["is_end"] else False  # 如果is_end为True 代表到了最后一行
            return next_url

    def insert_user(self, author, conn):
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
        conn.insert_for_user(user_name=user_name,
                              user_gender=user_gender,
                              user_token=user_token,
                              user_avatar=user_avatar,
                              user_id=user_id,
                              user_type=user_type)

    def topic_re(self, topic_html):
        """
        topic 需要正则提取的参数
        :return:
        """
        topic_re_url = re.compile(r"http://www.zhihu.com/api/v4/(\S+)/feeds/top_activity?")
        range_re_number = re.compile(r"after_id=(\S+)&quot;}}")
        _topic_url = re.search(topic_re_url, topic_html).group(1)  # 读取话题列表url
        _range_number = re.search(range_re_number, topic_html).group(1)  # 第一次话题的随机数
        return _topic_url, _range_number

    def par_url_by_top(self, topic_url, url):
        """
        top 请求方法
        :param url:
        :param topic_url:
        :return:
        """
        url["hot"]["req_url"] = url["hot"]["req_url"].format(topic_url)
        hot_result = self.token.httpClint.send(url["hot"])
        return hot_result

