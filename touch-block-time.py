#!/usr/bin/env python

import os
import sys
sys.path.insert(0, os.path.abspath('/usr/local/lib/python3.9/site-packages'))
import time
millis = int(round(time.time() * 1000))
seconds = int(round(time.time()))

import blockcypher

try:
    block_time = blockcypher.get_latest_block_height(coin_symbol='btc')
    block_height = repr(block_time)
    f = open("BLOCK_TIME", "w")
    f.write("" + block_height + "\n")
    f.close()
except:
    block_time = 0
    pass



