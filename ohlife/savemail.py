#!/usr/bin/python27
import sys 
import email
#import html2text
import codecs
from datetime import date
raw_message = ''.join(sys.stdin.readlines())
msg = email.message_from_string(raw_message)
ohlife_filename = '/home/marty/ohlife/' + str(date.today()) + '_ohlife.txt'
ohlife_image = '/home/marty/ohlife/' + str(date.today()) + '_ohlife.png'
#file = open(ohlife_filename, 'a+') 
file = codecs.open(ohlife_filename, 'a+', encoding='utf8') 
for part in msg.walk():
    # each part is a either non-multipart, or another multipart message
    # that contains further parts... Message is organized like a tree
    if part.get_content_type() == 'text/plain':
        #print part.get_payload(decode=True).decode(part.get_content_charset()) # prints the raw text
        file.write(part.get_payload(decode=True).decode(part.get_content_charset())) # prints the raw text
#    elif part.get_content_type() == 'text/html':
#        #print html2text.html2text(part.get_payload(decode=True).decode(part.get_content_charset()))
#        #print part.get_payload(decode=True).decode(part.get_content_charset())
#        file.write(html2text.html2text(part.get_payload(decode=True).decode(part.get_content_charset())))
    elif part.get_content_type() == 'image/png':
        open(ohlife_image, 'wb').write(part.get_payload(decode=True))
file.close()
