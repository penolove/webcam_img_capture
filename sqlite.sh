# create empty db with script
sqlite3 webcam.db ".databases"

sqlite3 webcam.db "CREATE TABLE Images( 
   NAME           TEXT    NOT NULL,
   TIME_Folder    TEXT    NOT NULL
);"

sqlite3 yolo.db ".databases";
python sqlite.py;
