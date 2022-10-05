# rm usr limit
exec { 'fix':
  command => 'rm -f /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# rm usr limit
exec {'fix':
  command  => 'sudo service nginx restart',
  path    => '/usr/local/bin/:/bin/'
}
