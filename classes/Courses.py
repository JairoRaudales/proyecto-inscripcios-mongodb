from classes.DbMongo import DbMongo
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
        collection = db["courses"]
        courses = collection.find()
        
        list_course = []
        for s in courses:
            temp_course = Courses(
                s["aprobados"]
                , s["reprobados"]
            )
            
            list_course.append(temp_course)
        return list_course
    
    
    @staticmethod
    def delete_all(db):
        list_e = Courses