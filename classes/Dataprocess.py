from classes.data import DATA
from classes.DbMongo import DbMongo
from classes.Students import Students
class Dataprocess:

    def __init__(self, data):
        self.data = data


    def create_careers(self,db):
        self.__collection = "Careers"
        collection = db.create_collection("Careers")
 
        return True
    
    def create_courses(self, db):
        self.__collection = "Courses"
        collection = db.create_collection("Courses")
        return True
    
    def create_students(self, db):
        self.__collection = "Students"
        collection = db.create_collection("Students")

        return True

    def create_enrollments(self, db):
        self.__collection = "Enrollments"
        collection = db.create_collection("Enrollments")
        return True
    
    @staticmethod
    def delete_all(db):
        list_e = Dataprocess

