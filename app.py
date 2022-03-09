from flask import Flask, jsonify, request

app = Flask(__name__)
persons = [
    {'name': 'Artyom', 'age': 21},
    {'name': 'John', 'age': 30}
]


@app.route('/')
def home():
    return "<h1>Hello world!</h1>"


@app.route('/persons', methods=['POST'])
def add_person():
    request_data = request.get_json()
    new_person = {
        'name': request_data['name'],
        'age': request_data['age']
    }
    persons.append(new_person)
    return jsonify(new_person)


@app.route('/persons/<string:name>')
def get_data_by_name(name):
    matching_persons = list(filter(lambda person: person['name'] == name, persons))
    return jsonify({'data': matching_persons})


@app.route('/persons')
def get_persons():
    return jsonify({'persons': persons})


app.run(port=5000)
