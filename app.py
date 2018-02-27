from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f"<TODO: {todo}>"


@app.route('/')
def index():
    return "hello world"

@app.route('/todo', methods=["GET", "POST"])
def todo():
    if request.method == 'POST':
        _todo = request.form['todo']
        todo = Todo(todo=_todo)
        db.session.add(todo)
        db.session.commit()
    todos = Todo.query.all()
    return render_template('todo.html', todos=todos)
