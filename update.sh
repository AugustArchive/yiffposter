# Updates on local machine

DOCKER_PID=$(echo $(docker ps -aqf name="autoyiffer") | sed 's/\=//')
git pull
python3 -m pip install -U -r requirements.txt
docker stop $DOCKER_PID
docker rm $DOCKER_PID
docker build . --no-cache -t autoyiffer:latest
docker run --name autoyiffer -d autoyiffer:latest
