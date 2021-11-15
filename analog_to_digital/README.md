To Install the docker file on ubuntu (linux/amd64) you will need to have docker buildx and create a test env using docker buildx build --platform linux/amd64 -t raspian_grovepi:latest . --load
This will take quite some time to build
https://collabnix.com/building-arm-based-docker-images-on-docker-desktop-made-possible-using-buildx/

docker buildx build --platform linux/amd64 -t debian_grovepi -f Dockerfile.debian .  --load

To install the docker image on raspbian simply docker build -t "repo:tag" -f Dockerfile.debian .

To develop files and run them try

docker run -it -v /home/pi/app/grovepi -v "your_abs_path":/home/pi/app/ "repo:tag" sh (or python3 python file)