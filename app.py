from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    email = request.form.get("email")

    # Ensure email contains @ (Basic validation)
    if "@" not in email:
        return redirect(url_for("home"))  # Redirect back if invalid email

    return redirect(url_for("success", name=name))

@app.route("/success")
def success():
    name = request.args.get("name", "User")  
    return render_template("success.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
