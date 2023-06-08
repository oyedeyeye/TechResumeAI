#!/usr/bin/python3
"""
Resume Template definition
"""
from models.engine.db_storage import db


class Template(db.Model):
    __tablename__ = 'template'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    layout = db.Column(db.String(128), nullable=False)

    """Relationships definition template table"""
    resume_infos = db.relationship('Resume_info', back_populates='template')
