# rm usr limit
exec { "fix":
  command => "sed -i 's/holberton//g' /etc/security/limits.conf",
  path    => "/usr/local/bin/:/bin/"
}
