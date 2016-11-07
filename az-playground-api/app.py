import random
import logging
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from docker import Client, errors

VERSION = '0.0.1'

START_PORT = 1000
END_PORT = 5000
WORKER_INFO = {
    'image': 'az-playground-instance',
    'source_port': 3000,
}

cli = Client(base_url='unix://var/run/docker.sock')
app = Flask(__name__)

logging.getLogger('flask_cors').level = logging.DEBUG
# CORS(app)

@app.route("/")
def hello():
    return jsonify(version=VERSION, message='All systems are go!')

def _get_container():
    host_port = random.randrange(START_PORT, END_PORT)
    source_port = WORKER_INFO['source_port']
    host_config = cli.create_host_config(port_bindings={source_port: host_port})
    container = cli.create_container(host_config=host_config,
                                     image=WORKER_INFO['image'],
                                     ports=[source_port],
                                     detach=True,
                                     tty=True)
    return container.get('Id'), host_port


@app.route('/create', methods=['POST'])
@cross_origin()
def create_worker():
    attempts = 0
    container_id = None
    host_port = None
    error = None
    while attempts < 10 and not container_id:
        attempts += 1
        container_id, host_port = _get_container()
        try:
            cli.start(container=container_id)
        except errors.APIError as e:
            # Failed (port binding might be taken)
            error = e
            container_id = None
    if not container_id:
        raise Exception("Unable to create container. attempts={}, last_error={}".format(attempts, error))

    return jsonify(port=host_port, container_id=container_id[:12])

if __name__ == "__main__":
    app.run()

