#!/usr/bin/env python3

import os
import rdrand

home = os.getenv('HOME')
special = f"{home}/scripts/SpecialEnglishWords"
allwords = "/usr/share/dict/words"

r = rdrand.RdSeedom()
words = open(special).readlines()

print(r.choice(words))
