#!/bin/bash
apt update -y
apt install -y python3-pip nodejs npm git

# Flask
git clone https://github.com/animeshaggarwal27/DevOps-Project.git /opt/flask
pip3 install flask
nohup python3 /opt/flask/app.py &

# Express
mkdir /opt/express
cd /opt/express
npm init -y
npm install express
cat <<EOF > index.js
const express = require('express');
const app = express();
app.get('/', (req,res)=>res.send('Express Running'));
app.listen(3000);
EOF
nohup node index.js &
