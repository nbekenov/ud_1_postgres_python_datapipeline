# ud_1_postgres_python_datapipeline

The puprose of the project is to prepare data for analytical team.
The project consists of the script which create tables in Postgres database and ETL pipeline that loads data from the json files which contains users activity in the app and metadata about the songs into Postgres tables.

## Getting Started
1. execute create_tables.py - this script creates database sparkifydb and all needed tables in it.
2. to test that tables were created run 
2. execute etl.py - this script will proccess all json files and insert data into Postgres tables

### Prerequisites
```
Python 3
Postgres Database
```

## Running the tests
Run test.py to confirm your records were successfully inserted into each table.

## Data model
Data model is represnted in star schema  which consists of
fact table: songplays
and dimension tables: users,songs,artists,time
