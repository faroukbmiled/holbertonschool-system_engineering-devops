# changes the configuration file using puppet
file_line { 'Identity file':
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
}
file_line { 'no password':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}
