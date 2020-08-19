# * Running on http://127.0.0.1:5000/

from flask import Flask, jsonify, render_template, request, redirect, session
import sys
import copy
import rospy
from control_publisher import RobotBehaviour

app = Flask(__name__)
app.secret_key = "woz" 

#session = { user_name: ""; user_surname= ""}

@app.route('/')
def index(name=None):
    return redirect('/login');

@app.route('/login', methods=['GET', 'POST'])
def login(name=None,):
    if request.method=='POST':
        if (not len( request.form.get('fname') ) or not len( request.form.get('lname') ) ):
            print("error");
            return render_template('login.html', name=name)
        else:
            print(request.form);
            session['user_name'] = request.form.get('fname');
            session['user_surname'] = request.form.get('lname');
            return render_template('scenarios.html', name=name)
		
		
    return render_template('login.html', name=name)

	
@app.route('/reactions')
def reactions(name=None):
    if not session.get('user_name') or not len(session.get('user_name')) or not len( session.get('user_surname') ) :
        return redirect('/');

    return render_template('reactions.html', name=name)

@app.route('/scenarios')
def scenarios(name=None):
    if not session.get('user_name') or not len(session.get('user_name')) or not len( session.get('user_surname') ) :
        return redirect('/');

    return render_template('scenarios.html', name=name)

	
# woz_command can send ros messages and call ros services
@app.route("/woz",methods=['POST'])
def woz_command():
    payload = request.get_json() 
    prenom = request.form.get('fname')
    print(payload)
    behaviour = RobotBehaviour()
    behaviour.load_info(payload['command'],prenom)
    behaviour.realisation()
    return ("nothing")

	
if __name__ == "__main__":
    rospy.init_node("flask_interface",anonymous=True)
    try:
        app.run(host= '0.0.0.0',threaded=True)
    except KeyboardInterrupt:
        print("exiting")
