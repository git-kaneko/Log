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