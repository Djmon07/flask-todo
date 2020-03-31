from flask import Blueprint, render_template, request, redirect

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


@bp.route("/add", methods=["POST"])
def new_task():
    task = request.form['task']
    with db.get_db() as con:
        with con.cursor() as cur:
            cur.execute("""INSERT INTO todos (description, completed, created_at)
            VALUES (%s, %s, NOW())""",
                (task, False))

    return redirect("/")
