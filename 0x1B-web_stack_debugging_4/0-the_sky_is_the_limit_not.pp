# rm usr limit
exec { 'fix':
  command => "/bin/sed -i /etc/default/nginx -e 's/15/4098/'"
}

exec { 'restart nginx':
  command => '/usr/sbin/service nginx restart',
  require => Exec['fix']
}
