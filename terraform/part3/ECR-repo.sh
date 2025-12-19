docker build -t flask .
docker tag flask:latest <account>.dkr.ecr.ap-south-1.amazonaws.com/flask
docker push <account>.dkr.ecr.ap-south-1.amazonaws.com/flask
