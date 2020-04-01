from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from . import db

bp = Blueprint("auth", __name__)


@bp.route('/register', methods=('GET','POST'))
def register():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        with db.get_db() as con:
            with con.cursor() as cur:

                cur.execute("""INSERT INTO users (username, password)
                    VALUES (%s, %s)""", (username, password))

        return redirect('/')

    return render_template('register.html')
