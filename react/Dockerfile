# pull official base image
FROM node:13.12.0-alpine

# set working directory
WORKDIR /usr/src/react/

# add node_modules to $PATH
ENV PATH /react/node_modules/.bin:$PATH

# install app dependencies
COPY package.json .

RUN npm install --silent
RUN npm install react-scripts@3.4.1 -g --silent

# add app
COPY . .

# start app
CMD ["npm", "run", "start"]
