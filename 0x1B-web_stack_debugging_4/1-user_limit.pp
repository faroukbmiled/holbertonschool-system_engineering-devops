# rm usr limit
exec { 'fix':
  command => "/bin/sed -i 's/holberton//g' /etc/security/limits.conf"
}
