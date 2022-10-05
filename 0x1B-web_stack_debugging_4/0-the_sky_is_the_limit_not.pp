# rm usr limit
exec { 'fix':
  command => 'rm -f /etc/default/nginx && sudo service nginx restart',
  path    => '/usr/local/bin/:/bin/'
}
exec {'fix':
  command  => 'sudo service nginx restart',
  path    => '/usr/local/bin/:/bin/'
}
