import psycopg2

try:
    connection = psycopg2.connect(user="r00t",
                                  password="thebuckstopshere!!",
                                  host="192.168.1.206",
                                  port="5432",
                                  dbname="PropertyData")
    cursor = connection.cursor()

    postgres_insert_query = """ INSERT INTO mobile (ID, MODEL, PRICE) VALUES (%s,%s,%s)"""
    record_to_insert = (5, 'One Plus 6', 950)
    cursor.execute(postgres_insert_query, record_to_insert)

    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into mobile table")

except (Exception, psycopg2.Error) as error:
    print("Failed to insert record into mobile table", error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")