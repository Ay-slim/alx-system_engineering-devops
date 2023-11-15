# Stop 'too many files open' error

exec {'update-file-limit-restart':
  provider => shell,
  command  => 'sudo sed -i "/^#ULIMIT=/{s/^#//}" /etc/default/nginx;sudo service nginx restart'
}
