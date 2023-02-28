import pymongo
from classes import Students, DbMongo, Careers, Dataprocess, DATA, Courses, Enrollments
from dotenv import load_dotenv

def main():
    client, db = DbMongo.getDB()





    pipeline = Dataprocess(DATA)

    pipeline.create_careers(db)
    pipeline.create_students(db)
    pipeline.create_enrollments(db)
    pipeline.create_courses(db)

    return True

    client.close()

if __name__  == "__main__":
    load_dotenv()
    main()

