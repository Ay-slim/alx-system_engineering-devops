# Install flask via pip
package { 'flask':
  ensure   => 'installed',
  name     => 'flask~=2.1.0',
  provider => 'pip3',
}
