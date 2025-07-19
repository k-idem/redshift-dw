staging_events_drop = "DROP TABLE IF EXISTS staging_events;"
staging_songs_drop  = "DROP TABLE IF EXISTS staging_songs;"
songplay_drop = "DROP TABLE IF EXISTS songplays;"
users_drop    = "DROP TABLE IF EXISTS users;"
songs_drop    = "DROP TABLE IF EXISTS songs;"
artists_drop  = "DROP TABLE IF EXISTS artists;"
time_drop     = "DROP TABLE IF EXISTS time;"


staging_events_table_create = ("""
CREATE TABLE staging_events (
    artist          TEXT,
    auth            TEXT,
    firstName       TEXT,
    gender          TEXT,
    itemInSession   INT,
    lastName        TEXT,
    length          FLOAT,
    level           TEXT,
    location        TEXT,
    method          TEXT,
    page            TEXT,
    registration    BIGINT,
    sessionId       INT,
    song            TEXT,
    status          INT,
    ts              BIGINT,
    userAgent       TEXT,
    userId          INT
);
""")

staging_songs_table_create = ("""
CREATE TABLE staging_songs
( num_songs        INT,
  artist_id        TEXT,
  artist_latitude  FLOAT,
  artist_longitude FLOAT,
  artist_location  TEXT,
  artist_name      TEXT,
  song_id          TEXT,
  title            TEXT,
  duration         FLOAT,
  year             INT );
""")

songplay_table_create = ("""
CREATE TABLE songplays
( playid INT IDENTITY(0,1) PRIMARY KEY,
  start_time TIMESTAMP,
  userid INT,
  level  TEXT,
  songid TEXT,
  artistid TEXT,
  sessionid INT,
  location TEXT,
  useragent TEXT );
""")


staging_events_copy = ("""
COPY staging_events
FROM 's3://udacity-dend/log_data'
IAM_ROLE '{}'
REGION 'us-west-2'
JSON 'auto'
TIMEFORMAT 'epochmillisecs';
""")

staging_songs_copy = ("""
COPY staging_songs
FROM 's3://udacity-dend/song_data'
IAM_ROLE '{}'
REGION 'us-west-2'
JSON 'auto';
""")


songplay_table_insert = ("""
INSERT INTO songplays (start_time, userid)
SELECT TIMESTAMP 'epoch' + se.ts/1000 * INTERVAL '1 second',
       se.userid
FROM staging_events se
WHERE se.page = 'NextSong';
""")