FROM nginx:latest

RUN rm /etc/nginx/conf.d/default.conf
#COPY nginx.conf /etc/nginx/nginx.conf
COPY my_nginx.conf /etc/nginx/conf.d/

CMD ["nginx", "-g", "daemon off;"]
