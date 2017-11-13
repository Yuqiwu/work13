from flask import Flask, render_template, request
import urllib2, json

my_app = Flask(__name__)

@my_app.route("/")
def root():
    return render_template("geoip.html")

@my_app.route("/result", methods=["POST"])
def result():
    website = request.form["website"]
    u = urllib2.urlopen("http://www.freegeoip.net/json/%s" % website)
    data_string = u.read()
    d = json.loads(data_string)
    return render_template("result.html", ip = d["ip"], country_code = d["country_code"], country_name = d["country_name"], region_code = d["region_code"], city = d["city"], zip_code = d["zip_code"], time_zone = d["time_zone"], latitude = d["latitude"], longitude = d["longitude"], metro_code = d["metro_code"])

if __name__ == "__main__":
    my_app.debug = True
    my_app.run()
