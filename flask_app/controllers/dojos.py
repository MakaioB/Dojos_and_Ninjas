from flask import Flask, render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo


@app.route('/dojos', methods=['GET', 'POST'])
def dojo_page():
    dojo = Dojo.get_all_dojos()
    if request.method == 'POST':
        data = {
            'name': request.form['dojo_name']
        }
        Dojo.save_dojo(data)
        return redirect('/dojos')
    else:
        return render_template('dojo_screen.html', dojos=dojo)



@app.route('/dojos/<int:dojo_id>')
def dispaly_dojo(dojo_id):
    data = {
        "id" : dojo_id 
    }
    dojo = Dojo.get_one_dojo_with_ninjas(data)
    print(dojo.ninjas)
    return render_template('dojos_ninjas.html', dojo= dojo )
