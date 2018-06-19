from flask import Flask
from flask_restful import Resource, Api
from kubernetes import client, config
import json
app = Flask(__name__)
api = Api(app)


class List(Resource):
    def get(self):
        output = []
        config.load_kube_config()
        v1 = client.CoreV1Api()
        print("Listing pods with their IPs:")
        ret = v1.list_pod_for_all_namespaces(watch=False)

        for i in ret.items:
            eachOutput = {}
            eachOutput['name']=i.metadata.name
            eachOutput['ip']=i.status.pod_ip
            output.append(eachOutput)
        return output

class Add(Resource):
    def get(self):
        return "Adding a new resource"

class Delete(Resource):
    def get(self):
        return "Deleting a new resource"

api.add_resource(List, '/list')
api.add_resource(Add, '/add')
api.add_resource(Delete,'/delete')


if __name__ == '__main__':
     app.run(port='5002')