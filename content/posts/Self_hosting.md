+++
title = "Serving a website from your local computer."
date = "2024-12-30"

[taxonomies]
tags=["documentation"]

[extra]
repo_view = true
comment = true
+++

Serving a website from your local computer.

# Self Hosting? Why?
There are tons of ways you can host a website. In fact if you never host a website in your life that is fine too as there is so many websites out there and no one is going to miss your website.

But none of these means you need a reason for self hosting. Self hosting makes you feel better than whoever that is not self hosting. Thats a good enough reason for me.

# What I used for my my self hosting?
A list of things I used for my self hosting:
- Domain Name from namecheap
- AWS Route 53 Hosted Zone
- EC2 instance for reverse proxy
- Nginx Proxy Manager
- Tailscale
- Portainer
- Docker
- Poetry

## Domain Name from namecheap and AWS Rout53 Hosted Zone. 
You need a Domain Name so people can use it to load your website (i.e. something as lame as combination of your first name and your last name). Then you need a Hosted Zone where you can add DNS records to point your domain to your server.
I used Namecheap for Domain Name and AWS Route 53 for Hosted Zone. 

This takes internet traffic from your domain name to your server. Now, your local server is not exposed to the internet. That's why you're gonna need a reverse proxy. Next section explains that.

## EC2, Nginx Proxy Manager, Tailscale.
I used EC2 instance as for reverse proxy. I needed server application that can take internet traffic and forward it to my local server. I used Nginx Proxy Manager for that. It just gets traffic and for any particular path, it forwards it to the specific IP address and port. Later on you can setup SSL certificates for your domain name usig Nginx Proxy Manager.
It lets you decouple network setup from your simple python server. 

Now time for exposing the local computer port to server. That is portforwarding:
```
sudo iptables -t nat -A PREROUTING -p tcp --dport 8080 -j DNAT --to-destination local_ip:8080
sudo iptables -t nat -A POSTROUTING -j MASQUERADE
```
However, you cannot easily expose your local computer to the internet. You need a VPN. I used Tailscale for that. 
```
sudo tailscale up --auth-key=... --advertise-routes=0.0.0.0/0,::/0 --advertise-exit-node=false
```

Run  computer will make it appear as if it is on the same network as your server.
## Portainer, Docker, and Poetry for managing the server application.
I created a simple python server with Flask. Then I used Docker to containerize it. I used Portainer to manage the Docker containers. Portainer is a web interface for managing Docker containers. You can create containers, start, stop, and delete them. You can also see the logs of the containers. More importnatly you can compose stacks of containers. So for example you can run a database and a web server in the same stack.

For Python package management I used Poetry. Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you. To start a new project with Poetry, you can run:
```
poetry new my_project
```
Then you can add dependencies to your project by running:
```
poetry add requests
```
And you can install the dependencies by running:
``` 
poetry install
```
Poetry also gives you commmand line tools to run your project. For example, you can run your project by running:
```
poetry run python my_project.py
```
The result of all of this is TADDAA  : www.aminehdadsetan.net