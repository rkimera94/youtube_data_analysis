from .util import get_connection, get_connection_postgres


# build insert queries
def build_insert_query(table_name, column_names):

    column_names_str = ', '.join(column_names)

    column_values = tuple(
        map(lambda column: column.replace(column, '%s'), column_names))
    column_values_str = ', '.join(column_values)

    query = (f'''
    INSERT INTO {table_name} ({column_names_str}) VALUES ({column_values_str})
    ''')
    return query


def insert_data(connection, cursor, query, data, batch_size=200):
    recs = []
    count = 1
    for rec in data:
        recs.append(rec)
        if count % batch_size == 0:
            cursor.executemany(query, recs)
            connection.commit()
            recs = []
        count = count + 1
    cursor.executemany(query, recs)
    connection.commit()


# load table
def load_table(db_details, data, column_names, table_names):
    TARGET_DB = db_details['target']

    connection = get_connection_postgres(db_host=TARGET_DB['DB_HOST'],
                                         db_name=TARGET_DB['DB_NAME'],
                                         db_user=TARGET_DB['DB_USER'],
                                         db_pass=TARGET_DB['DB_PASS'])
    cursor = connection.cursor()
    query = build_insert_query(table_names, column_names)
    insert_data(connection, cursor, query, data)
    connection.close()
