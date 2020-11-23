import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:

    @staticmethod
    def getAppURL():
        url=config.get('common info','baseurl')
        return url
    
    @staticmethod
    def getUsername():
        name=config.get('common info','username')
        return name
    
    @staticmethod
    def getPassword():
        pwd=config.get('common info','password')
        return pwd
