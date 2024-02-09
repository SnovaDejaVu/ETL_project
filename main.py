import pandas as pd
import psycopg2


def extract_data():

    conn = psycopg2.connect(
        dbname="sales_data",
        user="your_username",
        password="your_password",
        host="your_host"
    )

    cur = conn.cursor()

    cur.execute("SELECT * FROM sales_data")
    extracted_data = cur.fetchall()

    cur.close()
    conn.close()
    return extracted_data


def transform_data(t):
    df = data

    df['net_amount'] = df['total_amount'] - df['discount_amount'] + df['tax_amount']

    df['sale_date'] = pd.to_datetime(df['sale_date'])
    df['shipping_date'] = pd.to_datetime(df['shipping_date'])

    df = df[df['delivery_status'].isin(['shipped', 'delivered'])]

    df = df.drop(['discount_amount', 'tax_amount', 'total_amount'], axis=1)

    transformed_data = df
    return transformed_data


def load_data(l):
    conn = psycopg2.connect(
        database="my_database",
        user="my_user",
        password="my_password",
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()

    with open("create_tables.sql", "r") as file:
        cur.execute(file.read())

    for data in transformed_data:
        cur.execute("INSERT INTO my_table (column1, column2) VALUES (%s, %s)", (data[0], data[1]))

    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    data = extract_data()

    transformed_data = transform_data(data)

    load_data(transformed_data)



