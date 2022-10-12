#!/usr/bin/python
import os

dns_name_check = ('api.github.com')
# dns_name_check= ('127.0.0.1')

os.system('ping -c4 {}'.format(dns_name_check))
