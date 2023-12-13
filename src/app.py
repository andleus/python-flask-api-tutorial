from flask import Flask;
from flask import Flask, jsonify;
from flask import request;

app = Flask(__name__)

pets= {
            "pet1": "Urraca",
            "pet2": "Roky"
            }

todos = [ { "label": "My first task", "done": False } ]


@app.route("/")
def welcome1():
    return"<h3>Bom dia</h3>"

@app.route("/todos1", methods=["GET"])
def hello_world1():
    return"<h1>Hello!</h1>"

# @app.route('/todos', methods=['GET'])
# def hello_world():
#     return "<h1>Hello!</h1>"

@app.route("/get")
def welcome3():
    response = {"message": "done",
               "results": "From GET"
               }
    # return"<h3>Bom dia</h3>"
    return response

@app.route("/getPets", methods=["GET"])
def welcome4():
    json_todos = jsonify(pets)

    return json_todos

@app.route("/todos", methods=["GET"])
def welcome5():
    json_pets = jsonify(todos)

    return json_pets


@app.route("/todos1", methods=["POST"])
def add_new_todo1():
    request_body = request.data
    print("Request with body params -> ",request_body)
    return 'Response from POST method'


@app.route("/todos", methods=["POST"])
def add_new_todo():
    request_body = request.json
    print("Request with body params -> ",request_body)
    for todo in request_body:
        todos.append(todo)
    print("Request with body params -> ",request_body)
    return jsonify(todos)


@app.route("/todos/<int:position>", methods=["DELETE"])
def delete_todo(position):
    print("Postion to delete -> ",position)
    # del todos[position]
    todos.pop((position-1))

    # return 'The element has been deleted'
    return jsonify(todos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)