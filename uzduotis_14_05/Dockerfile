FROM alpine
RUN apk update
RUN apk add python3 py3-flask
WORKDIR /
COPY uzduotis_14_05/simple_flask_web.py .
CMD python simple_flask_web.py

