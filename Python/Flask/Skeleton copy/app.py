from flask import Flask,jsonify, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
# configuro la base de datos, con el nombre el usuario y la clave
# app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost/test'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost/test'
# URI de la BBDD                          driver de la BD  user:clave@URLBBDD/nombreBBDD
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #none
db= SQLAlchemy(app)   #crea el objeto db de la clase SQLAlquemy
ma=Marshmallow(app)   #crea el objeto ma de de la clase Marshmallow

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    def __init__(self,content):
        self.content = content

with app.app_context():
    db.create_all()  # aqui crea todas las tablas
#  ************************************************************
class TaskSchema(ma.Schema):
    class Meta:
        fields=('id','content')

@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        content = request.form['content']
        new_task = Task(content=content)
        db.session.add(new_task)
        db.session.commit()
        return redirect('/')
    return render_template('add_task.html')

@app.route('/get_tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    task_list = [{'id': task.id, 'content': task.content} for task in tasks]
    return jsonify(task_list)

@app.route('/delete_task/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Tarea eliminada con éxito'})

if __name__ == '__main__':
    app.run(debug=True)
