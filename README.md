
# CHECK FOR
- References to old IP address
- The image name in app.py
- Modify the port range in app.py

# FRONTEND SERVICE
```
docker build -t derekbekoe/az-playground-api:0.2 az-playground-api
docker build -t derekbekoe/az-playground-cleaner:0.2 az-playground-cleaner
docker build -t derekbekoe/az-playground-frontend:0.2 az-playground-frontend
docker build -t derekbekoe/az-playground-instance:0.2 az-playground-instance
```
```
docker push derekbekoe/az-playground-api:0.2
docker push derekbekoe/az-playground-cleaner:0.2
docker push derekbekoe/az-playground-frontend:0.2
docker push derekbekoe/az-playground-instance:0.2
```

# API SERVICE
Check the configs in the API service app.py (e.g. worker image name)
```
sudo docker build -t az-playground-api:1 .
sudo docker run -it -d -v /var/run/docker.sock:/var/run/docker.sock -p 81:5000 --name api az-playground-api:1
```

# WORKER SERVICE
This workers get started automatically by the API Service
```
sudo docker build -t az-playground-worker:1 .
# Only run this for testing a single worker.
sudo docker run -it -d -p <host_ip>:3000 az-playground-worker:1
```

# CLEANER SERVICE
Removes old workers
```
sudo docker build -t az-playground-cleaner:1 .
sudo docker run -it -d -v /var/run/docker.sock:/var/run/docker.sock --name cleaner az-playground-cleaner:1
```


---
az login
az group create -l eastus -n azure-cli-playground
az vm create -g azure-cli-playground -n azplayground --image UbuntuLTS --size Standard_D3_v2 --public-ip-address-dns-name az-playground-a1
az vm open-port --port 80-5000 -g azure-cli-playground -n azplayground3

ssh IP_ADDRESS

curl -sSL https://get.docker.com/ | sh

sudo

curl -L "https://github.com/docker/compose/releases/download/1.8.1/docker-compose-$(uname -s)-$(uname -m)" > /usr/local/bin/docker-compose

chmod +x /usr/local/bin/docker-compose

az network nsg rule create --access Allow --destination-address-prefix '*' --destination-port-range 80-5000 --direction InBound -g debekoe1 --nsg-name playground-test1NSG --protocol Tcp --source-address-prefix '*' --source-port-range '*' -n allow-all --priority 1001

wget https://raw.githubusercontent.com/derekbekoe/az-playground/master/docker-compose.yml

Specify the endpoint (SPECIFY_ENDPOINT) in compose file!

docker-compose up

Or rename docker-compose-build.yml then:  
docker-compose up --build
