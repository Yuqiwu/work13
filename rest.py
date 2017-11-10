from flask import Flask, render_template
import urllib2, json

my_app = Flask(__name__)

@my_app.route("/")
def root():
    u = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=TBfi8kn1apA4h9iXK5NsKXGgu9tfaxEq9v1bdMru")
    data_string = u.read()
    d = json.loads(data_string)
    return render_template("rest.html", image = d["url"], explanation = d["explanation"])

if __name__ == "__main__":
    my_app.debug = True
    my_app.run()
