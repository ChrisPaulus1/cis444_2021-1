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

    password_from_user_form = request.form['password']
    user = {
            "sub" : request.form['firstname'] #sub is used by pyJwt as the owner of the token
            }
    if not user:
        return json_response(status_=401, message = 'Invalid credentials', authenticated =  False )

    return json_response( token = create_token(user) , authenticated = True)








 #   logger.debug("Login Handle Request")
    #use data here to auth the user

    
  #  password_form = request.form['password']
   # user = {
    #        "sub" : request.form['username'] #sub is used by pyJwt as the owner of the token
     #       }
    

    #cur = g.db.cursor()
 
    #cur.execute(f"select * from users where user_name = '{request.form['username']}';")
    


    #cur.execute("select * from users where password = '{password_form}';")
  #  cur.execute("select * from users where password = 'Danny_Password';")
#    cur.execute("select user_name from users where password = '{password_form}';")
   
    #print(password_form)
    
   #-- print(f"{password_form}" )

   
    #db_pass = cur.fetchone()
   
#    print(request.form)

    #--print(request.form['password'])

 
    #print(f"select * from users where user_name = {request.form['username']};")
    
   # print(f"select * from users where user_name = '{request.form['username']}';")

 # print(db_pass)
  
    #--logger.debug(db_pass)
    



    #if bcrypt.checkpw(bytes(request.form['password'], "utf-8"), bytes(db_pass[2], "utf-8")) == True:
     #   logger.debug("Login Was Sucessful!!!")
      #  return json_response( token = create_token(user) , authenticated = True)


   # if db_pass is None:
    #    logger.debug("IN DB_PASS IS NONE")
     #   return json_response(status_=401, message = 'USERNAME IS NOT FOUND', authenticated =  False )

   # else:
        #print("Password does not match!!")
    #    return json_response(status_=401, message = 'PASSWORD DOES NOT MATCH', authenticated =  False )
    


   # if bcrypt.checkpw(bytes(request.form['password'], "utf-8"), bytes(db_pass[2], "utf-8")) == True:
    #    logger.debug("Login Was Sucessful!!!")
     #   return json_response( token = create_token(user) , authenticated = True)
