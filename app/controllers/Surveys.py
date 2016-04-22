"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
from time import strftime
import string
string.letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
import random
random.choice(string.letters)

class Surveys(Controller):
    def __init__(self, action):
        super(Surveys, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.

            self.load_model('WelcomeModel')
        """

    """ This is an example of a controller method that will load a view for the client """

    def index(self):
        """ 
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_all_users()
        """
        try:
            session['count']
        except:
            session['count'] = 1
        return self.load_view('index.html')

    def results(self):
        session['name'] = request.form['name']
        session['location'] = request.form['location']
        session['language'] = request.form['language']
        session['comment'] = request.form['name']
        session['count'] += 1
        return redirect('/surveys/show')

    def show(self):
        return self.load_view('show.html')

