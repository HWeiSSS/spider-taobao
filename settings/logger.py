import logging.handlers
from settings import functions
from settings.library import *


def log():
    # 创建logger，如果参数为空则返回root logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)  # 设置logger日志等级
    # 这里进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志
    if not logger.handlers:
        # 创建handler
        fh = logging.FileHandler("./logs/{}.log".format(time.strftime("%Y-%m-%d", time.localtime(time.time()))), encoding="utf-8")
        # ch = logging.StreamHandler()
        # 设置输出日志格式
        formatter = logging.Formatter(
            fmt="[%(asctime)s] [%(levelname)s] [%(filename)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
            )
        # 为handler指定输出格式
        fh.setFormatter(formatter)
        # ch.setFormatter(formatter)
        # 为logger添加的日志处理器
        logger.addHandler(fh)
        # logger.addHandler(ch)
    return logger      # 直接返回logger