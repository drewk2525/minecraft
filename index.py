#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Andrew Kroft
10/22/2014
DPWP - Section 01
Dynamic Site
'''
#import cgitb
#cgitb.enable()
#print "Content-Type: text/html\n"
from flask import Flask, render_template, request
from flask.ext.session import Session
import jinja2
from page import Page, ContentPage
from items import ItemList

app = Flask(__name__)


app.debug = True

@app.route("/", methods=['GET'])
def get():

  i = ItemList()
  if request.args.get('id') != None:
    p = ContentPage()
    id = request.args.get('id')
    p.recipe = i.recipe_display(id)
    p.content = i.item_display(id)
  else:
    p = Page()
    p.recipe = ''
    p.content = i.display()
  
  return render_template('home.html', content = p.content, recipe = p.recipe)
