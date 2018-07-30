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
        template = env.get_template("templates/clicky.html")
        self.response.write(template.render(templateVars))
        #read request

        #redirect to DB

        #render response

    # def post(self):

class Description(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/description.html")
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', Home),
], debug = True)
