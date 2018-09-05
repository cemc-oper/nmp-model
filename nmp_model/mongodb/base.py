"""
Base class of all objects using in nwpc_takler

{
    id: id,
    owner: owner,
    repo: repo,
    timestamp: datetime
}
"""
import datetime

from mongoengine import Document, \
    StringField, DateTimeField, GenericEmbeddedDocumentField, IntField, EmbeddedDocument


class Base(Document):
    id = IntField(default=None)
    owner = StringField(default=None)
    repo = StringField(default=None)
    timestamp = DateTimeField(required=True, default=datetime.datetime.utcnow)
    data = GenericEmbeddedDocumentField(default=None)

    meta = {
        'allow_inheritance': True
    }

    def is_valid(self):
        if self.id is None:
            return False
        if self.owner is None:
            return False
        if self.repo is None:
            return False
        return True

    def set_data(self, data):
        self.data = data
        return True

    def to_dict(self):
        if not self.is_valid():
            return None

        data_dict = self.data
        if isinstance(data_dict, EmbeddedDocument):
            data_dict = data_dict.to_dict()

        result = {
            'id': self.id,
            'owner': self.owner,
            'repo': self.repo,
            'timestamp': self.timestamp,
            'data': data_dict
        }
        return result
