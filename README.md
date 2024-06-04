# Syndio Test API

## A simple python API

### To run in Docker:

1. Clone the repo
2. From inside the repo folder run `docker build -t syndioapi .` (This takes a while for the first build, but is much faster on subsequent builds thanks to Docker reusing the already-downloaded dependencies)
3. Run `docker run -d --name syndioapi -p $PORT:80 syndioapi`
4. Swagger documentation should now be available at localhost:$PORT/docs


### To run locally directly:

1. Clone the repo
2. From inside the repo folder run `pip3 install -r requirements.txt`
3. Run `fastapi run main.py --port $PORT`
4. Swagger documentation should now be available at localhost:$PORT/docs
