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
    article = Article.query.get_or_404(id)
    return render_template('page.html',
                            title=article.title,
                            content=markdown2html(article.content),
                            pubTime=article.pubTime,
                            tags=article.tags)

@app.route('/tags')
def show_tags():
    tags = Tag.query.all()
    return render_template('tags.html',
                           tags=tags)

@app.route('/tag/<int:id>')
def show_tag(id):
    try:
        page = int(request.args.get('page', '')) 
    except ValueError:
        page = 1
    tag = Tag.query.get_or_404(id)
    pagination = tag.articles.paginate(page, per_page=10)
    return render_template('tag.html',
                           tag=tag,
                           pagination=pagination)

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

@app.route('/publish', methods=['GET', 'POST'])
def publish():
    if request.method == 'GET':
        abort(404)
    token = request.form.get('token', '')
    if token != app.config['TOKEN']:
        return 'invalid access token', 500

    title = request.form.get('title', None)
    if not title:
        return 'no title found', 500

    summary = request.form.get('summary', None)
    if not summary:
        return 'no summary found', 500

    content = request.form.get('content', None)
    if not content:
        return 'no content found', 500

    pubTime = request.form.get('pubTime', None)
    if pubTime:
        pubTime = datetime.strptime(pubTime, app.config['TIME_FORMAT'])

    isPub = request.form.get('isPub', True)
    if isPub != True:
        isPub = False

    tags = request.form.getlist('tags')

    create_article(title, summary, content, pubTime, isPub, tags)
    return '', 200

