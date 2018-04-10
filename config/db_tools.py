# -*- coding: utf8 -*-
import pymysql
import sys
from pymysql import DataError, InternalError

from config import logger
from config.now_time import get_now_time
from config.yaml_info import _get_yaml_local

reload(sys)
sys.setdefaultencoding("utf-8")


class MysqlConn:
    pymysql.install_as_MySQLdb()

    def __init__(self):
        self.conn = self.mysql_conn()
        self.cur = self.conn.cursor()

    def mysql_conn(self):
        y = _get_yaml_local("config_zhihu_remote.yaml")
        conn = pymysql.connect(
                host=y["db"]["ip"],
                port=y["db"]["port"],
                user=y["db"]["uname"],
                passwd=y["db"]["passwd"],
                db=y["db"]["table"],
                charset="utf8mb4"
                )
        conn.autocommit(1)
        return conn

    def execute_m(self, sql):
        if sql is None:  # sql not None!
            return "please input sql"
        else:
            try:
                self.cur.execute(sql)
                logger.log(u"数据执行完毕..")
                return self.cur.fetchall()
            except DataError as e:
                logger.log(e)
            except InternalError as e:
                logger.log(e)
            except pymysql.err.Error as e:
                logger.log(e)
                self.conn = self.mysql_conn()  # mysql 断开连接重连
                self.execute_m(sql)

    def close_session(self):
        self.cur.close()
        self.conn.close()

    def l_time(self):
        return self.conn.escape(get_now_time("%Y-%m-%d %H:%M:%S"))

    def insert_for_topic(self, topic_name, topic_little_name, topic_little_describe, topic_little_url, topic_little_img_url):
        """
        话题库
        :param topic_name: 主话题名称
        :param topic_little_name: 小话题名称
        :param topic_little_describe: 小话题描述
        :param topic_little_url: 小话题url
        :return:
        """
        topic_name = self.conn.escape(topic_name)
        topic_little_name = self.conn.escape(topic_little_name)
        topic_little_describe = self.conn.escape(topic_little_describe)
        topic_little_url = self.conn.escape(topic_little_url)
        topic_little_img_url = self.conn.escape(topic_little_img_url)
        sql = """INSERT INTO zhihu_topicinfo (topic_name, topic_little_name, topic_little_describe, topic_little_url, topic_little_img_url, topic_create_time, topic_update_time, topic_is_spider)
                 VALUES ( %s, %s, %s, %s, %s, %s, %s, 0)""" % (topic_name, topic_little_name, topic_little_describe, topic_little_url, topic_little_img_url, self.l_time(), self.l_time())
        logger.log("即将插入sql: {}".format(sql))
        self.execute_m(sql=sql)

    def select_for_table(self, table=None, where=None, *args):
        """
        查询topic url
        * 代表所有
        "line1", "line2", "line3" 代表查询次三列的信息，依次类推
        :return: 查询的元祖信息列表
        """
        sql = """SELECT {0} FROM {1} {2}""".format(",".join(args),
                                                    table if table else "",
                                                    "WHERE "+where if where else "")
        table_info = self.execute_m(sql=sql)
        return table_info

    def update_for_table(self, table, where, line):
        """
        更新表字典
        :param table:
        :param where:
        :param args:
        :return:
        """
        sql = """UPDATE {0} SET {1} WHERE {2}""".format(table,
                                                       line,
                                                       where)
        table_info = self.execute_m(sql=sql)
        return table_info

    def insert_for_question(self, topic_info_id, question_name, question_content, question_author_name, question_author_describe, question_vote, question_comments, question_url, question_updated_time, question_created_time, question_id):
        """
        提问库
        :param question_created: 提问创建时间
        :param question_updated_time: 提问最后更新时间
        :param question_url: 提问连接
        :param topic_info: topic 外键关联
        :param question_name: 提问名称
        :param question_content: 提问内容缩略
        :param question_author_name: 提问作者
        :param question_author_describe: 提问作者描述
        :param question_vote: 提问投票数
        :param question_comments: 提问评论数
        :return:
        """
        question_name = self.conn.escape(question_name)
        question_content = self.conn.escape(question_content)
        question_author_name = self.conn.escape(question_author_name)
        question_author_describe = self.conn.escape(question_author_describe)
        question_vote = self.conn.escape(question_vote)
        question_comments = self.conn.escape(question_comments)
        question_url = self.conn.escape(question_url)
        question_updated_time = self.conn.escape(question_updated_time)
        question_created_time = self.conn.escape(question_created_time)
        question_id = self.conn.escape(question_id)
        sql = """INSERT INTO zhihu_question (topic_info_id, question_name, question_content, question_author_name, 
                 question_author_describe, question_vote, question_comments, question_url, question_updated_time,
                 question_created_time, question_id, question_create_time, question_update_time, question_is_spider)
                 VALUES ( {0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10},{11},{12}, 0)""".\
            format(topic_info_id,
                   question_name,
                   question_content,
                   question_author_name,
                   question_author_describe,
                   question_vote,
                   question_comments,
                   question_url,
                   question_updated_time,
                   question_created_time,
                   question_id,
                   self.l_time(),
                   self.l_time())
        logger.log("即将插入sql: {}".format(sql))
        self.execute_m(sql=sql)

    def insert_for_comments(self, question_id, comments_url, comments_content, comments_time, comments_author_name, comments_author_describe, comments_author_avatar):
        """
        评论库
        :param question: question外键关联
        :param comments_url: 评论连接
        :param comments_content: 评论内容
        :param comments_time: 评论时间
        :param comments_author_name: 评论作者名字
        :param comments_author_describe: 评论作者描述
        :param comments_author_avatar: 评论作者头像
        :return:
        """
        comments_url = self.conn.escape(comments_url)
        comments_content = self.conn.escape(comments_content)
        comments_time = self.conn.escape(comments_time)
        comments_author_name = self.conn.escape(comments_author_name)
        comments_author_describe = self.conn.escape(comments_author_describe)
        comments_author_avatar = self.conn.escape(comments_author_avatar)
        sql = """INSERT INTO zhihu_commentsinfo (question_id, comments_url, comments_content, comments_time, comments_author_name, comments_author_describe, comments_author_avatar, comments_create_time, comments_update_time)
              VALUES ( {0}, {1}, {2}, {3}, {4}, {5}, {6},{7},{8})""" \
            .format(question_id,
                    comments_url,
                    comments_content,
                    comments_time,
                    comments_author_name,
                    comments_author_describe,
                    comments_author_avatar,
                    self.l_time(),
                    self.l_time())
        logger.log("即将插入sql: {}".format(sql))
        self.execute_m(sql=sql)

    def insert_for_user(self, user_name, user_gender, user_token, user_avatar, user_id, user_type):
        """
        用户库
        :param user_name: 用户
        :param user_gender: 性别
        :param user_token: token
        :param user_avatar: 用户头衔url
        :param user_id: 用户id
        :return:
        """
        user_name = self.conn.escape(user_name)
        user_gender = self.conn.escape(user_gender)
        user_token = self.conn.escape(user_token)
        user_avatar = self.conn.escape(user_avatar)
        user_id = self.conn.escape(user_id)
        user_type = self.conn.escape(user_type)
        sql = """INSERT INTO zhihu_user (user_name, user_gender, user_token, user_avatar, user_id, user_type, user_create_time, user_update_time)
              VALUES ({0}, {1}, {2}, {3}, {4},{5}, {6}, {7})""" \
            .format(user_name,
                    user_gender,
                    user_token,
                    user_avatar,
                    user_id,
                    user_type,
                    self.l_time(),
                    self.l_time())
        logger.log("即将插入sql: {}".format(sql))
        self.execute_m(sql=sql)


if __name__ == "__main__":
    conn = MysqlConn()
    # for id, url in conn.select_for_table("zhihu_topicinfo", "topic_is_spider=0", "id", "topic_little_url"):
    #     print id, url
    print conn.select_for_table("zhihu_question", "question_is_spider=0", "id", "question_id")
