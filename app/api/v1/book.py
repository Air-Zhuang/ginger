from flask import jsonify

from sqlalchemy import or_

from app.libs.redprint import Redprint
from app.models.book import Book
from app.validators.forms import BookSearchForm
from app.models.base import db
api=Redprint('book')

@api.route('/search')
def search():
    '''
    url http://localhost:5000/v1/book/search?q={}
    '''
    form=BookSearchForm().validate_for_api()
    q='%'+form.q.data+'%'                                   #模糊搜索前后要加%
    books=Book.query.filter(
        or_(Book.title.like(q),Book.publisher.like(q))).all()
    books=[book.hide('summary') for book in books]
    resp={"result":books,"flag": 1}         #返回值拼接成json格式
    return jsonify(resp)

@api.route('/<isbn>/detail')
def detail(isbn):
    '''
    url http://localhost:5000/v1/book/9787111128069/detail
    '''
    book=Book.query.filter_by(isbn=isbn).first_or_404()
    return jsonify(book)

@api.route('/select')       #测试：通过原生sql语句获取查询结果
def select():
    from sqlalchemy import text
    sql = text("SELECT title FROM book")
    result = db.engine.execute(sql)
    for row in result:
        print(row)
        print(row[0])
    return "Hello World"