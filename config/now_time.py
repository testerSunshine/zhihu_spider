# coding=utf-8
import datetime


def get_now_time(time_type):
    """
    获取当前时间
    :param time_type: 传入当前时间格式戳， str类型
    :return:
    """
    if isinstance(time_type, str):
        return datetime.datetime.now().strftime(time_type)
    else:
        return "输入格式有误，需传入类似%Y-%m-%d %H:%M:%S类型"


if __name__ == "__main__":
    print type(get_now_time("%Y-%m-%d %H:%M:%S"))