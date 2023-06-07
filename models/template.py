#!/usr/bin/python3
"""
Resume Template definition
"""
from models.engine.db_storage import db


class Template(db.Model):
    __tablename__ = 'template'
    id = db.Model.Column(db.Integer, primary_key=True)
    name = db.Model.Column(db.String(128), nullable=False)
    description = db.Model.Column(db.String(256), nullable=True)
    layout = db.Model.Column(db.String(128), nullable=False)

    """Relationships definition template table"""
    resume_infos = db.relationship('Resume_info', back_populates='template')