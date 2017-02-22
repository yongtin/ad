from flask import Flask, url_for, redirect
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/ad")
def ad():
  return "<html><h1>Hello. I am Baymax. Your personal healthcare companion. I'll scan you. </h1></html>"

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=3000)
  conn.close()
