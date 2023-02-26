from classes.DbMongo import DbMongo
class Students:

    def __init__(self, nombre_completo, edad, cursos_aprovados,cursos_reprobados):
        self.nombre_completo = nombre_completo
        self.edad = edad
        self.cursos_aprovados = cursos_aprovados
        self.cursos_reprobados = cursos_reprobados
        self.__collection = "Student"

    def save(self, db):
        collection = db[self.__collection]
        result = collection.insert_one(self.__dict__)

    def delete(self, db):
        collection = db[self.__collection]
        filterToUse = { '_id' : self.__id }
        collection.delete_one(filterToUse)

        
  #  @staticmethod
   # def get_list(db):
   #    collection = db["student"]
   #    student = collection.find()
        
   #    list_estudiantes = []
        #for e in student:
         #   temp_students = Students(
          #      e["nombre_completo"]
           #     , e["edad"]
            #    , e["cursos_aprovados"]
             #   , e["cursos_reprobados"]
              #  , e["_id"]
            #)
            
            #list_estudiantes.append(temp_students)
        #return list_estudiantes
    
    
  ###  @staticmethod
   # def delete_all(db):
  #      list_e = Students
            
        
        
    
  



