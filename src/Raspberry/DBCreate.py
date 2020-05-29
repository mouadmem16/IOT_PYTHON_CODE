import sqlite3

DB_Name = "IOT_DB.db"
TableSchema = """
    drop table if exists Heartbeat_data ;
    create table Heartbeat_data (
        id integer primary key autoincrement,
        SensorID text,
        PersonID text,
        Date_Time text,
        beat decimal(6,2),
        beats_Level text,
    );
"""

conn = sqlite3.connect(DB_Name)
curs = conn.cursor()

sqlite3.complete_statement(TableSchema)
curs.executescript(TableSchema)

curs.close()
conn.close()
