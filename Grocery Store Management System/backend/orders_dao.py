from datetime import datetime
from sql_connection import get_sql_connection

def insert_order(connection, orders):
    cursor = connection.cursor()

    order_query = ("INSERT INTO orders "
             "(custmer_name, total, datetime)"
             "VALUES (%s, %s, %s)")
    order_data = (orders['custmer_name'], orders['grand_total'], datetime.now())

    cursor.execute(order_query, order_data)
    orders_id = cursor.lastrowid

    order_details_query = ("INSERT INTO order_details "
                           "(orders_id, products_id, quantity, total_price)"
                           "VALUES (%s, %s, %s, %s)")

    order_details_data = []
    for order_detail_record in orders['order_details']:
        order_details_data.append([
            orders_id,
            int(order_detail_record['products_id']),
            float(order_detail_record['quantity']),
            float(order_detail_record['total_price'])
        ])
    cursor.executemany(order_details_query, order_details_data)

    connection.commit()

    return orders_id

def get_order_details(connection, orders_id):
    cursor = connection.cursor()

    query = "SELECT * from order_details where order_id = %s"

    query = "SELECT order_details.orders_id, order_details.quantity, order_details.total_price, "\
            "products.product_name, products.price_per_unit FROM order_details LEFT JOIN products on " \
            "order_details.products_id = products.products_id where order_details.orders_id = %s"

    data = (orders_id, )

    cursor.execute(query, data)

    records = []
    for (orders_id, quantity, total_price, product_name, price_per_unit) in cursor:
        records.append({
            'orders_id': orders_id,
            'quantity': quantity,
            'total_price': total_price,
            'product_name': product_name,
            'price_per_unit': price_per_unit
        })

    cursor.close()

    return records

def get_all_orders(connection):
    cursor = connection.cursor()
    query = ("SELECT * FROM orders")
    cursor.execute(query)
    response = []
    for (orders_id, custmer_name, total, dt) in cursor:
        response.append({
            'orders_id': orders_id,
            'custmer_name': custmer_name,
            'total': total,
            'datetime': dt,
        })

    cursor.close()

    # append order details in each order
    for record in response:
        record['order_details'] = get_order_details(connection, record['orders_id'])

    return response

if __name__ == '__main__':
    connection = get_sql_connection()
    print(get_all_orders(connection))
    # print(get_order_details(connection,4))
    # print(insert_order(connection, {
    #     'custmer_name': 'dhaval',
    #     'total': '500',
    #     'datetime': datetime.now(),
    #     'order_details': [
    #         {
    #             'products_id': 1,
    #             'quantity': 2,
    #             'total_price': 50
    #         },
    #         {
    #             'products_id': 3,
    #             'quantity': 1,
    #             'total_price': 30
    #         }
    #     ]
    # }))