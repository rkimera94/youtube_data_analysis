#from flask import Flask
#from flask_restful import Api
import sys
#from config import DB_DETAILS
from app.util import get_tables, load_db_details
from app.read import readTable
from app.write import build_insert_query, load_table

# test env request


def main():
    #env = sys.argv[1]
    db_details = load_db_details()
    # print(db_details)
    tables = get_tables('table_list')

    #column_names = ('id','video_id', 'kind', 'created_at','updated_at')
    # table_name = 'yt_videos'

    for table_name in tables['table_name']:

        data = readTable.read_table(db_details, table_name)
        print(f'reading data for loading {table_name}')

        column_names = data['column_names']

        print(build_insert_query(table_name, column_names))
        print(f'loading data for table {table_name}')

        load_table(db_details, data['data'], column_names, table_name)


if __name__ == "__main__":
    main()
# debug = true for test environments
