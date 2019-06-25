# DROP TABLES

songplay_table_drop = "drop table IF EXISTS  songplays"
user_table_drop = "drop table IF EXISTS users"
song_table_drop = "drop  table IF EXISTS songs"
artist_table_drop = "drop table IF EXISTS artists"
time_table_drop = "drop table IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
create TABLE IF NOT EXISTS songplays (
songplay_id SERIAL not null PRIMARY KEY,
start_time  bigint not null, 
user_id int not null,
level varchar not null, 
song_id varchar, 
artist_id varchar, 
session_id int not null, 
location varchar, 
user_agent varchar 
)
""")

user_table_create = ("""
create TABLE IF NOT EXISTS users (
user_id int not null primary key, 
first_name varchar not null, 
last_name varchar not null, 
gender char not null, 
level varchar not null
)
""")

song_table_create = ("""
create TABLE IF NOT EXISTS songs (
    song_id varchar not null primary key,
    title varchar  not null, 
    artist_id varchar not null,
    year int,
    duration decimal 
)
""")

artist_table_create = ("""
create TABLE IF NOT EXISTS artists (
    artist_id varchar not null primary key, 
    name varchar not null,
    location varchar,
    latitude decimal,
    longitude decimal 
)
""")

time_table_create = ("""
create TABLE IF NOT EXISTS time (
    start_time timestamp not null primary key,
    hour int not null,
    day int not null,
    week varchar not null,
    month varchar not null,
    year int not null,
    weekday varchar not null
)
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays
(start_time, user_id, level , song_id , artist_id , session_id , location , user_agent )
VALUES ( %s, %s,%s, %s, %s,%s, %s, %s)
""")

user_table_insert = ("""
insert into users (user_id , first_name , last_name , gender , level  )
    values(%s, %s, %s, %s, %s ) 
    ON CONFLICT(user_id)
    DO UPDATE 
        SET level = excluded.level
""")

song_table_insert = ("""
INSERT INTO songs (song_id,title, artist_id,year,duration) 
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT(song_id)
                DO NOTHING
""")

artist_table_insert = ("""
insert into artists (artist_id, name, location,latitude,longitude )
                values (%s,%s,%s,%s,%s)
                ON CONFLICT(artist_id)
                DO NOTHING
""")


time_table_insert = ("""insert into time (start_time,hour,day,week,month,year,weekday) \
                values (%s,%s,%s,%s,%s,%s,%s)
                ON CONFLICT(start_time)
                DO NOTHING
""")

# FIND SONGS

song_select = ("""
select s.song_id, s.artist_id from songs s 
    join artists a on s.artist_id=a.artist_id 
    where s.title=%s and a.name=%s and s.duration=%s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]