#!/usr/bin/env python

import sys
import ConfigParser

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = 'config.ini'
    
oconfig = ConfigParser.RawConfigParser()
oconfig.read(filename)

# This write will destroy the configuration if there's a crash while
# writing the output.  We're in an SVN-controlled directory, so
# I didn't care enough to fix this.
fd = open(filename, 'wb')
def write():
    # Copy of write() code that sorts output by section
    if oconfig._defaults:
        fd.write("[%s]\n" % DEFAULTSECT)
        for (key, value) in oconfig._defaults.items():
            fd.write("%s = %s\n" % (key, str(value).replace('\n', '\n\t')))
        fd.write("\n")
    
    for section in sorted(oconfig._sections):
        fd.write("[%s]\n" % section)
        for (key, value) in oconfig._sections[section].items():
            if key != "__name__":
                fd.write("%s = %s\n" %
                         (key, str(value).replace('\n', '\n\t')))
        fd.write("\n")

write()

fd.close()
