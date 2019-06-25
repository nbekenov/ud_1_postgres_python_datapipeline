%run create_tables.py

%sql postgresql://<password>:<username>@127.0.0.1/<db_name>

%load_ext sql

%sql SELECT * FROM songplays LIMIT 5;