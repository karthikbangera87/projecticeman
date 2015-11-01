import models
import webapp2

class Preference(webapp2.RequestHandler):
    def post(self):
    	userpref = models.get_userpref()
    	try:
        	tz_offset = float(self.request.get('tzoffset'))
        	userpref.tz_offset = tz_offset
        	userpref.put()
        except ValueError:
        	pass
        self.redirect('/')

app = webapp2.WSGIApplication(

  [('/pref',Preference)],debug=True)