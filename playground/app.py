from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
 def index():
     return render_template("index.html")


@app.route("/welcome/<string:student_name>")
def welcome(student_name):
   return render_template("welcome.html", student_name = student_name)


@app.route("/welcome/<int:grade_view>")
def roster(grade_view):
   roster = [("John", "A"), ("Tom"," B"), ("Mary", "C"), ("Joe", "D"), ("Bob", "F")]
   return render_template("roster.html", grade_view = grade_view, roster=roster)

if __name__ == '__main__':

  app.run(
    host= '0.0.0.0' ,
    debug= True,
    port= 8080
  )
