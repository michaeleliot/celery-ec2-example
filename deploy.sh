# install necessary dependency for ecs-deploy
sudo add-apt-repository ppa:eugenesan/ppa
sudo apt-get update
sudo apt-get install jq -y

# install ecs-deploy
curl https://raw.githubusercontent.com/silinternational/ecs-deploy/master/ecs-deploy | \
  sudo tee -a /usr/bin/ecs-deploy
sudo chmod +x /usr/bin/ecs-deploy

# login AWS ECR
eval $(aws ecr get-login --region us-east-1)

# or login DockerHub
# docker login --username $DOCKER_HUB_USER --password $DOCKER_HUB_PSW

# build the docker image and push to an image repository
docker build -t test
docker tag test:latest $IMAGE_REPO_URL:latest
docker push $IMAGE_REPO_URL:latest

# update an AWS ECS service with the new image
ecs-deploy -c $CLUSTER_NAME -n $SERVICE_NAME -i $IMAGE_REPO_URL:latest