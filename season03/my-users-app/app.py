from flask import Flask
from flask import render_template
from flask import session
from flask import request
from flask import jsonify
from my_user_model import User

app = Flask(__name__, template_folder='views')
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def hello_world():
    return f"<p>Hello, World!</p>"

@app.route("/users", methods=['POST'])
def create_user():
    User.create({x:request.args.get(x) for x in \
        ["firstname", "lastname", "age", "password", "email"]
    })
    return f"<p>Created</p>"

@app.route("/users", methods=['GET'])
def get_all_users():
    #return jsonify(User.all())
    return render_template('index.html', users=User.all())

@app.route("/users", methods=['PUT'])
def update_user_password():
    if 'user_id' not in session: return f"<p>Sign in please</p>"
    password = request.args.get('password')
    if not password: return f"<p>provide password please</p>"
    User.update(session['user_id'], 'password', password)
    return f"<p>Done</p>"

@app.route("/users", methods=['DELETE'])
def delete_user():
    if 'user_id' not in session: return f"<p>Sign in please</p>"
    User.destroy(session['user_id'])
    return f"<p>Done</p>"

@app.route("/sign_in", methods=['POST'])
def sign_in():
    user = User.get_email(request.args.get("email"))
    if not user: return f"<p>Get out</p>"
    user_id, firstname, lastname, age, password, email = user
    if password!=request.args.get("password"): return f"<p>Get out</p>"
    session["user_id"] = user_id

@app.route("/sign_out", methods=['DELETE'])
def sign_out():
    session.pop('user_id', None)
    return f"<p>Signed out</p>"