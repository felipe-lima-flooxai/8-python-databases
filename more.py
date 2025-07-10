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
            "(%(name)s, %(age)s) "
        )

    data2 = (
        {"name": "Stan", "age": 100},
        {"name": "Maco", "age": 29},
        {"name": "Jani", "age": 55},
        {"name": "Cabaré", "age": 80},             
    )

    result = cursor.executemany(sql, data2)
    connection.commit() 

    with connection.cursor() as cursor:
        sql  = (
            f"SELECT * FROM {TABLE_NAME}"
        )
        cursor.execute(sql)

        data5 = cursor.fetchall()

        for row in data5:
            print(row)


    with connection.cursor() as cursor:
        menor_id = input("Digite um id menor")
        maior_id = input("Digite um id maior")
        sql  = (
            f"SELECT * FROM {TABLE_NAME} "
            f"WHERE id >= %s AND id <= %s "
        )
        cursor.execute(sql, (menor_id, maior_id))

        data5 = cursor.fetchone()

        for row in data5:
            print(row)




