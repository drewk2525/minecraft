#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Andrew Kroft
10/22/2014
DPWP - Section 01
Dynamic Site
'''
#print "Content-Type: text/html\n"

#Main page class, will send back information for the home page
class Page(object):
    def __init__(self):
        #add variable for page content, to be pulled from our item list
        self._content = ''

    #Getter and setter for self.__content
    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, temp):
        self._content = temp

    def print_out(self):
        return self._head + self._body + self._content + self._footer



#This is the page to show the content based on what the user clicked on
class ContentPage(Page):
    def __init__(self):
        Page.__init__(self)
        self._body = """
        <h1>Drew's Crafting Guide</h1>
        """
        self._content = ''
        self._recipe = ''

    #method for sending our content back to be displayed
    def print_out(self):
        self._content += "<a href='/'><button class='home'>Return Home</button></a>"
        return self._head + self._body + self._recipe + self._content + self._footer

    #Getter and setter for self._content
    @property
    def content(self):
        return self._content
    @content.setter
    def content(self, temp):
        self._content = temp


    #Getter and setter for self._recipe
    @property
    def recipe(self):
        return self._recipe
    @recipe.setter
    def recipe(self, temp):
        self._recipe = temp
