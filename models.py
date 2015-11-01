from google.appengine.api import users
from google.appengine.ext import ndb
import logging

class UserPref(ndb.Model):
	tz_offset = ndb.FloatProperty(default = 0.0)
	user = ndb.UserProperty(auto_current_user_add = True)

def get_userpref(user_id = None):
	if not user_id:
		user = users.get_current_user()
		if not user:
			return None
		user_id = user.user_id()
		key = ndb.Key('UserPref',user_id)
		userpref = key.get()
		logging.warning('key.get()')
		logging.warning(key.get())
		if not userpref:
			logging.warning('Creating a new preference for a user')
			userpref = UserPref(id = user_id)
	return userpref