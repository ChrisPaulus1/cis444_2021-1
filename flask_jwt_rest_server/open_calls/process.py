
from flask import Flask, render_template, request, jsonify

#app = Flask(__name__)
from db_con import get_db_instance, get_db


global_db_con = get_db()


def handle_request():


    cur = global_db_con.cursor()
    cur.execute(" select * from FormData;")

    email = request.form['email']
    name = request.form['name']
    message = request.form['message']

    if name and email and message:
        newName = "Thank you for your request " + name + "."
        print("Success! I will get back to you ASAP.")
    
        cur.execute("INSERT INTO FormData (email, name, message) VALUES ('"+str (request.form['email']) + "', '" + str (request.form['name']) + "', '" + str(request.form['message']) + "');") 

        global_db_con.commit()
        cur.execute("select * from FormData;")
        for r in cur.fetchall():
            print(r)


        return jsonify({'name' : newName})
        
    return jsonify({'error' : 'Missing data!'})

