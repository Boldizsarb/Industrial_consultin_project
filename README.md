# Data Mango Consulting Project

## Documentation

To keep the documentation simple a website has been setup with all the documentation which can be found [here](https://wiki.project-demo-hm.com) with git repository [here](https://github.com/4maynh59/project-documentation).

The project also comes with swagger API documentation, which is available on port 5000.


## Deploying the project

The project is intended to be run through Docker, and each section (front end, back end, and database) includes a Dockerfile responsible for building and deploying them as Docker images. To keep deployment simple, a docker-compose file is provided in the root directory. This file manages the Docker images and can be executed on system startup using the Systemd service file located in the 'server config' directory, it assumes the project will be at the location /home/user/Industrial_consulting_project/.

```bash
cd /home/user/
git clone https://github.com/Boldizsarb/Industrial_consulting_project.git
sudo cp '/home/user/Industrial_consulting_project/server config/run-project.service' /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable run-project.service
sudo systemctl start run-project.service
```

An example production Nginx server configuration that can be adapted to serve the application with HTTPS has also been provided.


## Contributing and issues

Because this is a university project its not open for contributing, however if you find any fundamental flaws or security issues, please open an issue with a description of your findings and feel free to email us at 4maynh59@solent.ac.uk
