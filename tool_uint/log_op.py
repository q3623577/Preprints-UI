import logging
import os
import time

root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_path = os.path.join(root_path, 'logs')


class Logger:

    def __init__(self):
        """

        """
        # 设置日志的目录位置和生成的日志文件名称格式
        self.logname = os.path.join(log_path, '{}.logs'.format(time.strftime("%Y%m%d-%H%M")))

        # 定义日志容器
        self.logger = logging.getLogger("logs")

        # 设置日志级别
        self.logger.setLevel(logging.DEBUG)

        # 创建日志输入格式
        self.formater = logging.Formatter("[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s")

        # 创建文件日志处理器
        self.file_handler = logging.FileHandler(self.logname, mode='a', encoding='utf-8')

        # 创建控制台日志处理器
        self.console_handler = logging.StreamHandler()

        # 设置日志处理器的日志输出格式
        self.file_handler.setFormatter(self.formater)
        self.console_handler.setFormatter(self.formater)

        # 将处理器添加到日志收集器中
        self.logger.addHandler(self.file_handler)
        self.logger.addHandler(self.console_handler)


logger = Logger().logger

if __name__ == '__main__':
    logger.debug(f"{os.getpid()} is")
