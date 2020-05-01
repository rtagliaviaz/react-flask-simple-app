from flask import Flask, request, jsonify
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS

app = Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost/newflaskcrud'
mongo = PyMongo(app)

CORS(app)

db = mongo.db.tasks

#Routes
@app.route('/tasks', methods=['POST'])
def createTask():
  id = db.insert({
    'title': request.json['title']
  })
  return jsonify(str(ObjectId(id)))

@app.route('/tasks', methods=['GET'])
def getTasks():
  tasks = []
  for doc in db.find():
    tasks.append({
      '_id': str(ObjectId(doc['_id'])),
      'title': doc['title']
    })
  return jsonify(tasks)

@app.route('/task/<id>', methods=['GET'])
def getTask(id):
  task = db.find_one({'_id': ObjectId(id)})
  print(task)
  return jsonify({
    '_id': str(ObjectId(task['_id'])),
    'title': task['title']
  })

@app.route('/tasks/<id>', methods=['DELETE'])
def deleteTask(id):
  db.delete_one({'_id': ObjectId(id)})
  return jsonify({'msg': 'task deleted'})

@app.route('/tasks/<id>', methods=['PUT'])
def editTask(id):
  db.update_one({'_id': ObjectId(id)}, {'$set': {
    'title': request.json['title']
  }})
  return jsonify({'msg': 'task updated'})

if __name__ == "__main__":
    app.run(debug=True)