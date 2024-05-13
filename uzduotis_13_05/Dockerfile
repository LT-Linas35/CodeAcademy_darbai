FROM nginx:alpine AS pirmas

RUN apk update
RUN apk add git nodejs yarn npm

FROM pirmas AS antras

WORKDIR /
RUN git clone https://github.com/mdn/todo-react.git
WORKDIR /todo-react
RUN npm install
RUN yarn run build

FROM nginx:alpine
COPY --from=antras /todo-react/dist/* /usr/share/nginx/html

