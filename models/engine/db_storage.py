#!/usr/bin/python3
"""
Contains the database storage for the TechResumeAI
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session, sessionmaker
from os import getenv


db = SQLAlchemy()


class DBStorage:
    """
    Defines the storage class of the TechResumeAI
    """
    __session = None
    __engine = None

    def __init__(self, app=None):
        """Instatiates the DBStorage object"""
        if app is not None:
            self.setup_db(app)

    def setup_db(self, app):
        """DB connection configuration"""
        TRAI_MYSQL_USER = getenv('TRAI_MYSQL_USER')
        TRAI_MYSQL_PWD = getenv('TRAI_MYSQL_PWD')
        TRAI_MYSQL_HOST = getenv('TRAI_MYSQL_HOST')
        TRAI_MYSQL_DB = getenv('TRAI_MYSQL_DB')
        trai_url = 'mysql+pymysql://{}:{}@{}/{}'.format(
                                                    TRAI_MYSQL_USER,
                                                    TRAI_MYSQL_PWD,
                                                    TRAI_MYSQL_HOST,
                                                    TRAI_MYSQL_DB)

        app.config['SQLALCHEMY_DATABASE_URI'] = trai_url
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(app)

        with app.app_context():
            if not db.engine.table_names():
                db.create_all()
            self.__engine = db.get_engine()
            self.__session = db.session()  # instead of scoped_session()

    def all(self, cls=None):
        """Query all records in the database"""
        objs = []
        if cls:
            objs = self.__session.query(cls).all()
        else:
            classes = [User, Resume_info, Template]
            for cls in classes:
                objs += self.__session.query(cls).all()
        return objs

    # additional methods for managing database records
    def new(self, obj):
        """Add new object into the current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session"""
        if obj:
            self.__session.delete(obj)
            self.save()

    def get(self, cls, id):
        """Retrieve one object based on the class name and its ID"""
        if cls:
            return self.__session.query(cls).get(id)
        return None

    def reload(self):
        """Reload (create all tables in the database)"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def count(self, cls=None):
        """Get the count of all objects in storage or specific objects"""
        if cls:
            return len(self.all(cls))
        else:
            return len(self.all())

    def close(self):
        """Close the session"""
        self.__session.close()
