from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app
from flask_login import current_user, login_required
from app import db
from app.admin import bp


@bp.route('/admin', methods=['GET', 'POST'])
def admin():
    return render_template('admin.html', title='Admin')