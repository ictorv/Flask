from flask import Flask, render_template,request
app=Flask(__name__)
@app.route('/')
@app.route('/subscribe')
def subscribe():
    # ttle="About"
    return render_template("subscribe.html")
@app.route('/about')
def about():
    # ttle="About"
    return render_template("about.html")
@app.route('/form', methods=["POST"])
def form():
    # ttle="About"
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    return render_template("form.html", first_name=first_name, last_name=last_name, email=email)

app.run(debug=True)