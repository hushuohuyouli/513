from flask import Blueprint,render_template,url_for,request,render_template_string
from app.models import Movie
from app.extensions import db
from app.forms import SearchForm

main = Blueprint('main',__name__)


@main.route('/index/')
def index():

    return render_template('main/index.html')

@main.route('/search/',methods = ['get','post'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        input_info = form.content.data

        data = Movie.query.filter(Movie.movie_name.like('%{}%'.format(input_info)))
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
            mylist.append([movie_id, movie_name, img_small, img_big, url_list, movie_type])
        return render_template('main/search_result.html', mylist=mylist)

    return render_template('main/search.html',form = form)
