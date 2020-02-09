from ftplib import FTP
import os
import time
import ftp_tree as ft


host = 'your host'
user = 'your user'
passwd = 'your password'

t = 1
while t:
    time.sleep(t)
    date_time = time.asctime()[4:].lower().replace(' ', '-').replace(':', '-')

    ftp = FTP(host)
    ftp.login(user, passwd)
    ft.backup(ftp, ftp.nlst(), date_time)
    ftp.quit()

    print('the {0} backup has been ended'.format(date_time))
    t = 0
