

1. Install Anaconda
2. Open jupyter notebook. 
3. Set up postgres database server. Create database aviyel




Navigate to the 'aviyel/src' directory using Anaconda jupyter notebook.
DIRECTORY: 'aviyel/src' 

DEFINE VARIABLE: in the  youtube_data_analysis_aviyel.ipynb file.

Database Connection: Please enter the database Connection parameters. 
user, password,host,port,dbname

EXECUTE FILE youtube_data_analysis_aviyel.ipynb  in  the src folder. Using the RUN: button on the jupyter notebook top menu.
 





2.PYTHON  ETL TOOL. 

Set up a free running ETL pipeline for continuous data analysis: 

ETL tool will pick published data from the source database, i.e. data capture from the youtube api. 
The do analysis on  the data, transform the data, and store the aggregated data in the target database. 

Python flask: setting up the app/tool server. 
API:  routes to fetch, process, and load data. (which can be integrated in a UI admin panel to enable users manage the processes)

CLONE JOBS: Using job scheduling for the tool to automatically check the source data, if there is published data. Setting time intervals
            The tool to always run queries to check for published data in a give time interval. 


PROJECT 


step: A

setup  python Virtual environment:  e.g.   python3 -m venv venv  

(https://flask.palletsprojects.com/en/2.0.x/installation/)

Active the Virtual environment {venv} And Install the following packages. 


setup flask server:  pip install Flask
Install pandas:  pip install pandas
Install python-decouple : pip install python-decouple
Install mysql connector: pip install mysql-connector-python
Install postgres connector: pip install psycopg2


step B 

create .env file: Define database connection variables for both the Source db and Target Database. 


# source database 
DB_DATABASE_NAME= 
DB_PORT=
DB_USERNAME= 
DB_PASSWORD= 
DB_HOST=  localhost
DB_DIALECT=
DB_OPERATORSALIASES=

# target database 
DB_TARGET= 
DB_PORT=
DB_USERNAME= 
DB_PASSWORD= 
DB_HOST=  
DB_DIALECT=
DB_OPERATORSALIASES=


Step c. 

open terminal at the etl director: 



DEVELOPMENT: 

- setting tool to read from source database and load to the target database:  "COMPLETE"
edit text file table_list: to indicate which table to copy. The function will copy all columns. 


1. RUN: 
python3 main.py 

check the target database if data is loaded successfully 

- Adding analysis functions to process data.  "PENDING" 

- Measure code performance and store in database " PENDING"

-  Setting up Time intervals for fetching data. "PENDING"
- 