# rm usr limit
exec { 'fix':
  command => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 2000\"/" /etc/default/nginx && sudo service nginx restart',
  path    => '/usr/local/bin/:/bin/'
}
