# rm usr limit
exec { 'fix':
  command => 'rm -f /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}
