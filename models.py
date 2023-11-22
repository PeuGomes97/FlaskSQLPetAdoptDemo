from flask_sqlalchemy import SQLAlchemy

IMAGE = "https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif"

db = SQLAlchemy()


class Pet(db.model):
    """Pet to adopt"""

    __talbename__ = "pets"

    id = db.column(db.Integer, primary_key=True)
    name= db.column(db.Text, nullable=False)
    species = db.column(db.Text, nullable=False)
    photo_url = db.column(db.Text)
    age = db.column(db.Integer)
    notes = db.column(db.Text)
    available = db.column(db.Boolean, nullable=False, default=True)

    def image_url(self):
        """Image for the pet"""

        return self.photo_url or IMAGE
    

def connect_db(app):
    db.app = app
    db.init_app(app)


