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
    #lat = ndb.FloatProperty()
    #long = ndb.FloatProperty()
    picture = ndb.BlobProperty()
    description = ndb.StringProperty()
    company = ndb.StringProperty()

######################################################################

class HomePage(webapp2.RequestHandler):
    def get(self):
        login_url = "/"
        logout_url = "/"

        current_user = users.get_current_user()
        if current_user:
            logging.info(current_user.user_id())


        if not current_user:
            print("no one logged in")
            login_url = users.create_login_url('/')
        else:
            logging.info("This is the main handler")
            logout_url = users.create_logout_url('/')


        filler = Filler.query().get()
        if not filler:
            filler = Filler(name="test_name_1", type="test_type", location="test_location", description="test filler #1").put()

        filler_list = Filler.query().fetch()

        templateVars = {
        "current_user" : current_user,
        "login_url" : login_url,
        "logout_url" : logout_url,
        "filler" : filler,
        "filler_list" : filler_list,
        }
        template = env.get_template("templates/home.html")
        self.response.write(template.render(templateVars))

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

        #Get the values from user entered info
        name = self.request.get('name')
        location = self.request.get('location')
        type = self.request.get('type')
        description = self.request.get('description')
        company = self.request.get('company')

        current_filler = Filler.query().filter(Filler.location == location).get()

        if not current_filler:
            current_filler = Filler(name = name, location = location, type = type, description = description, company = company)
            current_filler.put()

        templateVars = {

        }
        self.response.write(template.render(templateVars))
        self.redirect("/")
        #### self.response.write(self.request.POST)


app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/description', Description),
    ('/search', Search),
    ('/add', AddFiller),
], debug = True)
