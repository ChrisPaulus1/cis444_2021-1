import psycopg2


def get_db():
    return psycopg2.connect(host="localhost", dbname="books" , user="chris", password="test_password")

def get_db_instance():  
    db  = get_db()
    cur  = db.cursor()

    return db, cur 



if __name__ == "__main__":
    db, cur = get_db_instance()

   # cur.execute("create table FormData ( email varchar(255), name varchar(255), message varchar(255));")


    #db.commit()






    #cur.execute("select * from users")
    #for r in cur.fetchall():
     #      print(r)
    #db_pass = cur.fetchall()

   # print(db_pass)
