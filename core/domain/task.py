from ..config.extension import db
from collections import OrderedDict

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    is_completed = db.Column(db.Boolean, default=False)

    def __init__(self, title, description=None, is_completed=False):
        self.title = title
        self.description = description
        self.is_completed = is_completed

    def mark_complete(self):
        self.is_completed = True

    def mark_incomplete(self):
        self.is_completed = False

    def __repr__(self):
        return f'<Task {self.title}>'

    def to_dict(self):
        return OrderedDict([
            ('id', self.id),
            ('title', self.title),
            ('description', self.description),
            ('is_completed', self.is_completed)
        ])