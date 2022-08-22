from context_manager.lab3 import open_db


def test_open_db():
    with open_db(file_name="./test_lab3.db") as cursor:
        cursor.execute('CREATE TABLE IF NOT EXISTS "test_lab3"( "message" TEXT )')
        cursor.execute('INSERT INTO "test_lab3"("message") VALUES("python is ok")')
        cursor.execute('SELECT * FROM "test_lab3"')
        print(cursor.fetchall())