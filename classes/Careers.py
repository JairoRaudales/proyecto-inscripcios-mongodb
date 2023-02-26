from classes.DbMongo import DbMongo
from classes.data import DATA
class Careers:

    def __init__(self, carrera_1, carrera_2):
        self.carrera_1 = carrera_1
        self.carrera_2 = carrera_2
        self.__collection = "Careers"

    def save(self, db):
        collection = db[self.__collection]
        result = collection.insert_one(self.__dict__)


    def update(self, db):
        collection = db[self.__collection]
        filterToUse = {'_id':self._id}
        objstore = {'$set':self.__dict__}
        collection.update_one(filterToUse, objstore)
        
    def delete(self, db):
        collection = db[self.__collection]
        filterToUse = { '_id' : self.__id }
        collection.delete_one(filterToUse)
        
    @staticmethod
    def get_list(db):
        collection = db["career"]
        Career = collection.find()
        
        list_careers = []
        for e in DATA:
            temp_career = Careers(
                e["carrera"]
            )
            
            list_careers.append(temp_career)
        return list_careers
    
    @staticmethod
    def delete_all(db):
        list_e = Careers