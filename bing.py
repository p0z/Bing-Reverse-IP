#!/usr/bin/env python
import requests
import urlparse
import argparse
import re
import os

os.system('clear')

parser = argparse.ArgumentParser(description='Example: %(prog)s -t 127.0.0.1 -r 30', usage='%(prog)s -t `ip address` -r 30')
parser.add_argument("-t", "--target", help='ip address host (ex: 127.0.0.1)')
parser.add_argument("-r", "--results", help='Bing results, default: 10', default='10',type=int)
args = parser.parse_args()

print 
print ' Target: '+str(args.target)
print ' _____________________________'
print

if args.target is None:
	print "Run script option -h"
	os._exit(0)



bing_url = 'http://www.bing.com/search?q=ip%3a'
urls_array = []
count = 0
req2 = ''

while count < args.results:
	url = bing_url+args.target+'&first='+str(count)
	req = requests.get(url, timeout = 3, stream = True)
	req2 += str(req.content)
	count = count+9

hrefs = re.findall('href=[\'"]?([^\'" >]+)', req2)

for href in hrefs:
	if 'http' in href:
		if 'microsoft' not in href:
			parse = urlparse.urlparse(href)
			urls_array.append(parse.scheme+'://'+parse.netloc)

print '\n'.join(set(urls_array))
