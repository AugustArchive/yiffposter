# Updates on local machine

$DOCKER_PID=$(docker ps -aqf "name=autoyiffer")
git pull
python3 -m pip install -U -r requirements.txt
docker stop $DOCKER_PID
docker rm $DOCKER_PID
docker build . --no-cache -t autoyiffer:latest
docker run --name autoyiffer -d autoyiffer:latest
