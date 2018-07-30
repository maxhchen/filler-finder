#run: dev_appserver.py app.yaml
#Go to console.google.com
import webapp2
import jinja2
import os
import logging
import time

from google.appengine.api import users #to login through g-acc.
from google.appengine.ext import ndb
from google.appengine.api import images

# jinja2 Environment
env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class User(ndb.Model):
    name = ndb.StringProperty()
    email = ndb.StringProperty()

class Comment(ndb.Model):
    message = ndb.StringProperty()
    user_key = ndb.KeyProperty() #store the user key to point to who posted it
    filler_key = ndb.KeyProperty() #store the filler key in which the comment is in

class Filler(ndb.Model):
    name = ndb.StringProperty()
    type = ndb.StringProperty()
    location = ndb.StringProperty()
    picture = ndb.BlobProperty()
    description = ndb.StringProperty()
    company = ndb.DateProperty()

######################################################################

class HomePage(webapp2.RequestHandler):
    def get(self):

        template = env.get_template("templates/home.html")
        self.response.write(template.render())

class Description(webapp2.RequestHandler):
    def get(self):
        # get and display correct filler from urlsafe_key
        urlsafe_key = self.request.get("key")
        key = ndb.Key(urlsafe = urlsafe_key)
        filler = key.get()

        templateVars = {
        "filler" : filler,
        }

        template = env.get_template("templates/description.html")
        self.response.write(template.render(templateVars))

class Search(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/search.html")
        self.response.write(template.render())

class AddFiller(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/addFiller.html")
        self.response.write(template.render())

    def post(self):
        template = env.get_template("templates/addFiller.html")
        templateVars = {
            "name" : self.request.get('name'),
            "location" : self.request.get('location'),
            "fountain" : self.request.get('fountain'),
            "description" : self.request.get('description'),
            "company" : self.request.get('company'),
        }
        self.response.write(template.render(templateVars))
        #### self.response.write(self.request.POST) 


app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/description', Description),
    ('/search', Search),
    ('/add', AddFiller),
], debug = True)
