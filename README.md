# EnsaEats

<img src="./EnsaEats.png">

EnsaEats is an app developed by student for the students which aims to connect the restorers and their clients. It's an academic project aiming at teaching the second-year student at ENSAI how to design their own API using Python. 

EnsaEats was originally meant to run locally on student's own computer for a pure academic purpose.
In this repo, the project is powered by Docker, Kubernetes and Helm to be deployed online and be more scalable and customizable.

## Installation

If you want to install the app locally, you need to clone the project (for example):

```shell 
git clone https://github.com/TheAIWizard/Ensaeats.git
``` 

Then, on your terminal, you need to load 

```shell 
pip install -r requirements.txt
```

to get all the needed dependencies

## Usage

EnsaEat has seven endpoints : */clients/*, */restaurants/*, */commandes/*, */restaurateurs/*, */article/*, */menus/*

In order to request one of these endpoints, you can :
- make a curl request
- use your a python script (requests library for instance)
- use the built-in interface

Tip: using the built-in interface will help you to get the accurate curl request

### Access the API (FOR RESTORERS): launch the built-in interface locally 

Execute the start_api.py file in the project root:

```shell 
python start_api.py
```
In this file, choose the appropriate port (default:80 but 5000 works too)

go to your favourite browser and type : 'localhost:port/docs' --> example : 'localhost:80/docs'


### Acces the UI (FOR CLIENTS): launch the interface locally (views)

```shell 
python start_client.py
```
execute the start_client.py file on on terminal and start_api.py on another one

### Deploy the built-in API and interface on a remote cloud from any laptop

The API and UI are deployed on the SSP Cloud (an instance of the open source project Onyxia developed by the DIIT team from The National Institute of Statistics and Economic Studie) powered by a Kubernetes cluster.

If you have a kubernetes cluster and a domain host, you can choose the DNS in the ingress.yaml file
(kubernetes approach)

(Helm still to come)

Access the API developed by the students for the project: you can go to your favourite browser and type https://ensaeats-api.lab.sspcloud.fr/docs 

Access the UI: (still to come)