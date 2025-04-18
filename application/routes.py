from flask import render_template, url_for, request, redirect, session

from application import app
from datetime import datetime
from application.utilities import get_time_of_day
from application.fake_data import products, people
import os
# from application.forms.register_form import RegisterForm
from application.data_access import add_person, get_people


@app.route('/')
@app.route('/home')
def home():
    session['loggedIn'] = False
    now = datetime.now()
    time_slot = get_time_of_day(now.hour)
    return render_template('home.html', title='Home', time_slot=time_slot, is_morning=True)


@app.route('/welcome/<name>')
@app.route('/welcome')
def welcome(name="World"):
    return render_template('welcome2.html', name=name, group='Everyone')


@app.route('/product/<int:product_id>')
def products_by_id(product_id):
    if product_id + 1 > len(products):
        return render_template('products.html', products=products, title='All Products')

    time_slot = get_time_of_day(datetime.now().hour)
    if len(products) > product_id + 1:
        next_url = url_for('products_by_id', product_id=product_id + 1)
    else:
        next_url = False
    if product_id > 0:
        previous_url = url_for('products_by_id', product_id=product_id - 1)
    else:
        previous_url = False
    image_src = '../static/images/image_' + str(product_id) + '.jpg'

    # app.logger.debug(os.path.exists(os.path.join(app.static_folder, 'images/image_2.gif')))
    # app.logger.debug(os.path.exists(os.path.join(app.template_folder, 'index.html')))

    file_path = '../static/images/image_' + str(product_id) + '.gif'
    if os.path.exists((os.path.join(app.static_folder, 'images/image_' + str(product_id) + '.gif'))):
        image_gif = file_path
    else:
        image_gif = False

    title = products[product_id]['name']
    return render_template('product.html', product=products[product_id], time_slot=time_slot, next_url=next_url, previous_url=previous_url, image_src=image_src, image_gif=image_gif, title=title)


@app.route('/products')
def all_products():
    return render_template('products.html', products=products, title='All Products')


@app.route('/people')
def all_people():
    return render_template('people.html', people=people, title='All People')


@app.route('/peopledb')
def all_people_from_db():
    people_from_db = get_people()
    print(people_from_db)
    return render_template('people2.html', people=people_from_db, title='Database People')


@app.route('/register', methods=['GET', 'POST'])
def register():
    error = ""
    register_form = RegisterForm()

    if request.method == 'POST':
        first_name = register_form.first_name.data
        last_name = register_form.last_name.data

        if len(first_name) == 0 or len(last_name) == 0:
            error = 'Please supply both a first and last name'

        else:
            people.append({'Firstname': first_name, 'Lastname': last_name})
            add_person(first_name, last_name)
            return redirect(url_for('register'))

    return render_template('register.html', form=register_form, title='Add Person', message=error)


@app.route('/admin')
def admin():
    if 'username' in session:
        username = session['username']
        return render_template('adminarea.html', username=username, title='Admin Area')
    return render_template('adminarea.html', username=False, title='Admin Area')


@app.route('/adminpage1', methods=['GET', 'POST'])
def adminpage1():
    if 'username' in session:
        username = session['username']
        print('admin page 1')
        print(username)
        return render_template('page1.html', username=username, title='Admin Page 1')
    return render_template('adminarea.html', username=False, title='Admin Area')


@app.route('/adminpage2')
def adminpage2():
    if 'username' in session:
        username = session['username']
        return render_template('page2.html', username=username, title='Admin Page 2')
    return render_template('adminarea.html', username=False, title='Admin Area')


@app.route('/login', methods=['GET', 'POST'])
def login():
    # app.logger.debug("Start of login")
    if request.method == 'POST':
        session['username'] = request.form['username']
        # app.logger.debug("Username is: " + session['username'])
        session['loggedIn'] = True
        session['role'] = 'admin'
        return redirect(url_for('all_products'))
    return render_template('login.html', title="Login")


@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    session.pop('username', None)
    session.pop('role', None)
    session['loggedIn'] = False
    return redirect(url_for('all_products'))
