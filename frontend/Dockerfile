FROM node
USER root


RUN apt-get update 
RUN apt-get -y install locales && localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

# ENV TZ Asia/Tokyo
# ENV LANG ja_JP.UTF-8
# ENV LANGUAGE ja_JP:ja
# ENV LC_ALL ja_JP.UTF-8

WORKDIR /app

RUN npm create vite@latest frontend -y -- --template svelte
WORKDIR /app/frontend

RUN npm install
# https://fitech101.aalto.fi/web-software-development/24-introduction-to-svelte/6-svelte-in-a-container/
# viteは設定を変えないとDockerで動かない
COPY ./frontend/copys/vite.config.js /app/frontend/
COPY ./frontend/App.svelte /app/frontend/src/

EXPOSE 5173

ENTRYPOINT [ "npm" ,"run" ,"dev" ] 

