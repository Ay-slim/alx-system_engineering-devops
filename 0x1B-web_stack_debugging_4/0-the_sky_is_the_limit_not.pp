# Stop 'too many files open' error

exec {'sedstart':
  provider => shell,
  command  => 'sudo sed -i "s/15/4000/" /etc/default/nginx;sudo service nginx restart'
}
