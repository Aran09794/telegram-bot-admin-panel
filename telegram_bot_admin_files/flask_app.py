
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

# Crea l'app Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admins.db'
app.config['SECRET_KEY'] = 'randomsecretkey'

db = SQLAlchemy(app)

# Modello per gli Admin
class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

# Homepage (login)
@app.route('/')
def index():
    return render_template('login.html')

# Login Handler
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    admin = Admin.query.filter_by(username=username, password=password).first()
    if admin:
        return redirect(url_for('admin_dashboard'))
    else:
        return "Invalid credentials"

# Dashboard degli admin
@app.route('/admin')
def admin_dashboard():
    return render_template('admin_dashboard.html')

# Avvia il server
if __name__ == '__main__':
    db.create_all()  # Crea il database
    app.run(debug=True)
