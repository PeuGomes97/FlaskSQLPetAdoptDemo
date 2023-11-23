from flask_sqlalchemy import SQLAlchemy

IMAGE = "https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif"

db = SQLAlchemy()


class Pet(db.Model):
    """Pet to adopt"""

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def image_url(self):
        """Image for the pet"""

        return self.photo_url or IMAGE
    

def connect_db(app):
    with app.app_context():
     db.app = app
     db.init_app(app)
     db.create_all()


