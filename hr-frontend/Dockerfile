# ---------- Build stage ----------
FROM node:20 AS builder

WORKDIR /app
COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

# ---------- Production NGINX ----------
FROM nginx:stable
COPY --from=builder /app/dist/hr-frontend/browser /usr/share/nginx/html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
