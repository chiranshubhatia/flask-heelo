import os
from flask import Flask
import flask
app=Flask(__name__)

@app.route('/')
def extract_text():
  print(" hello world")
  return '''
<html><head><title>Upload new File</title>
    </head><body><h1>OCR extraction for HDCF form 1500</h1>
     <h2>HIT button for demo run</h2>
  
    <form method="post" enctype="multipart/form-data">
          
         <input type="submit" value="RUN">
         </p>
         </form></h2><div style="background-color: rgb(255, 143, 0); display: none; color: white; text-align: center; position: fixed; top: 0px; left: 0px; width: 100%; height: auto; min-width: 100%; min-height: auto; max-width: 100%; font: 12px &quot;Helvetica Neue&quot;, Helvetica, Arial, Geneva, sans-serif; cursor: pointer; padding: 5px;"><span style="color: white; font: 12px &quot;Helvetica Neue&quot;, Helvetica, Arial, Geneva, sans-serif;">You have turned off the paragraph player. You can turn it on again from the options page.</span><img src="chrome-extension://gfjopfpjmkcfgjpogepmdjmcnihfpokn/img/icons/icon-close_16.png" style="width: 20px; height: auto; min-width: 20px; min-height: auto; max-width: 20px; float: right; margin-right: 10px;"></div></body></html>
'''
