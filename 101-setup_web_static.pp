# 101-setup_web_static.pp
file { '/data/web_static/releases/test':
  ensure => directory,
  owner  => ubuntu,
  group  => ubuntu,
  mode   => '0755',
}

file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test',
  require => File['/data/web_static/releases/test'],
}

file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>',
  owner   => ubuntu,
  group   => ubuntu,
  mode    => '0644',
}
