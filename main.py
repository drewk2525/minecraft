#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Andrew Kroft
10/22/2014
DPWP - Section 01
Dynamic Site
'''
print "Content-Type: text/html\n"
#imports including from page.py and items.py
import webapp2
from page import Page, ContentPage
from items import ItemList

print "Testing"

class MainHandler(webapp2.RequestHandler):
    def get(self):
        i = ItemList()  #Set our item list object

        #Check if there was a Get request
        if self.request.GET:
            p = ContentPage() #if so, make our p variable a ContentPage object
            id = self.request.GET['id']  #Get the id of the item we're looking at
            p.recipe = i.recipe_display(id)  #use id to get recipe display and send to content page
            p.content = i.item_display(id)  #use id to get item display and send to content page
        else:
            p = Page()  #if there is no get request, make our p variable a Page object
            p.content = i.display()  #set our content to our item list display

        #Display whatever we have
        self.response.write(p.print_out())



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
