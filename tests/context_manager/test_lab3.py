from context_manager.lab3 import open_db


def test_open_db():
    with open_db(file_name="./test.db") as cursor:
        cursor.execute('CREATE TABLE IF NOT EXISTS "test"( "message" TEXT )')
        cursor.execute('INSERT INTO "test"("message") VALUES("python is ok")')
        cursor.execute('SELECT * FROM "test"')
        print(cursor.fetchall())
