#Set config file
file_line { 'Declaring entity file'
    path => 'etc/ssh/ssh_config',
    line => 'IdentityFile ~/.ssh/holberton',
}
file_line { 'No autentication required'
    path => 'etc/ssh/ssh_config',
    line => 'PasswordAuthentication no',
}
