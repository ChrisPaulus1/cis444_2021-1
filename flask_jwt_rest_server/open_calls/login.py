from flask import request, g
from flask_json import FlaskJSON, JsonError, json_response, as_json
from tools.token_tools import create_token

from db_con import get_db_instance, get_db
from tools.logging import logger

import bcrypt
import psycopg2



def handle_request():


    logger.debug("Login Handle Request")
    #use data here to auth the user

    
    password_form = request.form['password']
    user = {
            "sub" : request.form['username'] #sub is used by pyJwt as the owner of the token
            }
    

    cur = g.db.cursor()
  
    cur.execute("select * from users where user_name = '{password_form}';")
   
    db_pass = cur.fetchone()
    
    print(db_pass)
  
    logger.debug(db_pass)
    


    if db_pass is None:
        logger.debug("IN DB_PASS IS NONE")
        return json_response(status_=401, message = 'USERNAME IS NOT FOUND', authenticated =  False )

    else:
        #print("Password does not match!!")
        return json_response(status_=401, message = 'PASSWORD DOES NOT MATCH', authenticated =  False )
    


    if bcrypt.checkpw(bytes(request.form['password'], "utf-8"), bytes(db_pass[2], "utf-8")) == True:
        logger.debug("Login Was Sucessful!!!")
        return json_response( token = create_token(user) , authenticated = True)
