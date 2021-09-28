from flask import Blueprint, render_template

movies = Blueprint('movies', __name__, template_folder = 'movies_templates')

@movies.route('/actoroftheday')
def actoroftheday():
    movie_of_the_day= 'Fast and Furious: FAST FIVE'
    actor_of_the_day= ['Vin Disel','Dwayne The Rock Johnson', 'Paul Walker']
    return render_template('actoroftheday.html', actor=actor_of_the_day, movie=movie_of_the_day)