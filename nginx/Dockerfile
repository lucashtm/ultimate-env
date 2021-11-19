FROM nginx
ARG nginx_services
ENV NGINX_SERVICES $nginx_services
COPY generate_config_file.py /generate_config_file.py
COPY nginx.conf /etc/nginx/nginx.conf
RUN apt-get update && apt-get install -y python3
RUN python3 /generate_config_file.py