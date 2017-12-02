import sqlite3
from oslo.config import cfg
import pickle

# reading setting
opt_morestuff_group = cfg.OptGroup(name='morestuff',
                         title='A More Complex Example')

morestuff_opts = [
    cfg.StrOpt('img_path', default='No data',
               help=('setting for image path')),
    cfg.ListOpt('category', default=None,
                help=('A list of category')),
]
 
CONF = cfg.CONF
#regist each group  
CONF.register_group(opt_morestuff_group)
#regist opts to their group
CONF.register_opts(morestuff_opts, opt_morestuff_group)
CONF(default_config_files=['app.conf'])

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    categories = CONF.morestuff.category
    pickle.dump(categories, open("Currnet_cate.pkl", "wb"))
    print(categories)
    database = "yolo.db"

    # Images_det table
    sql_query_create_tasks_table = """CREATE TABLE Images_det(
       NAME           TEXT    NOT NULL,
       TIME_Folder    TEXT    NOT NULL,"""
    for i, cate in enumerate(categories):
        sql_query_create_tasks_table += cate+"         INT     DEFAULT 0"
        if (i+1) != len(categories):
            sql_query_create_tasks_table += ","
        sql_query_create_tasks_table += "\n"
    sql_query_create_tasks_table += ");"

    # minute_det table
    sql_query_create_min_table = """CREATE TABLE minute_det(
       TIME_Folder    TEXT    NOT NULL,"""
    for i, cate in enumerate(categories):
        sql_query_create_min_table += cate+"         INT     DEFAULT 0"
        if (i+1) != len(categories):
            sql_query_create_min_table += ","
        sql_query_create_tasks_table += "\n"
    sql_query_create_min_table += ");"

    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create Image_det table
        create_table(conn, sql_query_create_tasks_table)
        # create minute_det table
        create_table(conn, sql_query_create_min_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()
