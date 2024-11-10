from flask import Flask, request, render_template
from readF import genTables, getFile, getRelations

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        file = request.form['filename']
        Nfile = getFile(file)
        tables = genTables(Nfile)
        relations = getRelations(tables)
        return render_template('index.html', sqlData=tables, relations=relations)
    return render_template('index.html', sqlData=False, relations=False)

# POST ROUTES --------------------------------------------
@app.route("/upload-file", methods=['POST'])
def uploadF():
    return {"lol" : "lol"}

if __name__ == '__main__':
    app.run()
