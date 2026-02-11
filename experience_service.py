from ..db import db
from ..domain.experience import Experience

class ExperienceService:
    def create_experience(self, data):
        if not data.get('id') or not data.get('title') or not data.get('description'):
            raise ValueError("ID, title and description are required")
        existing = Experience.query.filter_by(id=data['id']).first()
        if existing:
            raise ValueError("Experience with this ID already exists")
        experience = Experience(id=data['id'], title=data['title'], description=data['description'])
        db.session.add(experience)
        db.session.commit()
        return experience

    def get_experience(self, id):
        return Experience.query.filter_by(id=id).first()
