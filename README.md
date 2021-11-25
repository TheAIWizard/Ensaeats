# EnsaEats


## Installation

EnsaEa is blabal


```shell
pip install fastapi
```

then you need to install

```shell
pip install "uvicorn[standard]"
```

## Usage

EnsaEat has seven endpoints : *clients*, *restaurants*, *commandes*, *restaurateurs*, *blabla*

In order to request one of these endpoints, you can :
- make a curl request
- use your a python script
- use the built-in interface

### curl command

```shell
curl --request GET 'http://127.0.0.1:0000/clients
```

### Python script

```python
import requests

URL = "votre url"

data = ()


res = requests.get(URL, data=data)

```