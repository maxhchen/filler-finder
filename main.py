#run: dev_appserver.py app.yaml
#Go to console.google.com

import webapp2
import jinja2
import os
import logging
import time

from google.appengine.api import users #to login through g-acc.
from google.appengine.ext import ndb

class Person(ndb.Model):
    name = ndb.StringProperty()
    biography = ndb.StringProperty()
    birthday = ndb.DateProperty() #without time to have only the date.
    email = ndb.StringProperty()

env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        #read request
        current_user = users.get_current_user()

        #redirect to DB
        people = Person.query().fetch()
        if current_user:
                current_email = current_user.email()
                current_person = Person.query().filter(Person.email == current_email).get()
        else:
                current_person = None

        #render response
        logout_url = users.create_logout_url('/')
        login_url = users.create_login_url('/')


        templateVars = {
            'people' : people,
            'current_user': current_user,
            'logout_url': logout_url,
            'login_url': login_url
        }

        template = env.get_template('templates/home.html')
        self.response.write(template.render(templateVars))

    # def post(self):

class ProfilePage(webapp2.RequestHandler):
    def get(self):
        #Get info from request
        urlsafe_key = self.request.get('key')
        #Read or quite from DB
        key = ndb.Key(urlsafe=urlsafe_key) #turning urlsafe into key object

        person = key.get() #turing key object to person

        #Render a response
        templateVars = {
            'person' : person
        }

        template = env.get_template('templates/profile.html')
        self.response.write(template.render(templateVars))

class CreateHandler(webapp2.RequestHandler):
    def post(self):
        #Get info from request
        name = self.request.get('name')
        biography = self.request.get('biography')
        current_user = users.get_current_user()
        email = current_user.email()

        #Read or write from DB
        person = Person(name = name, biography = biography, email=email)
        person.put()
        #Render a respose
        time.sleep(2)
        self.redirect('/')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/profile', ProfilePage),
    ('/create', CreateHandler),

], debug = True)
