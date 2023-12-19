import datetime

class Note:
    def __init__(self, id, title, body):
        self.id = id
        self.title = title
        self.body = body
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def update(self, title, body):
        self.title = title
        self.body = body
        self.updated_at = datetime.datetime.now()
