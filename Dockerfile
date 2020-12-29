FROM node:latest-alpine

LABEL MAINTAINER="August <august@augu.dev>"
COPY . .
RUN npm ci
RUN npm run build

CMD ["node", "build/index.js"]
