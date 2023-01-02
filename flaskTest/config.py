class Config(object):
    
    NAME = "Base"

class Production(Config):
    pass


class Dev(Config):
   NAME = "DEv"