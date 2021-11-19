# Ultimate Env

Clone this project and create a .env file in the root directory project with a variable `NGINX_SERVICES` with the format `<service_1>:<service_1_port>,<service_2>:<service_2_port>` to expose those services.

## Example:

`NGINX_SERVICES=myapp:3000,myotherapp:5000`

will expose the services `myapp` and `myotherapp` on the domains `myapp.localhost` and `myotherapp.localhost` respectively pointing to their ports on localhost.

After that just run `docker-compose up` and you should be able to access the services.
