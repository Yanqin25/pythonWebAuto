import logging
import os
import datetime


class UserLog():
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.fileStream = logging.FileHandler(self.__get_log_name())
        self.__init_logger_handle()

    def __get_log_name(self):
        log_path = os.path.join(os.path.dirname(
            os.path.abspath(__file__)), "logs")
        log_file = datetime.datetime.now().strftime("%Y-%m-%d")+".log"
        return log_path+"/"+log_file

    def __init_logger_handle(self):
        formatter = logging.Formatter(
            '%(asctime)s %(filename)s %(funcName)s %(lineno)s %(levelname)s --->%(message)s')
        self.fileStream.setFormatter(formatter)
        self.logger.addHandler(self.fileStream)

    def close(self):
        self.fileStream.close()
        self.logger.removeHandler(self.fileStream)

    def get_logger(self):
        return self.logger


if __name__ == "__main__":
    log = UserLog()
    logger = log.get_logger()
    logger.debug("yangqin")
    log.close
