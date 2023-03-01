from classes.DbMongo import DbMongo
class Enrollments:

    def __init__(self,nombre, carrera, curso):
        self.nombre = nombre
        self.carrera = carrera
        self.curso = curso
        self.__collection = "Enrollments"

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
    def delete_all(db):
        list_e = Enrollments