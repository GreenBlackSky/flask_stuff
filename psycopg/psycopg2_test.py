import psycopg2

connection_data = {
    'user': 'john',
    'password': 'qwerty',
    'host': 'localhost',
    'port': '5432',
    'database': 'test'
}

create_table_query = '''
    CREATE TABLE test_table_1(
    ID serial PRIMARY KEY,
    FATHER_ID INT NOT NULL,
    MOTHER_ID INT NOT NULL
);'''

with psycopg2.connect(**connection_data) as connection:
    cursor = connection.cursor()
    cursor.execute(create_table_query)
    connection.commit()
    cursor.close()
