from flask import Flask, render_template, redirect, url_for
from src.routes.ui.auth_routes import auth_bp
from src.routes.ui.home_routes import home_bp
from src.routes.attacks.haveibeenpwned_routes import pwned_bp
from src.routes.attacks.attack_router import attack_bp
from dotenv import load_dotenv
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import os

load_dotenv()

app = Flask(__name__, template_folder="src/templates", static_folder="src/static")
app.secret_key = os.getenv("SECRET_KEY")
app.register_blueprint(auth_bp)
app.register_blueprint(home_bp)
app.register_blueprint(pwned_bp)
app.register_blueprint(attack_bp)


# Mount /metrics endpoint for Prometheus
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {"/metrics": make_wsgi_app()})


@app.route("/")
def index():
    return redirect(url_for("auth.authenticate"))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html", custom_css="css/styles_404.css"), 404


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=5080)

##Testing CI/CD Pipeline