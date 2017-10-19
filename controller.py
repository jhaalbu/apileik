# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 17:36:53 2017

@author: JanHelge
"""

from model import InputForm
from flask import Flask, render_template, request
from compute import hentSkred
import sys

app = Flask(__name__)

@app.route('/skred', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        chart = hentSkred(form.veg.data, form.fylke.data)
        chart = chart.render_data_uri()
    else:
        chart = None

    return render_template('chart1.html', form=form, chart=chart)

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/charts/')
def line_route():
   chart = hentSkred('fv60', 14)
   chart = chart.render_data_uri()

   return render_template( 'charts.html', chart = chart)

if __name__ == '__main__':
    app.run(debug=True)