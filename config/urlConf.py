# -*- coding: utf8 -*-

urls = {
    "signup": {  # 登录网页
        "req_url": "/signup?next=%2F",
        "req_type": "get",
        "Referer": "https://www.zhihu.com/",
        "Host": "www.zhihu.com",
        "re_try": 1,
        "re_time": 0.1,
        "s_time": 0.1,
        "is_logger": False,
        "is_json": False,
        "is_multipart_data": False,
        "headers": {
        }
    },
    "captcha": {  # 判断是否需要验证码
        "req_url": "/api/v3/oauth/captcha?lang=cn",
        "req_type": "get",
        "Referer": "https://www.zhihu.com/",
        "Host": "www.zhihu.com",
        "re_try": 1,
        "re_time": 0.1,
        "s_time": 0.1,
        "is_logger": True,
        "is_json": True,
        "is_multipart_data": False,
        "headers": {
            "authorization": "oauth c3cef7c66a1843f8b3a9e6a1e3160e20",
        }
    },
    "auth": {   # 登录
        "req_url": "/api/v3/oauth/sign_in",
        "req_type": "post",
        "Referer": "https://www.zhihu.com/signup?next=%2F",
        "Host": "www.zhihu.com",
        "re_try": 1,
        "re_time": 0.1,
        "s_time": 0.1,
        "is_logger": True,
        "is_json": True,
        "is_multipart_data": True,
        "headers": {
            "X-UDID": "AADs651LPQ2PTvmuuEJieNomsFdKFy7Loz8=",
            "X-Xsrftoken": "e4e00d03-ee84-4f74-aba0-a94c3702d84c",
        }
    },
    "TopicsPlazzaListV2": {   # 获取所有小话题
        "req_url": "/node/TopicsPlazzaListV2",
        "req_type": "post",
        "Referer": "https://www.zhihu.com/topics",
        "Host": "www.zhihu.com",
        "re_try": 1,
        "re_time": 0.1,
        "s_time": 0.4,
        "is_logger": True,
        "is_json": True,
        "is_multipart_data": True,
    },
    "topic": {   # 话题广场
        "req_url": "/topics#{}",
        "req_type": "get",
        "Referer": "https://www.zhihu.com/signup?next=%2F",
        "Host": "www.zhihu.com",
        "re_try": 1,
        "re_time": 0.1,
        "s_time": 0.1,
        "is_logger": True,
        "is_json": False,
        "is_multipart_data": True,
        "headers": {
            "X-UDID": "AADs651LPQ2PTvmuuEJieNomsFdKFy7Loz8=",
            "X-Xsrftoken": "e4e00d03-ee84-4f74-aba0-a94c3702d84c",
        }
    },
    "top-activity": {   # 全部话题
        "req_url": "/api/v4/{0}/feeds/top_activity?include=data[?(target.type=topic_sticky_module)].target.data[?(target.type=answer)].target.content,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;data[?(target.type=topic_sticky_module)].target.data[?(target.type=answer)].target.is_normal,comment_count,voteup_count,content,relevant_info,excerpt.author.badge[?(type=best_answerer)].topics;data[?(target.type=topic_sticky_module)].target.data[?(target.type=article)].target.content,voteup_count,comment_count,voting,author.badge[?(type=best_answerer)].topics;data[?(target.type=topic_sticky_module)].target.data[?(target.type=people)].target.answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics;data[?(target.type=answer)].target.content,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;data[?(target.type=answer)].target.author.badge[?(type=best_answerer)].topics;data[?(target.type=article)].target.content,author.badge[?(type=best_answerer)].topics;data[?(target.type=question)].target.comment_count&limit=5&after_id={1}",
        "req_type": "get",
        "Referer": "https://www.zhihu.com/topic/19552192/hot",
        "Host": "www.zhihu.com",
        "re_try": 3,
        "re_time": 0.5,
        "s_time": 0.5,
        "is_logger": True,
        "is_json": True,
        "is_multipart_data": False,
        "headers": {
            "X-UDID": "AADs651LPQ2PTvmuuEJieNomsFdKFy7Loz8=",
            "authorization": "oauth c3cef7c66a1843f8b3a9e6a1e3160e20",
        }
    },
    "top-answers": {   # 精华话题
        "req_url": "{}/top-answers",
        "req_type": "post",
        "Referer": "https://www.zhihu.com/signup?next=%2F",
        "Host": "www.zhihu.com",
        "re_try": 1,
        "re_time": 0.1,
        "s_time": 0.1,
        "is_logger": True,
        "is_json": True,
        "is_multipart_data": True,
        "headers": {
            "X-UDID": "AADs651LPQ2PTvmuuEJieNomsFdKFy7Loz8=",
            "X-Xsrftoken": "e4e00d03-ee84-4f74-aba0-a94c3702d84c",
        }
    },
    "hot": {   # 讨论话题
        "req_url": "{}/hot",
        "req_type": "post",
        "Referer": "https://www.zhihu.com/signup?next=%2F",
        "Host": "www.zhihu.com",
        "re_try": 1,
        "re_time": 0.1,
        "s_time": 0.5,
        "is_logger": False,
        "is_json": False,
        "is_multipart_data": False,
        "headers": {
            "X-UDID": "AADs651LPQ2PTvmuuEJieNomsFdKFy7Loz8=",
            "X-Xsrftoken": "e4e00d03-ee84-4f74-aba0-a94c3702d84c",
        }
    },
    "unanswered": {   # 等待回答
        "req_url": "{}/unanswered",
        "req_type": "post",
        "Referer": "https://www.zhihu.com/signup?next=%2F",
        "Host": "www.zhihu.com",
        "re_try": 1,
        "re_time": 0.1,
        "s_time": 0.1,
        "is_logger": True,
        "is_json": False,
        "is_multipart_data": False,
        "headers": {
            "X-UDID": "AADs651LPQ2PTvmuuEJieNomsFdKFy7Loz8=",
            "X-Xsrftoken": "e4e00d03-ee84-4f74-aba0-a94c3702d84c",
        }
    },
    "comments": {   # 等待回答，参数化问题id和页数，is_end为True表示评论已刷完
        "req_url": "/api/v4/answers/{0}/comments?include=data[*].author,collapsed,reply_to_author,disliked,content,voting,vote_count,is_parent_author,is_author&order=normal&limit=20&offset=0&status=open",
        "req_type": "get",
        "Referer": "https://www.zhihu.com/topic/19550994/hot",
        "Host": "www.zhihu.com",
        "re_try": 3,
        "re_time": 0.5,
        "s_time": 0.3,
        "is_logger": True,
        "is_json": True,
        "is_multipart_data": False,
        "headers": {
            "authorization": "oauth c3cef7c66a1843f8b3a9e6a1e3160e20",
        }
    },

}