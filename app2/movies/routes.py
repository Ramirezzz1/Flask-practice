# import app2
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app2.forms import newActorForm
movies = Blueprint('movies', __name__, template_folder = 'movies_templates')

@movies.route('/actoroftheday')
def actoroftheday():
    movie_of_the_day= 'Fast and Furious: FAST FIVE'
    actor_of_the_day= ['Vin Disel','Dwayne The Rock Johnson', 'Paul Walker']
    return render_template('actoroftheday.html', actor=actor_of_the_day, movie=movie_of_the_day)

@movies.route('/addactor', methods=['GET','POST'])
def addactor():
    form = newActorForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            actor_dict= {
                'name': form.name.data,
                'age': form.age.data,
                'nationality': form.nationality.data,
                'hiringprice': form.hiringprice.data,
                'bestperfomance': form.best_film.data
            }
            flash('from validated', category='alert-info')
            flash(f'{actor_dict}', category='alert-info')
        else:
            flash('form did not validate', category = 'alert-danger') 
        return redirect(url_for('movies.addactor'))
    return render_template('addactor.html', form=newActorForm())


# @app2.route('/register')
# def register():
#     form = RegistrationForm()
#     return render_template('register.html', title= 'Register', form=form)

# @app2.route('/login')
# def register():
#     form = LoginForm()
#     return render_template('login.html', title= 'login', form=form)