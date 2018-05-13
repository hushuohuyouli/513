from flask import Blueprint,render_template,url_for,request
from app.models import Movie
from app.extensions import db

movie = Blueprint('movie',__name__)

# 喜剧
@movie.route('/comedy/')
def comedy():
    data = Movie.query.filter(Movie.movie_type.like('%喜剧%'))
    # data = Movie_test.query.filter(Movie.movie_type.like('%喜剧%'))
    mylist = []
    for i in data:
        movie_id = i.id
        movie_name = i.movie_name
        img_small = i.movie_img.splitlines()[0]
        img_big = i.movie_img.splitlines()[1]
        movie_url = i.movie_url
        movie_type = i.movie_type
        mylist.append([movie_id,movie_name,img_small,img_big,movie_url,movie_type])
    return render_template('movie/comedy.html',mylist = mylist)
# 爱情

@movie.route('/love/')
def love():
    data = Movie.query.filter(Movie.movie_type.like('%爱情%'))
    mylist = []
    for i in data:
        movie_id = i.id
        movie_name = i.movie_name
        img_small = i.movie_img.splitlines()[0]
        img_big = i.movie_img.splitlines()[1]
        movie_url = i.movie_url
        movie_type = i.movie_type
        mylist.append([movie_id,movie_name,img_small,img_big,movie_url,movie_type])
    return render_template('movie/love.html',mylist = mylist)

@movie.route('/action/')
def action():
    data = Movie.query.filter(Movie.movie_type.like('%动作%'))
    mylist = []
    for i in data:
        movie_id = i.id
        movie_name = i.movie_name
        img_small = i.movie_img.splitlines()[0]
        img_big = i.movie_img.splitlines()[1]
        movie_url = i.movie_url
        movie_type = i.movie_type
        mylist.append([movie_id,movie_name,img_small,img_big,movie_url,movie_type])
    return render_template('movie/action.html',mylist = mylist)

@movie.route('/feature/')
def feature():
    data = Movie.query.filter(Movie.movie_type.like('%剧情%'))
    mylist = []
    for i in data:
        movie_id = i.id
        movie_name = i.movie_name
        img_small = i.movie_img.splitlines()[0]
        img_big = i.movie_img.splitlines()[1]
        movie_url = i.movie_url
        movie_type = i.movie_type
        mylist.append([movie_id,movie_name,img_small,img_big,movie_url,movie_type])
    return render_template('movie/feature.html',mylist = mylist)

@movie.route('/science/')
def science():
    data = Movie.query.filter(Movie.movie_type.like('%科幻%'))
    mylist = []
    for i in data:
        movie_id = i.id
        movie_name = i.movie_name
        img_small = i.movie_img.splitlines()[0]
        img_big = i.movie_img.splitlines()[1]
        movie_url = i.movie_url
        movie_type = i.movie_type
        mylist.append([movie_id,movie_name,img_small,img_big,movie_url,movie_type])
    return render_template('movie/science.html',mylist = mylist)

@movie.route('/horror/')
def horror():
    data = Movie.query.filter(Movie.movie_type.like('%恐怖%'))
    mylist = []
    for i in data:
        movie_id = i.id
        movie_name = i.movie_name
        img_small = i.movie_img.splitlines()[0]
        img_big = i.movie_img.splitlines()[1]
        movie_url = i.movie_url
        movie_type = i.movie_type
        mylist.append([movie_id,movie_name,img_small,img_big,movie_url,movie_type])
    return render_template('movie/horror.html',mylist = mylist)

@movie.route('/cartoon/')
def cartoon():
    data = Movie.query.filter(Movie.movie_type.like('%恐怖%'))
    mylist = []
    for i in data:
        movie_id = i.id
        movie_name = i.movie_name
        img_small = i.movie_img.splitlines()[0]
        img_big = i.movie_img.splitlines()[1]
        movie_url = i.movie_url
        movie_type = i.movie_type
        mylist.append([movie_id,movie_name,img_small,img_big,movie_url,movie_type])
    return render_template('movie/cartoon.html',mylist = mylist)

@movie.route('/thriller/')
def thriller():
    data = Movie.query.filter(Movie.movie_type.like('%惊悚%'))
    mylist = []
    for i in data:
        movie_id = i.id
        movie_name = i.movie_name
        img_small = i.movie_img.splitlines()[0]
        img_big = i.movie_img.splitlines()[1]
        movie_url = i.movie_url
        movie_type = i.movie_type
        mylist.append([movie_id,movie_name,img_small,img_big,movie_url,movie_type])
    return render_template('movie/thriller.html',mylist = mylist)

@movie.route('/movie_info/<int:movie_id>')
def movie_info(movie_id):
    data = Movie.query.filter(Movie.id == movie_id)
    mylist = []
    url_list = []
    for i in data:
        movie_id = i.id
        movie_name = i.movie_name
        img_small = i.movie_img.splitlines()[0]
        img_big = i.movie_img.splitlines()[1]
        movie_url = i.movie_url
        movie_type = i.movie_type
        for url in i.movie_url.splitlines():
            url_list.append(url)
        mylist.append([movie_id, movie_name, img_small, img_big,url_list, movie_type])
    return render_template('movie/movie_info.html',mylist=mylist)
