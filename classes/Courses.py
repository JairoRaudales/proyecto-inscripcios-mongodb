from classes.DbMongo import DbMongo
from classes.Dataprocess import Dataprocess
from classes.data import DATA
class Courses:

    def __init__(self,aprobados, reprobados):
        self.aprobados = aprobados
        self.reprobados = reprobados
        self.__collection = "Courses"

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
       collection = Dataprocess.create_courses
       courses = collection.find()
        
       list_estudiantes = []
       for courses in DATA:
            temp_students = Courses(
            )
            
            list_estudiantes.append(temp_students)
       return list_estudiantes