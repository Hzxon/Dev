from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    names = ["Men's Doubles", "Men's Single", "Women's Doubles", "Women's Single"]
    return render_template("index.html")

@app.route("/more")
def more():
    return render_template("more.html")

@app.route("/mens_doubles")
def mens_doubles():
    return render_template("mens_doubles.html")

@app.route("/mens_single")
def mens_single():
    return render_template("mens_single.html")

@app.route("/womans_doubles")
def woman_doubles():
    return render_template("womans_doubles.html")

@app.route("/womans_single")
def woman_single():
    return render_template("womans_single.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "admin" and "password" == "123456":
            return render_template("success.html")
        return render_template("login.html", err="Login Failed, Please try agian!")

    return render_template("login.html")
    # return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")

# @app.route("/auth", methods=["GET", "POST"])
# def auth():
#     if request.methods == "POST":
#         username = request.form.get("username")
#         password = request.form.get("password")
#         if username == "admin" and "password" == "123456":
#             return render_template("success.html")
#         return render_template("login.html", err="Login Failed, Please try agian!")

#     return render_template("login.html")

# @app.route("/login", methods=["GET", "POST"])
# def login():
    
#     if request.method == "POST":
#         username = request.form.get("username")
#         password = request.form.get("password")
#         if username == "admin" and "password" == "123456":
#             return render_template("success.html")
#         return render_template("login.html", err="Login Failed, Please try again!")

#     return render_template("login")


# @app.route("/auth", methods=["GET", "POST"])
# def auth():
#     if request.method == "POST":
#         username = request.form.get("username")
#         password = request.form.get("password")
#         if username == "admin" and "password" == "123456":
#             return render_template("success.html")
#         return render_template("login.html", err="Login Failed, Please try agian!")

#     return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True) 