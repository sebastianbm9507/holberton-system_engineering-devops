# install puppet lint
package { 'install pupper-lint':
ensure   => '2.1.1',
provider => 'gem'
}
