from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/diksha'

db = SQLAlchemy(app)

class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __repr__(self): #dander wrapper method (optional)
         return f'<Person {self.id}, {self.name}>' # ability to custimize a printable string

with app.app_context():
        db.create_all()

@app.route('/')
def index():
    person = Person.query.first()
    return 'Hello ' + person.name

app.run(debug=True)
# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)

# if(__name__) == '__main__':
#     app.run(host="0.0.0.0")