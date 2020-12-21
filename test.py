import webapp2
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write("Hello World App Executed Well and Good")
app=webapp2.WSGIApplication([('/', MainPage),],debug=True)
