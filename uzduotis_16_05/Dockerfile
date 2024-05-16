FROM alpine AS pirmas
RUN apk update
RUN apk add yarn
WORKDIR /
COPY CodeAcademyTask /CodeAcademyTask
WORKDIR /CodeAcademyTask
RUN yarn install && yarn test
CMD [ "yarn", "run", "dev" ]

