from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token

from tools.logging import logger

#global_db_con = get_db()

def handle_request():
    logger.debug("Get Books Handle Request")

    cur = g.db.cursor()
    #cur =global_db_con.cursor()

    cur.execute("select * from books_table;")

    bookList= cur.fetchall()

    # if books_table is None:
     #    print("Nothing")


    return json_response( token = create_token(  g.jwt_data ) , books= bookList)
