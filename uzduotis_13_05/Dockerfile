FROM nginx:alpine AS pirmas
RUN apk update
RUN apk add git yarn nodejs
FROM pirmas AS antras
WORKDIR /
RUN git clone https://github.com/mdn/todo-react.git
WORKDIR /todo-react
RUN yarn install
RUN yarn run build
FROM nginx:alpine
RUN rm -R /usr/share/nginx/html/*
COPY --from=antras /todo-react/dist/* /usr/share/nginx/html

