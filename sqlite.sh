# create empty db with script
sqlite3 test.db ".databases"
sqlite3 test.db "CREATE TABLE Images( 
   NAME           TEXT    NOT NULL,
   TIME_Folder    TEXT    NOT NULL,
   CATE_1         INT     DEFAULT 0,
   CATE_2         INT     DEFAULT 0,
   CATE_3         INT     DEFAULT 0,
   CATE_4         INT     DEFAULT 0,
   CATE_5         INT     DEFAULT 0
);"
