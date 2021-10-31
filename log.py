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