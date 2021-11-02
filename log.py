import logging
import configparser
import os
import errno

class Log:

    def __init__(self):

        self.logger = logging.getLogger(__name__)
        #handlerに渡すログの最低レベルを設定
        self.logger.setLevel(logging.DEBUG)

        self.handler = self.setHandler()
        self.logger.addHandler(self.handler)

    def setHandler(self) -> object:

        """
        ハンドラーに各設定を追加
        """

        logMode, logFile = self.readConfigfile()

        if logMode == 'dev':

            #出力するログの最低レベルを設定
            handler.setLevel(logging.DEBUG)
        
        else:

            #出力するログの最低レベルを設定
            handler.setLevel(logging.INFO)

        handler = logging.FileHandler(logFile)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(filename)s\n%(message)s')
        handler.setFormatter(formatter)

        return handler

    def readConfigfile(self):

        """
        コンフィグファイルを読み込む
        """

        config = configparser.ConfigParser()
        configPath = 'config.ini'

        if not os.path.exists(configPath):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), configPath)

        config.read('config.ini', encoding='utf-8')

        logMode = config.get('LOG', 'MODE')
        logFile = config.get('LOG', 'FILE')

        return logMode, logFile

    def debug(self, message: str):

        """
        デバックレベルログを出力
        message: str エラーメッセージ
        """

        self.logger.debug(message)

    def info(self, message: str):

        """
        インフォレベルログを出力
        message: str エラーメッセージ
        """

        self.logger.info(message)

    def warn(self, message: str):

        """
        ワーニングレベルログを出力
        message: str エラーメッセージ
        """

        self.logger.warn(message)

    def error(self, message: str):

        """
        エラーレベルログを出力
        message: str エラーメッセージ
        """

        self.logger.error(message)

    def critical(self, message: str):

        """
        クリティカルレベルログを出力
        message: str エラーメッセージ
        """

        self.logger.critical(message)