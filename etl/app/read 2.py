from .util import get_connection


class readTable():
    def __init__(self, *args):
        super(self).__init__(*args)

    def read_table(db_details, table_name, limit=0):
        SOURCE_DB = db_details['source']
        connection = get_connection(db_type=SOURCE_DB['DB_TYPE'], db_host=SOURCE_DB['DB_HOST'],
                                    db_name=SOURCE_DB['DB_NAME'],
                                    db_user=SOURCE_DB['DB_USER'],
                                    db_pass=SOURCE_DB['DB_PASS'])
        cursor = connection.cursor()
        if limit == 0:
            query = f'SELECT * FROM {table_name}'
            
            print(query)
        else:
            query = f'SELECT * FROM {table_name} LIMIT{limit}'
        cursor.execute(query)
        col_data = cursor.description 
        column_names =  [i[0] for i in col_data]

        result = cursor.fetchall()
        connection.close()
        data = {"column_names":column_names,"data":result}



        return data
