import os
from string import Template

services = os.environ['NGINX_SERVICES'].split(',')

service_template = '''
server {{
    listen 80;
    server_name {name}.localhost;

    location / {{
        proxy_pass http://localhost:{port};
    }}
}}
'''

final_file = ''
with open('/etc/nginx/nginx.conf', 'r') as f:
    file_template = Template(f.read())
    servers = []
    for service in services:
        name, port = service.split(':')
        servers.append(service_template.format(name=name, port=port))
    final_file = file_template.substitute(services='\n'.join(servers))

with open('/etc/nginx/nginx.conf', 'w') as f:
    f.write(final_file)