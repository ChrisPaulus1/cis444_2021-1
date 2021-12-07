
from flask import Flask, render_template, request, jsonify

#app = Flask(__name__)





def handle_request():

        email = request.form['email']
        name = request.form['name']

        message = request.form['message']

        if name and email and message:
                newName = "Thank you for your request " + name + "."
                print("Success! I will get back to you ASAP.")
                return jsonify({'name' : newName})

        return jsonify({'error' : 'Missing data!'})

#if __name__ == '__main__':
 #   app.run(host='0.0.0.0', port=80)
