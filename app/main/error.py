from flask import Flask, render_template
from . import main

@main.errorhandler(404)
def four_ow_four(error):
  '''
  Function to render the 404 error page
  '''

  return render_template('fourOwfour.html'),404