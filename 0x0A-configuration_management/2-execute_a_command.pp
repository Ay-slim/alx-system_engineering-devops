# Execute ppkill
exec { '/usr/bin/pkill':
  command => ['/usr/bin/pkill', 'killmeow'],
}
