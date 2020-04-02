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
        user_exists = None

        with db.get_db() as con:
            with con.cursor() as cur:
                cur.execute("""SELECT username FROM users
                    WHERE username = %s""", (username,))
                user_exists = cur.fetchone()

        if not username:

            flash('Username is required')

        elif not password:

            flash('Password is required')

        elif user_exists is not None:

            flash(f'{username} is already registered')

        else:
            with db.get_db() as con:
                with con.cursor() as cur:

                    cur.execute("""INSERT INTO users (username, password)
                        VALUES (%s, %s)""", (username, password))

            return redirect('/')

    return render_template('register.html')
