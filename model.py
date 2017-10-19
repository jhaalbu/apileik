# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 17:37:21 2017

@author: JanHelge
"""

from wtforms import Form, IntegerField, StringField, validators

class InputForm(Form):
    veg = StringField(label='Veg (f.eks fv60)', validators=[validators.InputRequired()])
    fylke = IntegerField(label='Fylke (f.eks 14)', validators=[validators.InputRequired()])

