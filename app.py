from flask import render_template
from controllers.user_controller import user_bp
from controllers.item_controller import item_bp
from controllers.login_controller import login_bp
from controllers.dashboard_controller import dashboard_bp

from database import app

@app.route('/')
def home():
    return render_template('login.html')

app.register_blueprint(login_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(user_bp)
app.register_blueprint(item_bp)

if __name__ == '__main__' :
    app.run(debug=True)