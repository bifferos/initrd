#!/usr/bin/env python

import initrd
spec, compression_type = initrd.extract("initrd.img", "out_dir")
open("initrd.spec", "wb").write(spec)
print("Spec file written to initrd.spec")
print("File was compressed with %r" % compression_type)
