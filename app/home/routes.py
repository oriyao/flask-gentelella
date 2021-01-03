from app.home import blueprint
from flask import render_template,current_app
from flask_login import login_required


@blueprint.route('/index')
@login_required
def index():
    current_app.logger.info(current_app.config["TESTENV"])

    return render_template('index.html')


@blueprint.route('/<template>')
@login_required
def route_template(template):
    return render_template(template + '.html')
