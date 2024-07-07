image_name="delivery_db"
docker stop $(docker ps -a --filter ancestor="$image_name" -q) && docker rm $(docker ps -a --filter ancestor="$image_name" -q)
docker rmi "$image_name"
