import configparser, psycopg2
from sql_queries import staging_events_copy, staging_songs_copy, songplay_table_insert

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
    iam = config['IAM_ROLE']['ARN']

    for q in [staging_events_copy.format(iam), staging_songs_copy.format(iam)]:
        cur.execute(q); conn.commit()

    cur.execute(songplay_table_insert); conn.commit()
    conn.close()

if __name__ == "__main__":
    main()