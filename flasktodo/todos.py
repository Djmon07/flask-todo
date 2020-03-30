from flask import Blueprint, render_template, request

from . import db


bp = Blueprint("todos", __name__)

@bp.route("/", methods=('GET', 'POST'))
def index():
    """View for home page which shows list of to-do items."""

    cur = db.get_db().cursor()

    if request.method == 'POST':
        filter = request.form['filter']

        if filter == 'all':

            cur.execute('SELECT * FROM todos')
            todos = cur.fetchall()
            cur.close()
            return render_template("index.html", todos=todos)

        elif filter == 'completed':

            cur.execute('SELECT * FROM todos WHERE completed=True')
            todos = cur.fetchall()
            cur.close()
            return render_template("index.html", todos=todos)

        elif filter == 'uncompleted':

            cur.execute('SELECT * FROM todos WHERE completed=False')
            todos = cur.fetchall()
            cur.close()
            return render_template("index.html", todos=todos)

    cur.execute('SELECT * FROM todos')
    todos = cur.fetchall()
    cur.close()

    return render_template("index.html", todos=todos)
