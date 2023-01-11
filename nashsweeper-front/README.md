# Nashsweeper Front-end
## 0x00 Main Tech Stack
* [Vue.js](https://cn.vuejs.org/): The Progressive
JavaScript Framework to create component with logic and template.
* [TailwindCSS](https://tailwindcss.com/): A utility-first CSS framework packed with classes like flex, pt-4, text-center and rotate-90 that can be composed to build any design, directly in your markup.
* [Axios](https://axios-http.com/): Axios is a simple promise based HTTP client for the browser and node.js. Axios provides a simple to use library in a small package with a very extensible interface.
* [DaisyUI](https://daisyui.com/): daisyUI components Use Tailwind CSS but write fewer class names.
## 0x01 Run this Project
### Install Node.js firstly
You can install Node.js and npm through [https://nodejs.org/en/](https://nodejs.org/en/). In this project, node version must be 18.12.1 and above.
### Install npm dependencies
```shell
# With Taobao Image Acceleration
$ npm config set registry http://registry.npmmirror.com
$ npm install
```
### Run dev and build front-end project
```shell
# dev mode
$ npm run dev
# build the project
$ npm run build
# run the project preview
$ npm run preview
```
## 0x02 Docker Deployment
### Dockerfile(run: npm run build first)
```docker
FROM node:latest
COPY package.json /
RUN npm i --registry=https://registry.npm.taobao.org
RUN npm run build

FROM nginx:latest
# 这里的dist/目录是你的项目打包后的文件目录
COPY ./dist/ /usr/share/nginx/html/
COPY ./nginx.conf /etc/nginx/conf.d/

EXPOSE 80
```
nginx.conf
```nginx
server {
    listen 80 default_server;
    server_name _;

    location / {
      root   /usr/share/nginx/html/web;
      index  index.html index.htm;
      try_files $uri $uri/ /index.html;
    }

    # 接口代理示例
    # location /api {
    #     proxy_pass http://xxx.com;
    #     proxy_set_header Host $host:$server_port;
    #     proxy_set_header X-Real-IP $remote_addr;
        #     proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    #     proxy_set_header Cookie $http_cookie;
    #     proxy_buffering off;
    #     proxy_cache off;
    # }
  }
```