from application import app, db
from application.models import Tasks
from flask import render_template, request,redirect, url_for
from application.forms import TaskForm

@app.route("/")
@app.route("/home")
def home():
    all_tasks = Tasks.query.all()
    output = ""
    return render_template("index.html", title="Home", all_tasks=all_tasks)

@app.route("/create", methods=["GET","POST"])
def create():
    form = TaskForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_task = Tasks(description=form.description.data, completed = False) 
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for("home"))

    return render_template("add.html", title="Create a Task",form=form)


@app.route("/update/<int:id>", methods= ["GET","POST"])
def update(id):
    form = TaskForm()
    task = Tasks.query.filter_by(id=id).first()
    if request.method == "POST":
        task.description = form.description.data
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("update.html", form=form, title="Update Task", task=task)


@app.route("/delete/<int:id>", methods=["GET","POST"])
def delete(id):
    task = Tasks.query.filter_by(id=id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/complete/<int:id>", methods=["GET","POST"])
def complete(id):
    task = Tasks.query.filter_by(id=id).first()
    task.completed = True
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/incomplete/<int:id>", methods=["GET","POST"])
def incomplete(id):
    task = Tasks.query.filter_by(id=id).first()
    task.completed = False
    db.session.commit()
    return redirect(url_for("home"))



# @app.route('/add/<newtask>/<newdescription>')
# def add(newtask,newdescription):
#     if newdescription == "":
#         newdescription = "No description was added"
#         new_task = Todo(task= newtask, description= newdescription)
#         db.session.add(new_task)
#         db.session.commit()
#     else:
#         new_task = Todo(task= newtask, description= newdescription)
#         db.session.add(new_task)
#         db.session.commit()

#     return "Added new task  to database"


# @app.route('/view')
# def read():
#     all_tasks = Todo.query.all()
#     task_string = ""
#     for new_task in all_tasks:
#         task_string += "<br>"+ new_task.task + ":" + new_task.description
#     return task_string

# @app.route('/update/<name>')
# def update(name):
#     first_game = Todo.query.first()
#     first_game.name = name
#     db.session.commit()
#     return first_game.name