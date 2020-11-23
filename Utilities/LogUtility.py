import logging

class Loggen:
    
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Logs\\Automation.log",
                            format='%(asctime)s;  %(levelname)s;  %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',
                            filemode='w')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
