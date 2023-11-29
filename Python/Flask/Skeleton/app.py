# Importación de módulos necesarios
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
from flask_cors import CORS       # del modulo flask_cors importar CORS
from flask_marshmallow import Marshmallow
from sqlalchemy.exc import IntegrityError
import datetime

#Creacion de APP Flask
app = Flask(__name__)
CORS(app) #modulo cors es para que me permita acceder desde el frontend al backend

# configuro la base de datos, con el nombre el usuario y la clave
# app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://user:password@localhost/test'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@localhost/proyecto'
# URI de la BBDD                          driver de la BD  user:clave@URLBBDD/nombreBBDD
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #none
db= SQLAlchemy(app)   #crea el objeto db de la clase SQLAlquemy
ma=Marshmallow(app)   #crea el objeto ma de de la clase Marshmallow

#Definimo el modelo de datos
class Empleado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    apellido= db.Column(db.String(100))
    dni= db.Column(db.String(16))
    num_empleado= db.Column(db.String(20))
    correo= db.Column(db.String(30))
    cargo= db.Column(db.String(10))
    fecha_nacimiento= db.Column(db.Date)
    
    def __init__(self,nombre,apellido,dni,num_empleado,correo,cargo,fecha_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.num_empleado = num_empleado
        self.correo = correo
        self.cargo = cargo
        self.fecha_nacimiento = fecha_nacimiento

#Definimos el esquema
class EmpleadoSchema(ma.Schema):
    class Meta:
        fields = ('id','nombre','apellido','dni','num_empleado','correo','cargo','fecha_nacimiento')


#Crear esquemas para la db
empleado_schema = EmpleadoSchema() #trae un empleado
empleados_schema = EmpleadoSchema(many=True) #Para traer más de un empleado

#Creamos la tablas
with app.app_context():
    db.create_all()

#Endpoint Get
@app.route('/empleados', methods=['GET'])
def get_all_empleados():
    try:
        empleados = Empleado.query.all()
        if empleados:
            return empleados_schema.jsonify(empleados)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

#Endpoint Get by Id
@app.route('/empleados/<id>', methods=['GET'])
def get_empleado(id):
    try:
        empleado = Empleado.query.get(id)

        if empleado:
            return empleado_schema.jsonify(empleado)
        else:
            return jsonify({'error': 'Empleado no encontrado'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Ruta para crear un nuevo empleado mediante una solicitud POST
@app.route('/empleados', methods=['POST'])
def create_empleado():
    try:
        json_data = request.get_json()
        nombre = json_data['nombre']
        apellido = json_data['apellido']
        dni = json_data['dni']
        num_empleado = json_data['num_empleado']
        correo = json_data['correo']
        cargo = json_data['cargo']
        fecha_nacimiento = datetime.datetime.strptime(json_data['fecha_nacimiento'], "%Y-%m-%d").date()

        # Cargar datos JSON en un objeto Empleado
        nuevo_empleado = Empleado(nombre, apellido, dni, num_empleado, correo, cargo, fecha_nacimiento)

        # Realizar validaciones adicionales si es necesario

        db.session.add(nuevo_empleado)
        db.session.commit()

        return empleado_schema.jsonify(nuevo_empleado), 201  # Devolver el empleado creado con el código 201 (creado)
    except ValidationError as err:
        return jsonify({'error': err.messages}), 400  # Devolver mensajes de error de validación con el código 400 (error de solicitud)

# Ruta para actualizar un empleado mediante una solicitud PUT
@app.route('/empleados/<id>', methods=['PUT'])
def update_empleado(id):
    try:
        empleado = Empleado.query.get(id)

        # Verificar si el empleado existe en la base de datos
        if empleado:
            json_data = request.get_json()
            empleado.nombre = json_data.get('nombre', empleado.nombre)
            empleado.apellido = json_data.get('apellido', empleado.apellido)
            empleado.dni = json_data.get('dni', empleado.dni)
            empleado.num_empleado = json_data.get('num_empleado', empleado.num_empleado)
            empleado.correo = json_data.get('correo', empleado.correo)
            empleado.cargo = json_data.get('cargo', empleado.cargo)
            empleado.fecha_nacimiento = datetime.datetime.strptime(json_data['fecha_nacimiento'], "%Y-%m-%d").date()

            # Realizar validaciones según tus requerimientos

            db.session.commit()
            return empleado_schema.jsonify(empleado)
        else:
            return jsonify({'error': 'Empleado no encontrado'}), 404  # Devolver código 404 si el empleado no existe

    except ValidationError as err:
        return jsonify({'error': err.messages}), 400  # Devolver mensajes de error de validación con el código 400 (error de solicitud)

# Ruta para eliminar un empleado mediante una solicitud DELETE
@app.route('/empleados/<id>', methods=['DELETE'])
def delete_empleado(id):
    try:
        empleado = Empleado.query.get(id)

        # Verificar si el empleado existe en la base de datos
        if empleado:
            db.session.delete(empleado)
            db.session.commit()
            return empleado_schema.jsonify(empleado)
        else:
            return jsonify({'error': 'Empleado no encontrado'}), 404  # Devolver código 404 si el empleado no existe

    except Exception as e:
        return jsonify({'error': str(e)}), 500  # Devolver código 500 si hay un error durante la eliminación


if __name__ == '__main__':
    app.run(debug=True)

