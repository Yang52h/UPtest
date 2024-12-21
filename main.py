from myLogger import logger
from Config import read_config

if __name__ == '__main__':
    logger.debug("这是一个调试信息。")
    logger.info("这是一个信息消息。")
    logger.warning("这是一个警告消息。")
    logger.error("这是一个错误消息。")
    logger.critical("这是一个严重错误消息。")


    config_ini = read_config('config.ini')

    ip = config_ini.get('target_ip', 'IP')
    print(f'IP: {ip}')

    print("start")
