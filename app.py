from flask import Flask, render_template, request, redirect, url_for
from src.handlers.year_handler import current_year

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # For now, just get the posted username and password
        username = request.form['username']
        password = request.form['password']
        # Add authentication logic here
        return f"Logged in as {username}"
    return render_template('login.html', custom_css='css/styles_login.css', current_year=current_year())

if __name__ == '__main__':
    app.run(debug=True)