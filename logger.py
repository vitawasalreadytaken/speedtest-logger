#!/usr/bin/env python3

import datetime
import os
import subprocess
import sys
import time



def run(args, output_file):
	with open(output_file, 'a') as output:
		subprocess.run(('speedtest-cli',) + args, check = True, stdout = output)


if __name__ == '__main__':
	output_file = sys.argv[1]
	interval = int(sys.argv[2])

	if not os.path.exists(output_file):
		print(f'{output_file} does not exist, creating...')
		run(('--csv-header',), output_file)

	while True:
		print(datetime.datetime.now(), 'starting speed test...')
		run(('--csv',), output_file)
		print(datetime.datetime.now(), f'done, sleeping for {interval} seconds...')
		time.sleep(interval)
