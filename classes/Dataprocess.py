from classes.data import DATA
from classes.DbMongo import DbMongo
class Dataprocess:

    def __init__(self, data):
        self.data = data


    def create_careers(self,db):
        self.__collection = "Careers"
        collection = db.create_collection("Careers")
        result = collection.insert_one(self.__dict__)
        Careers = collection

        DATA = Careers["carrera"]




        return True
    
    def create_courses(self, db):
        self.__collection = "Courses"
        collection = db.create_collection("Courses")
        result = collection.insert_one(self.__dict__)

 
        return True
    
    def create_students(self, db):
        self.__collection = "Students"
        collection = db.create_collection("Students")
        result = collection.insert_one(self.__dict__)

 


        return True

    def create_enrollments(self, db):
        self.__collection = "Enrollments"
        collection = db.create_collection("Enrollments")
        result = collection.insert_one(self.__dict__)
        enrollments = collection

        return True
