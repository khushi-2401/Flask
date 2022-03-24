from flask import Flask, jsonify, request
app=Flask(__name__)
tasks=[
    {
        "contact":9876543210,
        "name":"abc",
        "done":True,
        "id":1,
    },
    {
        "contact":1123456789,
        "name":"xyz",
        "done":False,
        "id":2,
    }
]

@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide data"
        },400)
    task={
        "contact":request.json.get("contact"),
        "name":request.json["name"],
        "done":False,
        "id":tasks[-1]["id"]+1,
    }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"task added successfully"
    })
@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })
app.run()