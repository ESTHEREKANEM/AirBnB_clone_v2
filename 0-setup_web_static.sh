#!usr/bin/env bash
#The following script set ups webservers for deployment of web static

while ! [ -x "$(command -v nginx)" ]; do
  sudo apt-get update
  sudo apt-get install nginx -y
done
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# Creating a fake HTML file
echo "<html><head><title>Test Page</title></head><body><p>This is a test page.</p></body></html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

config="server {
    listen 80;
    listen [::]:80;
    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html;
    }
}"
sudo echo "$config" | sudo tee /etc/nginx/sites-available/default > /dev/null
sudo service nginx restart
