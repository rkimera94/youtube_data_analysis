import sys
from app.util import get_tables, load_db_details
from app.read import readTable


def read_table_data():
    db_details = load_db_details()
    tables = get_tables('table_list')

    for table_name in tables['table_name']:

        data = readTable.read_table(db_details, table_name)
        print(f'reading data for loading {table_name}')

        #column_names = data['column_names']
        return data

