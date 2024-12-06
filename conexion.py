import psycopg2

try: 
    connection=psycopg2.connect(
        host='localhost',
        user='postgres',
        password='Mazapan2022!',
        database='mi_flask_app'
    )

    print("Conexión exitosa a la base de datos")
    cursor=connection.cursor()
    cursor.execute("SELECT version()")
    row=cursor.fetchone()
    print(row)

except Exception as ex:
    print("Ocurrió un error al conectar a la base de datos", ex)