from flask import Flask, render_template, request, session, redirect,flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from flask_mail import Mail
import json
import os
import math
from datetime import datetime


local_server = True
with open("config.json", "r") as c:
    params = json.load(c)["params"]

app = Flask(__name__)
app.secret_key = "super-secret-key"
app.config["UPLOAD_FOLDER"] = params["upload_location"]
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT = "465",
    MAIL_USERNAME = params["user"],
    MAIL_PASSWORD = params["password"]
)
mail = Mail(app)
if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params["local_uri"]
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params["prod_uri"]

db = SQLAlchemy(app)

class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    phone_num = db.Column(db.String(15), nullable=False)
    message = db.Column(db.String(150), nullable=True)
    date = db.Column(db.String(12), nullable=False)

class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(50), nullable=False)
    tagline = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(150), nullable=False)
    date = db.Column(db.String(12), nullable=False)

@app.route("/")
def home():
    posts = Posts.query.filter_by().all()
    last = math.ceil(len(posts)/int(params["no_of_posts"]))
    page= request.args.get("page")
    print(page)
    if(not str(page).isnumeric()):
        page = 1
    page = int(page)
    posts = posts[(page-1)*int(params["no_of_posts"]):(page-1)*int(params["no_of_posts"])+ int(params["no_of_posts"])]
    #pagination
    if (page==1):
        prev = "#"
        next = "/?page=" + str(page+1)
    elif (page==last):
        prev = "/?page=" + str(page-1)
        next = "#"
    else:
        prev = "/?page=" + str(page-1)
        next = "/?page=" + str(page+1)

    return render_template("index.html", params=params, posts=posts, prev =prev, next=next)


@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/dashboard", methods=["GET","POST"])
def dashboard():
    if "user" in session and session["user"] == params["admin_user"]:
        posts = Posts.query.all()
        return render_template('dashboard.html', params=params, posts=posts)
    if request.method=="POST":
        username = request.form.get("uname")
        userpass = request.form.get("pass")
        if (username== params["admin_user"]) and userpass== params["admin_password"]:
            session["user"] = username
            posts = Posts.query.all()
            return render_template('dashboard.html', params=params, posts=posts)

    else:
        return render_template('login.html', params=params)

@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/dashboard')

@app.route("/edit/<string:sno>", methods = ['GET', 'POST'])
def edit(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method == 'POST':
            box_title = request.form.get('title')
            tline = request.form.get('tline')
            slug = request.form.get('slug')
            content = request.form.get('content')
            date = datetime.now()

            if sno=='0':
                post = Posts(title=box_title, slug=slug, content=content, tagline=tline, date=date)
                db.session.add(post)
                db.session.commit()
            else:
                post = Posts.query.filter_by(sno=sno).first()
                post.title = box_title
                post.slug = slug
                post.content = content
                post.tagline = tline
                post.date = date
                db.session.commit()
                return redirect('/edit/'+sno)
        post = Posts.query.filter_by(sno=sno).first()
        return render_template('edit.html', params=params, post=post, sno=sno)

@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html', params=params, post=post)

@app.route("/uploader", methods = ['GET', 'POST'])
def uploader():
    if ('user' in session and session['user'] == params['admin_user']):
        if (request.method == 'POST'):
            f= request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename) ))
            return "Uploaded successfully"

@app.route("/delete/<string:sno>", methods = ['GET', 'POST'])
def delete(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        post = Posts.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/dashboard')

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if(request.method=="POST"):
        '''Add Entries to database'''
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = Contacts(name=name, email=email, phone_num=phone, message=message, date=datetime.now())
        db.session.add(entry)
        db.session.commit()
        # mail.send_message("New Message from "+ name,
        #                   sender= email, recipients= [params["user"]],
        #                   body = message + "\n"+ phone)
        flash("Congratulations! Your request has been submitted, we will get back to you soon.", "success")
    return render_template("contact.html")

app.run(debug=True)