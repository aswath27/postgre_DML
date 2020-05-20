import psycopg2


try:
    connection = psycopg2.connect(
        user = "postgres",
        password = "Aswath27",
        host = "localhost",
        port = "5432",
        database = "test_db"
    )

   
    cursor = connection.cursor()
    print(connection.get_dsn_parameters(),"\n")
   
    
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected ")


except(Exception, psycopg2.Error) as error:
    print("Error connecting to PostgreSQL database", error)
    connection = None


finally:
    if(connection != None):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is now closed")