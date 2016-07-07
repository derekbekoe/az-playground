
# CHECK FOR
- References to old IP address
- The image name in app.py
- Modify the port range in app.py

# FRONTEND SERVICE
```
sudo docker build -t az-playground-frontend:1 .
sudo docker run -p 80:80 -d --name frontend az-playground-frontend:1
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
az resource group create -l westus -n azure-cli-playground
az vm create -g azure-cli-playground -n azplayground --image UbuntuLTS --size Standard_D3_v2 --dns-name-for-public-ip az-playground-d1
az network nsg rule create --access Allow --destination-address-prefix '*' --destination-port-range 80-60000 --direction InBound -g azure-cli-playground --nsg-name azplaygroundNSG --protocol Tcp --source-address-prefix '*' --source-port-range '*' -n allow-all --priority 1001

ssh az-playground-d1.westus.cloudapp.azure.com
OR
ssh 13.91.46.9
curl -sSL https://get.docker.com/ | sh

Live - https://aka.ms/projectazplayground
Live - http://az-playground-d1.westus.cloudapp.azure.com
Back up - http://23.99.91.240/



