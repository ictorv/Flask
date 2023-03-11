from flask import Flask, render_template,request,redirect
# import smtplib
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app=Flask(__name__)

####
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///friends.sqlite3'
db=SQLAlchemy(app)
####

class Friends(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(200),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)

    # def __repr__(self):
    #     return '<Name %r>' % self.id
    db.create_all()

@app.route('/')
@app.route('/subscribe')
def subscribe():
    # ttle="About"
    return render_template("subscribe.html")
@app.route('/about')
def about():
    # ttle="About"
    return render_template("about.html")

@app.route('/friend', methods=["POST","GET"])
def friend():
    # ttle="About"
    if request.method=="POST":
        friend_name=request.form.get('name')
        new_friend=Friend(name=friend_name)

        try:
            db.session.add(new_friend)
            db.session.commit()
            return redirect('/friend')
        except:

            return "Error in adding Friend"

    else:
        friends=Friend.query.order_by(Friend.date_created)
        return render_template("friend.html", friends=friends)

@app.route('/form', methods=["POST"])
def form():
    # ttle="About"
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")

    # message="You have been subscribet to my email news letter..."
    # server=smtplib.SMTP("smtp.gmail.com",587)
    # server.starttls()
    # server.login("victor.myid@gmail.com", "PASSWORD")
    # server.sendmail("victor.myid@gmail.com",email,message)

    if not first_name or not last_name or not email:
        error_statement="All Details are Necessary..."
        return render_template("subscribe.html", error_statement=error_statement, 
                               first_name=first_name, 
                               last_name=last_name, 
                               email=email)

    return render_template("form.html", first_name=first_name, last_name=last_name, email=email)

app.run(debug=True)