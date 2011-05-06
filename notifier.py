#!/usr/loca/bin/ python
import yaml
from datetime import datetime
import imaplib
import urllib

config = yaml.load(file(config.yaml, 'r'))
con = imaplib.IMAP4_SSL(config['imap_add'], config['imap_port'])
con.login(config['imap_email'], config['imap_pwd'])
con.select(config['imap_folder'])
typ, data = con.search(None, 'UNSEEN')
print '%s: Looking for some emails, bro.\n' % (datetime.today())
for num in data[0].split():
    typ, data = con.fetch(num, '(RFC822)')
    for n in data[0][1].split('\r\n'):
        if n[:5] == 'From:':
            email = n.split(':')[1]
            url = 'http://api.tropo.com/1.0/sessions?action=create&token=%s&to=%s&msg=%s' % (config['tropo_token'], config['phone'], email)
            urllib.urlopen(url)
            print '%s: Got one, bro (%s).\n' % (datetime.today(), email)

con.close()
con.logout()

