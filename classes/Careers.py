from classes.DbMongo import DbMongo
from classes.data import DATA
from classes.Dataprocess import Dataprocess
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
        
    @staticmethod
    def get_list(db):
       collection = Dataprocess.create_careers
       careers = collection.find()
        
       list_estudiantes = []
       for careers in DATA:
            temp_students = Careers(
                collection.insert_one("Carrera:")
            )
            
            list_estudiantes.append(temp_students)
       return list_estudiantes
    
    
    @staticmethod
    def delete_all(db):
        list_e = Careers