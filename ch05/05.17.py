#! /usr/bin/env python

import random

N = random.randint(1, 100)
Nc = random.randint(1, N)
src = [random.uniform(1, 2e10) for x in xrange(N)]
csrc = [random.choice(src) for x in xrange(Nc)]
csrc.sort()

print N, src, Nc, csrc