from . import index
from flask import request, render_template, jsonify


@index.route('/', methods=['GET'])
def root():
    return render_template("index.html")


@index.route('/api', methods=['POST'])
def api():
    print(request.json, request.form)
    # request.json.get("arg")
    return jsonify({"code": 0, "msg": "success"})
