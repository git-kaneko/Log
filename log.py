import logging

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

        handler = logging.StreamHandler()
        #出力するログの最低レベルを設定
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(filename)s Line:%(lineno)s\n%(message)s')
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