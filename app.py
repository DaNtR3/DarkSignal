from flask import Flask, render_template, redirect, url_for
from routes.ui.auth_routes import auth_bp
from routes.ui.home_routes import home_bp
from routes.attacks.haveibeenpwned_routes import pwned_bp
from routes.attacks.attack_router import attack_bp
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
app.register_blueprint(auth_bp)
app.register_blueprint(home_bp)
app.register_blueprint(pwned_bp)
app.register_blueprint(attack_bp)


@app.route("/")
def index():
    return redirect(url_for("auth.authenticate"))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', custom_css='css/styles_404.css'), 404

if __name__ == '__main__':
    app.run(debug=True)