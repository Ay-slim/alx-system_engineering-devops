# Install nginx with puppet

package {'nginx':
  ensure => 'present',
}

exec {'install':
  command  => 'sudo apt-get -y update ; sudo apt-get -y install nginx',
  provider => shell,
}

exec {'Hello World!':
  command  => 'echo "Hello World!" > /var/www/html/index.html',
  provider => shell,
}

exec {'Replace sites available':
  command  => 'sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/www.youtube.com\/watch?v=QH2-TGUlwu4;\\n\\t}/" /etc/nginx/sites-available/default',
  provider => shell,
}

exec {'Replace sites available':
  command  => 'sudo sed -i \"63i "\\\n\tadd_header X-Served-By \"$HOSTNAME\";\"" /etc/nginx/nginx.conf',
  provider => shell,
}

exec {'Restart nginx':
  command  => 'sudo service nginx restart',
  provider => shell,
}
