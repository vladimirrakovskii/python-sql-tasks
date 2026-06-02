import psycopg2

conn = psycopg2.connect('postgresql://postgres:@localhost:5432/test_db')


# BEGIN (write your solution here)
def add_movies(connection):
    sql = "INSERT INTO movies (title, release_year, duration) VALUES ('Godfather', 1972, 175);"
    cursor = connection.cursor()
    cursor.execute(sql)
    cursor.close()

    sql2 = "INSERT INTO movies (title, release_year, duration) VALUES ('The Green Mile', 1999, 189);"
    cursor = connection.cursor()
    cursor.execute(sql2)
    cursor.close()

def get_all_movies(connection):
    sql = "SELECT * from movies;"
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    return rows
# END
