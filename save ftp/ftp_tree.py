from ftplib import FTP
import os
import time


# returns True, if 'name' is name of a folder, False - if isn't
def folder_q(name):
    return not ('.' in name)


# returns an ftp tree
def ftp_tree(lst, folder='server'):
    tree  = [folder]
    for i in lst:
        if folder_q(i):
            ftp.cwd(i)
            tree.append(ftp_tree(ftp.nlst(), i))
            ftp.cwd('../')
        else:
            tree.append(i)
    return tree


# creates the backup of a server
def backup(ftp, lst, folder='server'):
    print('directory: {0}'.format(folder))  # delete it
    os.mkdir(folder)
    for i in lst:
        if folder_q(i):
            ftp.cwd(i)
            backup(ftp, ftp.nlst(), r'{0}\{1}'.format(folder, i))
            ftp.cwd('../')
        else:
            print('file: {0}'.format(i))  # delete it
            with open(r'{0}\{1}'.format(folder, i), 'wb') as local_file:
                ftp.retrbinary('RETR ' + i, local_file.write)
