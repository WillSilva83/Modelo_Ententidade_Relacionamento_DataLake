import os 

class Config: 
    OUTPUTLOCATION = os.getenv('OUTPUTLOCATION', 's3://teste/')

config = Config()