from flask import Flask,render_template,request,redirect
from until import scrapyphoto
import json
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/ajax')
def Ajax_find():
    key = request.args.get('find')
    allphoto = scrapyphoto.SpiderPhoto()
    List = allphoto.work_on(key)
    return json.dumps(List)

if __name__ == '__main__':
    app.run(debug=True)
