import logging
import configparser
import os
import errno
import json

class Log:

    def __init__(self, logFileSection: str, myFileName: str):

        self.myFileName = myFileName
        self.logFileSection = logFileSection
        self.logger = logging.getLogger(myFileName)
        #handlerに渡すログの最低レベルを設定
        self.logger.setLevel(logging.DEBUG)

        self.handler = self.setHandler()
        self.logger.addHandler(self.handler)

    def setHandler(self) -> object:

        """
        ハンドラーに各設定を追加
        """

        logMode, logFile = self.readConfigfile()
        handler = logging.FileHandler(logFile)

        if logMode == 'dev':

            #出力するログの最低レベルを設定
            handler.setLevel(logging.DEBUG)
        
        else:

            #出力するログの最低レベルを設定
            handler.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s %(levelname)s {}\n%(message)s'.format(self.myFileName))
        handler.setFormatter(formatter)

        return handler

    def readConfigfile(self):

        """
        コンフィグファイルを読み込む
        """

        configPath = os.path.dirname(__file__) + '/settings.json'

        if not os.path.exists(configPath):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), configPath)

        with open(configPath, 'r') as f:
            config = json.load(f)

        logMode = config['MODE']
        logFile = config[self.logFileSection]['FILE']

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