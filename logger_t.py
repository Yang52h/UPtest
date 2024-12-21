# 绝对路径导入
import sys
sys.path.append('../BASE_py/')
from Logger import logger

# 2024年12月18日22:52:18
'''搜了半天   目前的结论是 还是放在一起比较好'''

if __name__ == '__main__':
    logger.debug("这是一个调试信息。")
    logger.info("这是一个信息消息。")
    logger.warning("这是一个警告消息。")
    logger.error("这是一个错误消息。")
    logger.critical("这是一个严重错误消息。")

    print("start")
