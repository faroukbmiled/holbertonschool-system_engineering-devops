# rm usr limit
exec { 'fix':
  command => "/bin/sed -i 's/holberton/none/g' /etc/security/limits.conf"
}

exec { 'fix2':
  command => "/bin/sed -i 's/holberton/none/g' /etc/security/limits.conf",
  require => Exec['fix']
}
