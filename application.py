import os
from flask import Flask
import flask
app=Flask(__name__)

@app.route('/')
def extract_text():
  print(" hello world")
  return "welcome to the page"
app.run()
