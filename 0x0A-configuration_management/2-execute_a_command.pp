# Execute ppkill
exec { '/usr/bin/pkill':
  command => ['/usr/bin/pkill', '-g', '-f', 'killmeow'],
}
