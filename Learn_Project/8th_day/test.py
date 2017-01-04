import paramiko, os
import warnings


def ssh_edit_file(h, u, file_in, file_out, key, new):
    """
    SSH_EDIT_FILE - replace a line in a remote file
    """ 

    try:
        s = new.replace("'","\'")
        if file_in == file_out:
            ssh_exe('sed -i "s/.*' + key + '.*/' + s + '/g" ' + file_out,
                    h = h, u = u )
        else:
            ssh_exe('sed -e "s/.*' + key + '.*/' + s + '/g" ' + 
                    file_in + '>|' +  file_out,
                    h = h, u = u )
    except:
        warnings.warn('key not found')

def inplace_change(filename, old_string, new_string):
    try:
        os.path.isfile(filename)
    except IOError:
        logger.warning('file {filename} not found'.format(filename = filename)
    with open(filename, 'r+') as f:
        if old_string not in f.read():
            logger.warning('Key {old_string} not found'.format(old_string = old_string)
        else:
            print 'Changing "{old_string}" to "{new_string}" in {filename}'.format(old_string = old_string, new_string = new_string)
            s = ('sed -i "s/.*' + key + '.*/' + s + '/g" ' + file_out,
                    h = h, u = u )


print "File %s %sexist" % (path, "does not " if ondemand_check else "")
func()