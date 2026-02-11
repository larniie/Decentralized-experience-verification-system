from ..db import db
from ..domain.identity import Identity

class IdentityService:
    def create_identity(self, data):
        if not data.get('id') or not data.get('name'):
            raise ValueError("ID and name are required")
        existing = Identity.query.filter_by(id=data['id']).first()
        if existing:
            raise ValueError("Identity with this ID already exists")
        identity = Identity(id=data['id'], name=data['name'])
        db.session.add(identity)
        db.session.commit()
        return identity

    def get_identity(self, id):
        return Identity.query.filter_by(id=id).first()

    def get_all_identities(self):
        return Identity.query.all()
