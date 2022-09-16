from flask import Flask, render_template, redirect, request
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas', methods=['GET', 'POST'])
def add_ninja():
    dojo = Dojo.get_all_dojos()
    if request.method == 'POST':
        data = {
            'dojo_id': request.form['dojo_select'],
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'age': request.form['age'],
        }
        Ninja.save_ninja(data)
        return redirect('/dojos')
    else:
        return render_template('create_ninja.html', dojos = dojo)