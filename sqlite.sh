# create empty db with script
sqlite3 test.db ".databases"

sqlite3 test.db "CREATE TABLE Images( 
   NAME           TEXT    NOT NULL,
   TIME_Folder    TEXT    NOT NULL
);"

sqlite3 test.db "CREATE TABLE Images_det( 
   NAME           TEXT    NOT NULL,
   TIME_Folder    TEXT    NOT NULL,
   CATE_1         INT     DEFAULT 0,
   CATE_2         INT     DEFAULT 0,
   CATE_3         INT     DEFAULT 0,
   CATE_4         INT     DEFAULT 0,
   CATE_5         INT     DEFAULT 0,
   CATE_6         INT     DEFAULT 0,
   CATE_7         INT     DEFAULT 0,
   CATE_8         INT     DEFAULT 0,
   CATE_9         INT     DEFAULT 0,
   CATE_10        INT     DEFAULT 0,
   CATE_11        INT     DEFAULT 0,
   CATE_12        INT     DEFAULT 0,
   CATE_13        INT     DEFAULT 0
);"
