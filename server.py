from flask import Flask, render_template
from game import Checkerboard
app = Flask (__name__)

@app.route("/<int:x>/<int:y>")
def checker(x, y):
    result = Checkerboard(x, y)
    return render_template ("index.html", collumn= result) 
    








if __name__== "__main__":
    app.run (debug=True)