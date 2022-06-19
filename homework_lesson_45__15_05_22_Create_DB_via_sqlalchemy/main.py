import os

from homework_lesson_45__15_05_22_Create_DB_via_sqlalchemy.database_homework_45 import DATABASE_NAME

from homework_lesson_45__15_05_22_Create_DB_via_sqlalchemy import create_database_45 as db_creator

if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()