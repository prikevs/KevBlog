#coding:utf8

from .database import db
from datetime import datetime

articles_tags = db.Table(
    'articles_tags',
    db.Column('tagId', db.Integer, db.ForeignKey('tags.id')),
    db.Column('articleId', db.Integer, db.ForeignKey('articles.id'))   
)

class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    summary = db.Column(db.String(300))
    content = db.Column(db.Text)
    pubTime = db.Column(db.DateTime, default=datetime.now())
    isPub = db.Column(db.Boolean, default=True)
    tags = db.relationship('Tag',
                           secondary=articles_tags,
                           backref=db.backref('articles', lazy='dynamic'))

    def __init__(self, title, summary, content, pubTime=None, isPub=True):
        self.title = title
        self.summary = summary
        self.content = content
        if pubTime:
            self.pubTime = pubTime
        self.isPub = isPub

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __unicode__(self):
        return unicode(self.title)


class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)

    def __init__(self, name):
        self.name = name.lower()

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __unicode__(self):
        return unicode(self.name)


def _get_tag(name):
    name = name.lower()
    tag = db.session.query(Tag).filter(Tag.name==name).first()
    if not tag:
        tag = Tag(name)
        tag.save()
    return tag

def create_article(title, summary, content, pubTime=None, isPub=True, tagnames=[]):
    article = Article(title, summary, content, pubTime, isPub)
    for tagname in tagnames:
        tag = _get_tag(tagname.lower())
        article.tags.append(tag)
    article.save()
    return article
