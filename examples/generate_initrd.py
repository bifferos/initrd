#!/usr/bin/env python

import initrd
initrd.gen_init_cpio("initrd.spec", "newinitrd.img", "gzip")
