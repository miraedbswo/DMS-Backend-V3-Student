import psycopg2


def lambda_handler(event, context):
    database = {
        'host': '52.199.207.14',
        'database': 'dms',
        'user': 'dms',
        'password': 'root',
        'port': 5432
    }

    conn = psycopg2.connect(**database)
    cursor = conn.cursor()

    cursor.execute("TRUNCATE extension_apply;")
    conn.commit()
    cursor.close()
    conn.close()

