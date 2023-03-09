from flask import Flask, render_template,request
import smtplib

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

    message="You have been subscribet to my email news letter..."
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("victor.myid@gmail.com", "PASSWORD")
    server.sendmail("victor.myid@gmail.com",email,message)

    if not first_name or not last_name or not email:
        error_statement="All Details are Necessary..."
        return render_template("subscribe.html", error_statement=error_statement, 
                               first_name=first_name, 
                               last_name=last_name, 
                               email=email)

    return render_template("form.html", first_name=first_name, last_name=last_name, email=email)

app.run(debug=True)