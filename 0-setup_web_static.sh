#!/usr/bin/env bash
# Install nginx to prepare a server
dpkg -s nginx &> /dev/null
if [ $? -ne 0 ]
then
    sudo apt-get update
    sudo apt-get -y install nginx
fi
if [ ! -d "/data" ]
then
    mkdir /data/
fi
if [ ! -d "/data/web_static/" ]
then
    mkdir /data/web_static/
fi
if [ ! -d "/data/web_static/releases/" ]
then
    mkdir /data/web_static/releases/
fi
if [ ! -d "/data/web_static/shared/" ]
then
    mkdir /data/web_static/shared/
fi
if [ ! -d "/data/web_static/releases/test/" ]
then
    mkdir /data/web_static/releases/test/
fi

echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>" > data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu /data
sudo chgrp -R ubuntu /data

if ! grep -q hbnb_static /etc/nginx/sites-available/default
then
    sed -i '/:80 default_server/a\\n\tlocation /hbnb_static/ {\n\t\talias \/data\/web_static\/current\/;\n\t}' /etc/nginx/sites-available/default
fi

service nginx restart
