# this is to Make passwordAuthentication and add new private key
file_line { 'replace passwordAuthentication':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  replace => true,
  line    => 'PasswordAuthentication no',
  match   => 'PasswordAuthentication yes',
}

file_line { 'add the private key ~/.ssh/school':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
}