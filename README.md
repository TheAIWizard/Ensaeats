# EnsaEats

<img src="./EnsaEats.png">

## Installation

EnsaEats is an app developed by student for the students which aims to connect the restorers and their clients


you need to load 

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

### FOR RESTORERS: launch the built-in interface locally 

```shell 
python
```
execute the start_api.py file 

choose the appropriate port (default:80 but on VM 5000 works too)

go to your favourite browser and tap : 'localhost:port/docs' --> example : 'localhost:80/docs'


### FOR CLIENTS: launch the interface locally (views)

```shell 
python
```
execute the start_client.py file on on terminal and start_api.py on another one

### Still to come: launch the built-in interface on a remote cloud from any laptop (still need privilege to access the ENSAI Network)

go to your favourite browser and write : https ://oyooou.deta.dev/docs

```shell 
deta
```

to connect : executes deta login

the files main.py and the folder deta are used to deploy the app on a remote cloud