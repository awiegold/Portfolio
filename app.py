from database import Database
from flask import Flask, render_template, request, redirect, url_for

# Create Flask app
app = Flask(__name__)

# Create Database instance
db = Database("portfolio.db")


# Home / Portfolio page (with message form)
@app.route("/", methods=["GET", "POST"])
def portfolio():
    if request.method == "POST":
        name = request.form['name']
        message = request.form['message']
        db.add_message(name, message)
    
    messages = db.get_messages()
    return render_template("portfolio.html", messages=messages)

# Learn About Me page
@app.route("/learnaboutme")
def learnaboutme():
    return render_template("learnaboutme.html")

@app.route("/myprojects")
def projects():
    return render_template("myprojects.html")

@app.route("/flexandgrid")
def flexandgrid():
    return render_template("flexandgrid.html")

@app.route("/goal1")
def goal1():
    return render_template("goal1.html")

@app.route("/goal2")
def goal2():
    return render_template("goal2.html")

@app.route("/goal3")
def goal3():
    return render_template("goal3.html")

@app.route("/delete/<int:id>")
def delete(id):
    db.delete_message(id)
    return redirect(url_for("portfolio"))

@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    if request.method == "POST":
        new_msg = request.form["message"]
        db.update_message(id, new_msg)
        return redirect(url_for("portfolio"))
    
    message = db.get_message(id)
    return render_template("edit.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)