from flask import Flask, jsonify, request
from werkzeug.exceptions import abort
from data import toys, categories


app = Flask(__name__)


@app.route("/toys")
def index():
    return jsonify(toys)


@app.route("/toys/<toy_id>")
def show_toy(toy_id):
    try:
        requested_toy = toys[int(toy_id)]
        return jsonify(requested_toy)
    except IndexError:
        abort(404)

@app.route("/toys", methods=["POST"])
def create_toys():
    try:
        if request.form["category_id"] and request.form["name"] and \
           request.form["description"] and request.form["price"]:
            toys.append(request.form)
            return jsonify(toys[-1])
    except KeyError:
        abort(422)



@app.route("/toys/<toy_id>", methods=["PUT", "GET"])
def update(toy_id):
    if int(toy_id) < len(toys):
        if request.method == "PUT":
            toys[int(toy_id)].update(request.form)
            return jsonify(toys[int(toy_id)])
    else:
        show_toy(toy_id)


@app.route("/toys/<toy_id>", methods=["DELETE", "GET"])
def delete_toy(toy_id):
    if request.method == "DELETE":
        toy_deleted = toys.pop()
        return jsonify(toy_deleted)
    elif request.method == "GET":
        show_toy(toy_id)


@app.route("/categories")
def index_category():
    return jsonify(categories)


@app.route("/categories/<category_id>")
def show_category(category_id):
    try:
        requested_category = categories[int(category_id)]
        return jsonify(requested_category)
    except IndexError:
        abort(404)


@app.route("/categories", methods=["POST"])
def create_category():
    try:
        if request.form["name"]:
            categories.append(request.form)
            return jsonify(categories[-1])
    except KeyError:
        abort(422)


@app.route("/categories/<category_id>", methods=["PUT", "GET"])
def update_category(category_id):
    if int(category_id) < len(categories):
        if request.method == "PUT":
            to = categories[int(category_id)].update(request.form)
            return jsonify(categories[int(category_id)])
    else:
        show_category(category_id)


@app.route("/categories/<category_id>", methods=["DELETE", "GET"])
def delete_category(category_id):
    if request.method == "DELETE":
        category_deleted = categories.pop()
        return jsonify(category_deleted)
    elif request.method == "GET":
        show_category(category_id)



@app.route("/categories/<name>/toys")
def additional(name): 
    result = []
    for i, dico in enumerate(categories):
        if dico["name"] == name:
            cat_index = i
        print("ici")
    for dico in toys:
        try:
            if dico["category_id"] == cat_index:
                result.append(dico)
        except:
            abort(404)



    return jsonify(result)


if __name__ == ("__main__"):
    app.run(debug=True)
