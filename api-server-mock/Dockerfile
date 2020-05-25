FROM node:current-alpine

WORKDIR /data

RUN npm install -g json-server

ENTRYPOINT ["json-server", "--watch", "/data/db.json", "-H", "0.0.0.0"]