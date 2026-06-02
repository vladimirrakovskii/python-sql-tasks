import psycopg2
from psycopg2.extras import execute_values

conn = psycopg2.connect('postgresql://postgres:@localhost:5432/test_db')


# BEGIN (write your solution here)
def batch_insert(connection, products_list):
    with connection.cursor() as curs:
        product_data = [(product['name'], product['price'], product['quantity']) for product in products_list]
        execute_values(curs, "INSERT INTO products (name, price, quantity) VALUES %s", product_data)

def get_all_products(connection):
    sql = "SELECT * from products ORDER BY price DESC;"
    with connection.cursor() as curs:
        curs.execute(sql)
        rows = curs.fetchall()
    return rows
# END
