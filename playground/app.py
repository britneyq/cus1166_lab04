from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
 def index():
     return render_template("index.html")


@app.route("/welcome/<string:course>")
def welcome(course):
   return render_template("welcome.html", course=course)

@app.route("/welcome/<string:course>")
def doiteach(course):
   doiteach = (course == "CUS1166") or (course == "CUS615")
   return render_template("layout.html", course=course, doteach=doteach)

@app.route("/welcome/<string:course>")
def roster(course):
   roster = [("John", "A"), ("Tom"," B"), ("Mary", "C"), ("Joe", "D")]
   return render_template("roster.html", course=course, roster=roster)

if __name__ == '__main__':

  app.run(
    host= '0.0.0.0' ,
    debug= True,
    port= 8080
  )
