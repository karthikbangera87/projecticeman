import webapp2
import datetime
import os
import jinja2
import models

from google.appengine.api import users

template_env = jinja2.Environment(
        loader = jinja2.FileSystemLoader(os.getcwd()))

class Hello(webapp2.RequestHandler):
    def get(self):
    	userpref = models.get_userpref()
        current_time = datetime.datetime.now()
        if userpref:
        	current_time += datetime.timedelta(0,0,0,0,0,userpref.tz_offset)
        user = users.get_current_user()
        login_url = users.create_login_url(self.request.path)
        logout_url = users.create_logout_url(self.request.path)
        template = template_env.get_template('home.html')
        context = {

        	'current_time':current_time,
        	'user': user,
        	'login_url':login_url,
        	'logout_url':logout_url,
        	'userpref':userpref
        }
        self.response.write(template.render(context))


app = webapp2.WSGIApplication(

  [('/',Hello)],debug=True)