from flask import Flask
from flask import render_template
from flask_restful import Resource, Api
from kubernetes import client, config
from pprint import pprint
import json
import os
app = Flask(__name__)
api = Api(app)

def create_service_object(unique_name):
    metadata = client.V1ObjectMeta(
        name=unique_name,
        labels={"app": unique_name, "type" : "minecraft"}
    )
    spec = client.V1ServiceSpec(
        ports=[
            client.V1ServicePort(name="minecraft",port=25565,target_port=25565),
            client.V1ServicePort(name="rcon", port=25575, target_port=25575)
        ],
        selector={"app": unique_name},
        type="LoadBalancer"
    )
    service = client.V1Service(
        api_version="v1",
        kind="Service",
        metadata=metadata,
        spec=spec
    )
    return service

def create_service(api_instance, service_object):
    api_response = api_instance.create_namespaced_service(
        body=service_object,
        namespace="default")
    return "Service created. status= {}".format(str(api_response.status))

def create_deployment_object(unique_name):
    # Configureate Pod template container
    container = client.V1Container(
        name=unique_name,
        image="openhack/minecraft-server:2.0",
        ports=[client.V1ContainerPort(container_port=25565),
               client.V1ContainerPort(container_port=25575)],
        env=[client.V1EnvVar(name = 'EULA', value = 'TRUE')],
        volume_mounts=[client.V1VolumeMount(mount_path="data", name=unique_name)])

    # Create and configurate a spec section
    template = client.V1PodTemplateSpec(
        metadata=client.V1ObjectMeta(labels={"app": unique_name, "type" : "minecraft"}),
        spec=client.V1PodSpec(containers=[container],
        volumes=[client.V1Volume(name=unique_name, persistent_volume_claim = (client.V1PersistentVolumeClaimVolumeSource(claim_name="azure-managed-disk-"+unique_name)))]))
    # Create the specification of deployment
    spec = client.ExtensionsV1beta1DeploymentSpec(
        replicas=1,
        template=template)
    # Instantiate the deployment object
    deployment = client.ExtensionsV1beta1Deployment(
        api_version="extensions/v1beta1",
        kind="Deployment",
        metadata=client.V1ObjectMeta(name=unique_name),
        spec=spec)

    return deployment

def create_deployment(api_instance, deployment):
    # Create deployement
    api_response = api_instance.create_namespaced_deployment(
        body=deployment,
        namespace="default")
    return "Deployment created. status= {}".format(str(api_response.status))

def create_vpc_object(unique_name):

    metadata = client.V1ObjectMeta(
        name = "azure-managed-disk-" + unique_name,
        annotations = {"volume.beta.kubernetes.io/storage-class": "managed-premium"}
    )

    spec = client.V1PersistentVolumeClaimSpec(
        access_modes = ["ReadWriteOnce"],
        resources = client.V1ResourceRequirements(requests={"storage": "5Gi"})
    )

    body = client.V1PersistentVolumeClaim(
        api_version="v1",
        kind="PersistentVolumeClaim",
        metadata=metadata,
        spec=spec
    )

    return body

def create_vpc(api_instance, vpc_object):
    api_response = api_instance.create_namespaced_persistent_volume_claim(
        body=vpc_object,
        namespace="default")
    return "VPC created. status= {}".format(str(api_response.status))

def is_mc(metadata):
    if hasattr(metadata, 'labels'):
        if metadata.labels is not None:
            if 'type' in metadata.labels:
                if metadata.labels['type'] == 'minecraft':
                    return True
    return False

class List(Resource):
    def get(self):
        output = []
        if os.path.isfile('/run/secrets/kubernetes.io/serviceaccount/..data/namespace'):
            config.load_incluster_config()
        else:
            config.load_kube_config()
        v1 = client.CoreV1Api()
        ret = v1.list_namespaced_service('default')
        for i in ret.items:
            if is_mc(i.metadata):
                eachOutput = {}
                eachOutput['name'] = i.metadata.name
                eachOutput['endpoints'] = {}

                try:
                    for port in i.spec.ports:
                        eachOutput['endpoints'][port.name] = str(i.status.load_balancer.ingress[0].ip) + ":" + str(port.port)
                    output.append(eachOutput)
                except:
                    continue
        return output

class Add(Resource):
    def get(self, unique_name):
        if os.path.isfile('/run/secrets/kubernetes.io/serviceaccount/..data/namespace'):
            config.load_incluster_config()
        else:
            config.load_kube_config()
        extensions_v1beta1 = client.ExtensionsV1beta1Api()
        coreV1 = client.CoreV1Api()
        vpc_object = create_vpc_object(unique_name)
        deployObject = create_deployment_object(unique_name)
        service_obj = create_service_object(unique_name)


        vpc_status = create_vpc(coreV1, vpc_object)
        status =create_deployment(extensions_v1beta1,deployObject)
        service_status = create_service(coreV1,service_obj)
        return vpc_status + "\n" + status + "\n" + service_status

def delete_deployment(api_instance,unique_name):
    api_response = api_instance.delete_namespaced_deployment(
        name=unique_name,
        namespace="default",
        body=client.V1DeleteOptions(
            propagation_policy='Foreground',
            grace_period_seconds=5))
    return "Deployment deleted. status={}".format(str(api_response.status))

def delete_service(api_instance,unique_name):
    api_response = api_instance.delete_namespaced_service(
        name=unique_name,
        namespace="default",
        body=client.V1DeleteOptions(
            propagation_policy='Foreground',
            grace_period_seconds=5))
    return "Service deleted. status={}".format(str(api_response.status))

def delete_vpc(api_instance,unique_name):
    api_response = api_instance.delete_namespaced_persistent_volume_claim(
        name = "azure-managed-disk-" + unique_name,
        namespace="default",
        body=client.V1DeleteOptions(
            propagation_policy='Foreground',
            grace_period_seconds=5))
    return "VPC deleted. status={}".format(str(api_response.status))

class Delete(Resource):
    def get(self,unique_name):
        if os.path.isfile('/run/secrets/kubernetes.io/serviceaccount/..data/namespace'):
            config.load_incluster_config()
        else:
            config.load_kube_config()
        extensions_v1beta1 = client.ExtensionsV1beta1Api()
        coreV1 = client.CoreV1Api()
        status = delete_deployment(extensions_v1beta1,unique_name)
        service_status = delete_service(coreV1,unique_name)
        vpc_status = delete_vpc(coreV1,unique_name)

        return vpc_status + "\n" + status + "\n" + service_status

class Ping(Resource):
    def get(self):
        return "ack"

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

api.add_resource(List, '/list')
api.add_resource(Add, '/add/<unique_name>')
api.add_resource(Delete,'/delete/<unique_name>')
api.add_resource(Ping,'/ping')

if __name__ == '__main__':
     app.run(port='5002',host='0.0.0.0')
