# Build React static files
FROM node:13.12.0-alpine as build

WORKDIR /code
COPY ./package.json ./
COPY ./package-lock.json ./
RUN npm ci --silent
COPY ./frontend/ ./
RUN npm run build

# Copy React static files and start nginx
FROM nginx:stable-alpine
COPY --from=build /app/frontend/build /usr/share/nginx/html
CMD ["nginx", "-g", "daemon off;"]