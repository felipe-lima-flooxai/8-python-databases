import pymysql
import dotenv
import os
TABLE_NAME = "customers"

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ["MYSQL_HOST"],
    user=os.environ["MYSQL_USER"],
    password=os.environ["MYSQL_PASSWORD"],
    database=os.environ["MYSQL_DATABASE"],
)
with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS {TABLE_NAME} "
            "( "
            "id INT NOT NULL AUTO_INCREMENT), "
            "name VARCHAR(50) NOT NULL, "
            "age INT NOT NULL "
            "PRIMARY KEY (id)"
            ") "
        )
        

    with connection.cursor() as cursor:
        sql = ( 
        f"INSERT INTO {TABLE_NAME} "
            "(name, age) " \
            "VALUES "
            "(%s, %s) "
        )
        result = cursor.execute(sql, ("Luiz", 18))

        connection.commit()

    with connection.cursor() as cursor:
        sql = ( 
        f"INSERT INTO {TABLE_NAME} "
            "(name, age) " \
            "VALUES "
            "(%(name)s, %(age)s) "
        )

        data = {
            "name": "Stan",
            "age": 100
        }

        result = cursor.execute(sql, data)

        print(cursor)

