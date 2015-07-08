#coding:utf8
from datetime import datetime
from flask import render_template, request, abort
from . import app
from .models import (Article, Tag, create_article)
from .utils import *


@app.errorhandler(404)
def page_not_found(error):
    title = unicode(error)
    message = error.description
    return render_template('errors.html',
                            title=title,
                            message=message)

@app.errorhandler(500)
def page_not_found(error):
    title = unicode(error)
    message = error.description
    return render_template('errors.html',
                            title=title,
                            message=message)

@app.route('/')
def index():
    try:
        page = int(request.args.get('page', '')) 
    except ValueError:
        page = 1
    pagination = Article.query.order_by(Article.id.desc()).paginate(page,per_page=10)
    return render_template('index.html',
                           pagination=pagination)

@app.route('/article/<int:id>')
def show_article(id):
    print("xx")
    article = Article.query.get_or_404(id)
    return render_template('page.html',
                            title=article.title,
                            content=article.content,
                            pubTime=article.pubTime,
                            tags=article.tags)

@app.route('/tags')
def show_tags():
    tags = Tag.query.all()
    return render_template('tags.html',
                           tags=tags)

@app.route('/tag/<int:id>')
def show_tag(id):
    tag = Tag.query.get_or_404(id)
    articles = tag.articles.all()
    return render_template('tag.html',
                           tag=tag,
                           entries=articles)

@app.route('/about')
def about():
    content = load_content('about')
    return render_template('page.html',
                            title='About',
                            content=content)

@app.route('/links')
def links():
    content = load_content('links')
    return render_template('page.html',
                           title="Links",
                           content=content)
