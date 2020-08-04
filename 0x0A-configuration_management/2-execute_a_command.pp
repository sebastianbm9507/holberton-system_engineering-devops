#Using Puppet, create a manifest that kills a process named killmenow.
exec { 'process killmenow':
    path    => '/usr/bin/',
    command => 'pkill -f killmenow',
}
