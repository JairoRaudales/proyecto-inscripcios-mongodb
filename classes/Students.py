from classes.DbMongo import DbMongo
from classes.data import DATA
from classes.Dataprocess import Dataprocess
class Students:

    def __init__(self,id = ""): 
        self.__collection = "Student"

    def save(self, db):
        collection = db[self.__collection]
        result = collection.insert_one(self.__dict__)

    def delete(self, db):
        collection = db[self.__collection]
        filterToUse = { '_id' : self.__id }
        collection.delete_one(filterToUse)

    @staticmethod
    def delete_all(db):
        list_e = Students
            
        
    
  



