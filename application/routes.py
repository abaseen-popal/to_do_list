from application import app, db
from application.models import Todo

@app.route("/", methods=['GET','POST'])
@app.route("/home", methods=['GET','POST'])
def home():
    all_tasks = Todo.query.all()
    output = ""
    for task in all_tasks:
        output += task.description + "Completed?"+ str(Todo.completed)+"<br>"
    return output

@app.route("/create")
def create():
    new_todo = Todo(description = "new task")
    db.session.add(new_todo)
    db.session.commit()
    return "New task added"

@app.route("/complete/<int:id>")
def complete(id):
    task = Todo.query.filter_by(id=id).first()
    task.completed = True
    db.session.commit()
    return "Task is now complete"

@app.route("/incomplete/<int:id>")
def incomplete(id):
    task = Todo.query.filter_by(id=id).first()
    task.completed = False
    db.session.commit()
    return "Task is now complete"

@app.route("/update/<new_description>")
def update(new_description):
    task = Todo.query.order_by(Todo.id.desc()).first()
    task.description = new_description
    db.session.commit()
    return "Most recent task was updated with the description: " + new_description


@app.route("/delete/<int:id>")
def delete(id):
    task = Todo.query.filter_by(id=id).first()
    db.session.delete(task)
    db.session.commit()
    return "task was deleted: " + id



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