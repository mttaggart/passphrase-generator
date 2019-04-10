from flask import Flask, abort, request, render_template
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
    pw = generate_password()
    return render_template("index.html", pw=pw)

@app.route("/api", methods=["GET","POST"])
def api():
    return render_template("api.html", n=10, sep="_", digit_min=10, digit_max=99)

@app.route("/api/pw")
def get_password():
    return generate_password()

@app.errorhandler(400)
def bad_request(error):
    return "Your API request did not match the specified parameters."

@app.route("/api/pwlist")
def get_passwords():
    n = int(request.args.get("n", 10))
    if n > 100:
        abort(400)
    
    sep = request.args.get("sep", " ")
    digit_min = int(request.args.get("digitMin", 10))
    digit_max = int(request.args.get("digitMax", 99))
    return "\n".join(password_list(n, sep, digit_min, digit_max))

if __name__ == "__main__":
    app.run(host="0.0.0.0")