#!/usr/bin/python3
"""
resume information definition
"""
from models.engine.db_storage import db


class Resume_info(db.Model):
    """defines the resume information class"""
    __tablename__ = 'resume_info'
    id = db.Model.Column(db.Integer, primary_key=True)
    user_id = db.Model.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    template_id = db.Model.Column(db.Integer, db.ForeignKey('template.id'), nullable=False)
    content = db.Model.Column(db.JSON, nullable=False)
    created_at = db.Model.Column(db.DateTime, default=db.func.current_timestamp())

    """Relationships to resume information table"""
    user = db.relationship('User', back_populates='resume_infos')
    template = db.relationship('Template', back_populates='resume_infos')
