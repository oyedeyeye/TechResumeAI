#!/usr/bin/python3
"""
User information
"""
from models.engine.db_storage import db


class User(db.Model):
    """User class"""
    __table__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    github_id = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    avatar_url = db.Column(db.String(128))
    access_token = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    """Add relationship with Resume_info"""
    resume_infos = db.relationship('Resume_info', back_populates='user')
