import logging
import colorlog

'''------------配置开始------------'''
'''带颜色log日志配置'''
# 创建一个日志记录器
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# 创建一个控制台处理器
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
# 使用 colorlog 的 ColoredFormatter

# '%(asctime)s - %(filename)s - %(funcName)s - %(lineno)s %(levelname)s : %(message)s'
# [日志时间] - [文件名] - [函数名] - [行号] [日志级别] : [日志消息]
formatter = colorlog.ColoredFormatter(
    "%(log_color)s%(asctime)s - %(levelname)s - %(message)s",
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    },
    datefmt='%Y-%m-%d %H:%M:%S'  # 添加日期格式
)
# 设置处理器的格式
console_handler.setFormatter(formatter)
# 将处理器添加到记录器
logger.addHandler(console_handler)
'''------------配置结束------------'''

'''测试用例
# 测试日志记录
    logger.debug("这是一个调试信息。")
    logger.info("这是一个信息消息。")
    logger.warning("这是一个警告消息。")
    logger.error("这是一个错误消息。")
    logger.critical("这是一个严重错误消息。")
'''


