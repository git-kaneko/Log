import logging

class Log:

    def createLogger(self) -> object:

        """
        logger生成関数
        """

        logger = logging.getLogger(__name__)
        #handlerに渡すログの最低レベルを設定
        logger.setLevel(logging.DEBUG)

        handler = self.setHandler()
        logger.addHandler(handler)

        return logger

    def setHandler(self) -> object:

        """
        ハンドラーに各設定を追加
        """

        handler = logging.StreamHandler()
        #出力するログの最低レベルを設定
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(module)s Line:%(lineno)s\n%(message)s')
        handler.setFormatter(formatter)

        return handler

    def debug(self, message: str):

        """
        デバックレベルログを出力
        message: str エラーメッセージ
        """

        logger = self.createLogger()
        logger.debug(message)

    def info(self, message: str):

        """
        インフォレベルログを出力
        message: str エラーメッセージ
        """

        logger = self.createLogger()
        logger.info(message)

    def warn(self, message: str):

        """
        ワーニングレベルログを出力
        message: str エラーメッセージ
        """

        logger = self.createLogger()
        logger.warn(message)

    def error(self, message: str):

        """
        エラーレベルログを出力
        message: str エラーメッセージ
        """

        logger = self.createLogger()
        logger.error(message)