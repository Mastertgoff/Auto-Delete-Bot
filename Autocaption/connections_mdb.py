import os
import pymongo
from info info ACC_DB, DATABASE_NAME


myclient = pymongo.MongoClient(ACC_DB)
#@Nothing                               
mydb = myclient[DATABASE_NAME]
mycol = mydb['CONNECTION']
