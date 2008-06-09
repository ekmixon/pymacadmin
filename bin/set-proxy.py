#!/usr/bin/python
# encoding: utf-8
"""
%prog --enable --protocol=HTTP --server=proxy.example.edu --port=3128

Configures the system proxy settings from the command-line using the pyMacAdmin PMASystemConfiguration module
"""

from socket import gethostbyname, gaierror
import sys
from PyMacAdmin.SCUtilities.SCPreferences import SCPreferences

def main():
  sc_prefs = SCPreferences()
  
  from optparse import OptionParser
  parser = OptionParser(__doc__.strip())
  parser.add_option('--enable',   dest='enable', action="store_true",               help='Enable proxy for the specified protocol', default=True)
  parser.add_option('--disable',  dest='enable', action='store_false',              help='Disable proxy for the specified protocol')
  parser.add_option('--protocol', choices=sc_prefs.proxy_protocols, metavar='PROTOCOL',   help='Specify the protocol (%s)' % ", ".join(sc_prefs.proxy_protocols))
  parser.add_option('--server',   metavar='SERVER',                                 help="Specify the proxy server's hostname")
  parser.add_option('--port',     type='int', metavar='PORT',                       help="Specify the proxy server's port")
  (options, args) = parser.parse_args()

  # optparser inexplicably lacks a require option due to extreme
  # pedanticism but it's not worth switching to argparse:
  if not options.protocol:
    print >>sys.stderr, "ERROR: You must specify a protocol to %s" % ("enable" if options.enable else "disable")
    sys.exit(1)
    
  if options.enable and (not options.server or not options.port):
    print >>sys.stderr, "ERROR: You must specify a %s proxy server and port" % options.protocol
    sys.exit(1)
  
  try:
    host_test = gethostbyname(options.server)
  except gaierror, e:
    print >>sys.stderr, "ERROR: couldn't resolve server hostname %s: %s" % (options.server, e.args[1]) # e.message is broken in the standard socket.gaierror!
    sys.exit(1)    

  try:
    sc_prefs.set_proxy(enable=options.enable, protocol=options.protocol, server=options.server, port=options.port)
    sc_prefs.save()
  except RuntimeError, e:
    print >>sys.stderr, e.message

if __name__ == '__main__':
  main()