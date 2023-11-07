FROM node:lts-slim

WORKDIR /app

# COPY ["package.json", "package-lock.json*", "./"]
COPY . .

RUN npm install
# RUN npm install --registry=http://registry.npmmirror.com

RUN npm run build

EXPOSE 4173

CMD npm run preview
