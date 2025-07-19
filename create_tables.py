import configparser, psycopg2
from sql_queries import *

def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect(
        host=config['CLUSTER']['HOST'],
        dbname=config['CLUSTER']['DB_NAME'],
        user=config['CLUSTER']['DB_USER'],
        password=config['CLUSTER']['PASSWORD'],
        port=config['CLUSTER']['PORT'])
    cur = conn.cursor()

    for q in [staging_events_drop, staging_songs_drop, songplay_drop,
              users_drop, songs_drop, artists_drop, time_drop]:
        cur.execute(q); conn.commit()

    for q in [staging_events_table_create, staging_songs_table_create,
              songplay_table_create]:
        cur.execute(q); conn.commit()

    conn.close()

if __name__ == "__main__":
    main()