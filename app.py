from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)

# VULNÉRABILITÉ 1 : Hardcoded secret
API_KEY = "sk_live_1234567890abcdef"  # ⚠️ Secret hardcodé

# VULNÉRABILITÉ 2 : SQL Injection
@app.route('/user')
def get_user():
    username = request.args.get('username')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # ⚠️ Concaténation de string dans SQL
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return str(cursor.fetchall())

# VULNÉRABILITÉ 3 : Path Traversal
@app.route('/file')
def read_file():
    filename = request.args.get('filename')
    # ⚠️ Pas de validation du chemin
    with open(filename, 'r') as f:
        return f.read()

# VULNÉRABILITÉ 4 : Weak cryptography
@app.route('/hash')
def hash_password():
    import hashlib
    password = request.args.get('password')
    # ⚠️ MD5 est obsolète et faible
    hashed = hashlib.md5(password.encode()).hexdigest()
    return hashed

# VULNÉRABILITÉ 5 : Debug mode en production
if __name__ == '__main__':
    # ⚠️ Debug=True expose des informations sensibles
    app.run(debug=True, host='0.0.0.0')