
#run: dev_appserver.py app.yaml
#Go to console.google.com

import webapp2
import jinja2
import os
import logging
import time

from google.appengine.api import users #to login through g-acc.
from google.appengine.ext import ndb


env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        #read request

        #redirect to DB

        #render response

    # def post(self):


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug = True)
