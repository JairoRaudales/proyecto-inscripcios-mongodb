from classes.data import DATA
from classes.DbMongo import DbMongo
class Dataprocess:

    def __init__(self, data):
        self.data = data


    def create_careers(self,db):
        self.__collection = "Careers"
        collection = db.create_collection("Careers")

        for diccionario in DATA:
            careers = {"carrera": diccionario["carrera"]}
            collection.insert_one(careers)

        return True
    
    def create_courses(self, db):
        self.__collection = "Courses"
        collection = db.create_collection("Courses")

        for diccionario in DATA:
            courses = {"curso aprobados": diccionario["cursos_aprobados"]
                       , "cursos reprobados": diccionario["cursos_reprobados"]}
            collection.insert_one(courses)

        return True
    
    def create_students(self, db):
        self.__collection = "Students"
        collection = db.create_collection("Students")
        for diccionario in DATA:
            courses = {"numero de cuenta": diccionario["numero_cuenta"]
                       , "nombre completo": diccionario["nombre_completo"]
                       , "cursos aprobados": diccionario["cursos_aprobados"]
                       , "cursos reprobados": diccionario["cursos_reprobados"]
                       , "edad": diccionario["edad"]
                       , "carrera": diccionario["carrera"]}
            collection.insert_one(courses)        

        return True

    def create_enrollments(self, db):
        self.__collection = "Enrollments"
        collection = db.create_collection("Enrollments")
        result = collection.insert_one(self.__dict__)
        enrollments = collection

        return True
