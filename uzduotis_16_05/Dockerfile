FROM alpine AS pirmas
RUN apk update
RUN apk add npm
WORKDIR /
COPY CodeAcademyTask /CodeAcademyTask
WORKDIR /CodeAcademyTask
RUN npm install
CMD [ "npm", "run", "dev" ]

