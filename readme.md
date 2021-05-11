[![codecov](https://codecov.io/gh/chawil/api-even/branch/master/graph/badge.svg?token=CSHFDGGO8A)](https://codecov.io/gh/chawil/api-even)

# api-even

API to know if a number is odd or even

## Docker

```bash
# to run container
docker run -p 5000:5000 --rm -d api-even/latest
```

## dev

```bash
# to install nodemon
npm install --global nodemon

# command to "hotreload" the web page when the code changes
nodemon -e py -x python main.py

# -e for extensions
# -x for the command

# to run server
python main.py

# to test
python tests.py

```

## Setup deployment.yml

```bash
3 secrets :
- container registry name : Settings > Access Keys 
- container registry password : Settings > Access Keys 
- kubeconfig cluster aks : az aks get-credentials --resource-group <RESOURCE GROUP NAME> --name <CLUSTER NAME> --file <OUTPUT FILE>
```
