from flask import Flask, request, jsonify
from worker import integrate


app = Flask(__name__)
TASKS ={} 

@app.route('/', methods=['GET'])
def list_task():
    tasks = {task_id: { 'ready': task.ready()}
             for task_id, task in TASKS.items()}
    return jsonify(tasks)

@app.route('/', methods=['PUT'])
def put_task():
    f = request.json['f']
    a = request.json['a']
    b = request.json['b']
    c = request.json['c']
    d = request.json['d']
    size = request.json.get('size', 100)

    task_id = len(TASKS)
    TASKS[task_id] = integrate.delay(f, a, b, c, d, size)

    response = {'result': task_id}

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
# http PUT http://localhost:5000  f='sqrt(4-xs**2)' a:=0 b:=2 c:=0 d:=2 size:=1000 
#  http GET http://localhost:5000