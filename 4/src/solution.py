import psycopg2
from psycopg2.extras import DictCursor


conn = psycopg2.connect('postgresql://postgres:@localhost:5432/test_db')


# BEGIN (write your solution here)
def get_order_sum(connection, month):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT 
                customers.customer_name,
                SUM(orders.total_amount) as total_sum
            FROM customers
            JOIN orders ON customers.customer_id = orders.customer_id
            WHERE EXTRACT(MONTH FROM orders.order_date) = %s
            GROUP BY customers.customer_id, customers.customer_name
            ORDER BY customers.customer_name
        """, (month,))

        results = cursor.fetchall()

        lines = []
        for row in results:
            customer_name = row[0]
            total_sum = row[1]
            lines.append(f"Покупатель {customer_name} совершил покупок на сумму {total_sum}")

        return "\n".join(lines)
# END
