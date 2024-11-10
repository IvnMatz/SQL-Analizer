from flask import Flask, request, render_template
from readF import genTables, getFile

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/sql/<fileN>")
def file(fileN):
    file = getFile(fileN)

    tables = genTables(file)
    return render_template('file.html', sqlData=tables)

# POST ROUTES --------------------------------------------
@app.route("/upload-file", methods=['POST'])
def uploadF():
    return {"lol" : "lol"}

if __name__ == '__main__':
    app.run()
