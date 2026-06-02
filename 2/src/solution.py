import psycopg2

conn = psycopg2.connect('postgresql://postgres:@localhost:5432/test_db')


# BEGIN (write your solution here)
def make_cars_table(connection):
    sql = "CREATE TABLE cars (id SERIAL PRIMARY KEY, brand VARCHAR(255), model VARCHAR(255));"
    with connection.cursor() as curs:
        curs.execute(sql)

def populate_cars_table(connection, cars_list):
    with connection.cursor() as curs:
        for car in cars_list:
            curs.execute("INSERT INTO cars (brand, model) VALUES ((%(brand)s), (%(model)s));",
                         {"brand": car[0], "model": car[1]})

def get_all_cars(connection):
    sql = "SELECT * from cars ORDER BY model;"
    with connection.cursor() as curs:
        curs.execute(sql)
        rows = curs.fetchall()
    return rows
# END
