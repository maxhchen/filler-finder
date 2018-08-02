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
    limit = ndb.IntegerProperty()

class Comment(ndb.Model):
    message = ndb.StringProperty()
    user_key = ndb.KeyProperty() #store the user key to point to who posted it
    filler_key = ndb.KeyProperty() #store the filler key in which the comment is in

class Filler(ndb.Model):
    name = ndb.StringProperty()
    type = ndb.StringProperty()
    location = ndb.StringProperty()
    #picture = ndb.BlobProperty()
    description = ndb.StringProperty()
    company = ndb.StringProperty()
    #The creator's email address
    current_user_email = ndb.StringProperty()

class APIkey(ndb.Model):
    key = ndb.StringProperty()

######################################################################

class HomePage(webapp2.RequestHandler):
    def get(self):
        #get api key from datastore
        apiKey = APIkey.query().get()

        login_url = "/"
        logout_url = "/"

        #get the user
        current_user = users.get_current_user()

        if not current_user:
            login_url = users.create_login_url('/')
        else:
            logout_url = users.create_logout_url('/')
            #see if a user has any user data with the same email
            current_person = User.query().filter(User.email == current_user.email()).get()
            #if they don't create a User object with their email assigned
            if not current_person:
                current_person = User(email = current_user.email(), limit = 0)
                current_person.put()

        filler_list = Filler.query().fetch()

        templateVars = {
        "current_user" : current_user,
        "login_url" : login_url,
        "logout_url" : logout_url,
        "filler_list" : filler_list,
        "apiKey" : apiKey,
        }
        template = env.get_template("templates/home.html")
        self.response.write(template.render(templateVars))

class Description(webapp2.RequestHandler):
    def get(self):
        #get API key from datastore
        apiKey = APIkey.query().get()

        login_url = "/"
        logout_url = "/"
        current_user = users.get_current_user()

        if not current_user:
            login_url = users.create_login_url('/')
        else:
            logout_url = users.create_logout_url('/')

        urlsafe_key = self.request.get("key")
        key = ndb.Key(urlsafe = urlsafe_key)
        filler = key.get()

        templateVars = {
        "current_user" : current_user,
        "login_url" : login_url,
        "logout_url" : logout_url,
        "filler" : filler,
        "apiKey" : apiKey,
        }

        template = env.get_template("templates/description.html")
        self.response.write(template.render(templateVars))

class Index(webapp2.RequestHandler):
    def get(self):
        login_url = "/"
        logout_url = "/"
        current_user = users.get_current_user()

        if not current_user:
            login_url = users.create_login_url('/')
        else:
            logout_url = users.create_logout_url('/')

        filler_list = Filler.query().order(Filler.name).fetch()

        templateVars = {
        "current_user" : current_user,
        "login_url" : login_url,
        "logout_url" : logout_url,
        'filler_list' : filler_list,
        }
        template = env.get_template("templates/fillerList.html")
        self.response.write(template.render(templateVars))

class AddFiller(webapp2.RequestHandler):
    def get(self):

        login_url = "/"
        logout_url = "/"
        current_user = users.get_current_user()

        if not current_user:
            login_url = users.create_login_url('/')
        else:
            logout_url = users.create_logout_url('/')

        templateVars = {
            'current_user' : current_user,
            "login_url" : login_url,
            "logout_url" : logout_url,
        }

        template = env.get_template("templates/addFiller.html")
        self.response.write(template.render(templateVars))

    def post(self):
        #get the user
        current_user = users.get_current_user()

        #get current_person(user object)
        current_person = User.query().filter(User.email == current_user.email()).get()
        #make one if they dont have one
        if not current_person:
            current_person = User(email = current_user.email(), limit = 0)
            current_person.put()

        template = env.get_template("templates/fillerList.html")
        #Get the values from user entered info
        name = self.request.get('name')
        location = self.request.get('location')
        type = self.request.get('type')
        description = self.request.get('description')
        company = self.request.get('company')
        #picture = self.request.get('picture')
#        picture = images.resize(picture, 50, 50)

        #Get the email of the current user so their email can be added to the "Added By:" section of the description page
        current_user = users.get_current_user()
        #Check if user exist and if they have an account and it they have exceeded their limits
        if current_user and current_person and current_person.limit < 10:

            #Check whether or not there is an existing filler if not, add one
            current_filler = Filler.query().filter(Filler.name == name).get()

            if not current_filler:
                ########picture = picture NOT ADDED YET
                current_filler = Filler(name = name, location = location, type = type, description = description, company = company, current_user_email = current_user.email())
                current_filler.put()
                current_person.limit += 1
                current_person.put()

        else:
            current_user_email = "None"


        self.response.write(template.render())

        time.sleep(2)
        self.redirect("/")
        #### self.response.write(self.request.POST)

class About(webapp2.RequestHandler):
    def get(self):
        login_url = "/"
        logout_url = "/"

        current_user = users.get_current_user()
        if current_user:
            logging.info(current_user.user_id())

        if not current_user:
            login_url = users.create_login_url('/')
        else:
            logout_url = users.create_logout_url('/')

        templateVars = {
        "current_user" : current_user,
        "login_url" : login_url,
        "logout_url" : logout_url,
        }
        template = env.get_template("templates/about.html")
        self.response.write(template.render(templateVars))


app = webapp2.WSGIApplication([
    ('/', HomePage),
    ('/description', Description),
    ('/index', Index),
    ('/add', AddFiller),
    ('/about', About),
], debug = True)
