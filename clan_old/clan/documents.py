"""Documents views."""

from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort
from sqlalchemy import inspect

from . import db
from .models import Document, User
from clan.auth import login_required


bp = Blueprint('documents', __name__)


@bp.route('/')
def index():
    """Get page with all posts."""
    query = Document.query.order_by(Document.created).all()
    documents = [
        {
            'id': doc.doc_id,
            'title': doc.title,
            'body': doc.body,
            'user_id': doc.author_id,
            'created': doc.created,
            'username': User.query.get(doc.author_id).name
        }
        for doc in query
    ]
    return render_template('documents/index.html', documents=documents)


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    """View to create new document."""
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            flash("Title is required.")
        else:
            document = Document(title=title, body=body, author_id=g.user.user_id)
            db.session.add(document)
            db.session.commit()
            return redirect(url_for('documents.index'))

    return render_template('documents/create.html')


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(doc_id: int):
    """Update document."""
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            flash("Title is required.")
        else:
            document = Document.query.get(doc_id)
            if document is None:
                abort(404, f"Document id {document_id} does not exist.")
            if document.author_id != g.user.user_id:
                abort(403)

            document.title = title
            documennt.body = body
            db.session.commit()
            return redirect(url_for('documents.index'))

    return render_template('documents/update.html', post=post)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(doc_id: int):
    """Delete post."""
    document = Document.query.get(doc_id)
    if document is None:
        abort(404, f"Document id {document_id} does not exist.")
    if document.author_id != g.user.user_id:
        abort(403)

    db.session.delete(doc_id)
    db.session.commit()
    return redirect(url_for('documents.index'))
