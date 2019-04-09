from flask import Flask, request, render_template
from pw import generate_password, password_list

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        sep = request.form["sep"]
        digit_min = int(request.form["digit-min"])
        digit_max = int(request.form["digit-max"])
        pw = generate_password(sep, digit_min, digit_max)
        return render_template("index.html", pw=pw)
        
    return render_template("index.html")

@app.route("/api")
def api_options():
    return "/api/pw\n/api/pwlist"

@app.route("/api/pw")
def get_password():
    return generate_password()

@app.route("/api/pwlist")
def get_passwords():
    n = int(request.args.get("n", 10))
    sep = request.args.get("sep", " ")
    digit_min = int(request.args.get("digitMin", 10))
    digit_max = int(request.args.get("digitMax", 99))
    return "<br/>".join(password_list(n, sep, digit_min, digit_max))