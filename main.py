from flask import Flask, render_template, request, redirect
from indeed import extract_indeed_jobs
from wwr import extract_wwr_jobs

app = Flask("JobScrapper")

db = {
    "python": []
}


@app.route("/")  # decorator
def home():
    return render_template("home.html", name="nico")


db = {}


@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else:
        indeed = extract_indeed_jobs(keyword)
        wwr = extract_wwr_jobs(keyword)
        jobs = indeed + wwr
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)


@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword is not db:
        return redirect(f"/search?keyword={keyword}")


app.run("0.0.0.0", port=8001)

'''
from indeed import extract_indeed_jobs
from wwr import extract_wwr_jobs
from file import save_to_file

keyword = input("What do you want to search for?")

indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)
jobs = indeed + wwr

save_to_file(keyword, jobs)
'''
