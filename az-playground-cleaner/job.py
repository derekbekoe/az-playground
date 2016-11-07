import time
import datetime
from docker import Client, errors

cli = Client(base_url='unix://var/run/docker.sock')

WORKER_IMAGE = 'az-playground-worker:1'

HOUR = 3600
EXPIRY_SECS = HOUR*12
now_secs = int(round(time.time()))
containers = cli.containers(all=True)

to_remove = [c['Id'] for c in containers if c['Image'] == WORKER_IMAGE and c['Created']+EXPIRY_SECS < now_secs]

for t in to_remove:
    cli.remove_container(container=t, v=True, force=True)


print("Removed {} containers at {}".format(len(to_remove), str(datetime.datetime.now())))
