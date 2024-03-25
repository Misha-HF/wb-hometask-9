from mongoengine import Document, StringField, ListField

class Quote(Document):
    quote = StringField()
    author = StringField()
    tags = ListField(StringField())


class Author(Document):
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()