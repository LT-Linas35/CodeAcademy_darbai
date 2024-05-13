FROM httpd:alpine AS pirmas

RUN apk update
RUN apk add git nodejs yarn npm

FROM pirmas

WORKDIR /usr/local/apache2
RUN git clone https://github.com/mdn/todo-react.git
WORKDIR /usr/local/apache2/todo-react
RUN npm install
RUN yarn run build
RUN cp -R dist/* ../htdocs/

