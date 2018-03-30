# -*- coding: utf8 -*-
from config import topic_conf, logger
from config.db_tools import MysqlConn
from config.soupTool import soup_tool


class ZHTopic:
    def __init__(self, token):
        self.conn = MysqlConn()
        self.token = token
        self.topic_list = topic_conf.topic_list

    def get_topic_all(self):
        """
        获取所有话题
        :return:
        """
        try:
            for i in xrange(len(self.topic_list)):
                offset = 0
                key = self.topic_list[i].keys()[0]
                while 1:
                    data = {
                        "method": "next",
                        "params": '{"topic_id":%d,"offset":%d,"hash_id":"cb253ec81f2947593a1e9c8426177bbe"}' %
                                  (self.topic_list[i][key], offset),
                    }
                    offset += 20
                    topic_data = self.token.httpClint.send(self.token.url["TopicsPlazzaListV2"], data)
                    if topic_data and "msg" in topic_data and topic_data["msg"]:
                        msg = topic_data["msg"]
                        for j in range(len(msg)):
                            soup = soup_tool(msg[j])
                            url = soup.find("a")["href"].replace("\\", "")
                            img_url = soup.find("img")["src"].replace("\\", "")
                            name = soup.find("img")["alt"].replace("\\", "")
                            describe = soup.find("p").text.split("\n")[0]
                            logger.log("获得topic信息：url is {0}, img_url is {1}, name is {2}, describe is {3}".format(url, img_url, name, describe))
                            self.conn.insert_for_topic(topic_name=key,
                                                       topic_little_name=name,
                                                       topic_little_describe=describe,
                                                       topic_little_url=url,
                                                       topic_little_img_url=img_url
                                                       )
                    else:
                        logger.log("当前topic url 爬取完毕")
                        break
        except Exception as e:
            logger.log(msg=e, func="error")
        finally:
            self.conn.close_session()


