# BRIP

**Bing Reverse IP** - bing dork parser :).

#### How it work?
The script use Bing dork "ip:__.__.__.__"  - shows domain names on one IP.

Command line parameters:

	$ python bing.py -h
	
	optional arguments:
	-h, --help		show this help message and exit
	-t, --target		ip address host [ex: 127.0.0.1]
	-r, --results		Bing results, default: 10

Argument **-t** must be used!

Usage:

	$ python bing.py -t 127.0.0.1 -r 50

Output:
	Target: 127.0.0.1

	_____________________________

	http://domain1.com
	http://domain2.com
	http://sub.domain1.com

**Note**: Argument **-r** is not required, but if you want see more results, use **-r >50**
