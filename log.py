import logging
from logging.handlers import TimedRotatingFileHandler
import os
import errno
import json

class Log:

    """
    python logging wrapper class
    """

    def __init__(self, logFileSection: str, fileName: str) -> None:
        self.logFileSection: str = logFileSection
        self.fileName: str = fileName
        self.logger = self.createLogger()

    def createLogger(self):
        logger = logging.getLogger(self.fileName)
        #出力するログの最低レベルを設定
        logger.setLevel(logging.DEBUG)
        handler = self.setHandler()
        logger.addHandler(handler)
        return logger

    def setHandler(self):

        """
        ハンドラーに各設定を追加
        """

        logFile = self.readConfigfile()
        # 日ごとにローテーションする設定
        handler = TimedRotatingFileHandler(
            logFile,
            when='midnight',
            backupCount=0,
            interval=7,
            encoding='utf-8'
        )

        formatter = logging.Formatter('%(asctime)s %(levelname)s {}\n%(message)s'.format(self.fileName))
        handler.setFormatter(formatter)

        return handler

    def readConfigfile(self):

        """
        コンフィグファイルを読み込む
        """

        configPath: str = os.path.dirname(__file__) + '/settings.json'

        if not os.path.exists(configPath):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), configPath)

        with open(configPath, 'r') as f:
            config = json.load(f)

        logFile = config[self.logFileSection]['FILE']

        return logFile

    def debug(self, message: str) -> None:

        """
        デバックレベルログを出力
        message: str エラーメッセージ
        """

        self.logger.debug(message)

    def info(self, message: str) -> None:

        """
        インフォレベルログを出力
        message: str エラーメッセージ
        """

        self.logger.info(message)

    def warn(self, message: str) -> None:

        """
        ワーニングレベルログを出力
        message: str エラーメッセージ
        """

        self.logger.warn(message)

    def error(self, message: str) -> None:

        """
        エラーレベルログを出力
        message: str エラーメッセージ
        """

        self.logger.error(message)

    def critical(self, message: str) -> None:

        """
        クリティカルレベルログを出力
        message: str エラーメッセージ
        """

        self.logger.critical(message)