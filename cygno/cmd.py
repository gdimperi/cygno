############# general TOOL for file #############

def mv_file(filein, fileout):
    import os
    command = '/bin/mv '+ filein +' '+ fileout
    return os.system(command)

def cp_file(filein, fileout):
    import os
    command = '/bin/cp '+ filein +' '+ fileout
    return os.system(command)

def rm_file(filein):
    import os
    command = '/bin/rm '+ filein
    return os.system(command)

def grep_file(what, filein):
    import subprocess
    command = '/usr/bin/grep ' + what +' '+filein
    status, output = subprocess.getstatusoutput(command)
    return output

def mkdir_file(folder):
    import os
    command = '/bin/mkdir -p '+ folder
    return os.system(command)


def append2file(line, filein):
    import os
    command = 'echo '+ line + ' >> '+filein
    return os.system(command)

def cache_file(url, cachedir='/tmp/', verbose=False):
    import os
    import sys
    import urllib
    from platform import python_version
    if not os.path.exists(cachedir):
        os.mkdir(cachedir)
    tmpname = cachedir+url.split('/')[-1]
    if not os.path.exists(tmpname):
        if verbose: print("downloading: "+tmpname)
        if python_version().split('.')[0]=='3':
            urllib.request.urlretrieve(url, tmpname, reporthook)
        else:
            urllib.urlretrieve(url, tmpname, reporthook)
    else:
        if verbose: sys.stderr.write('file '+tmpname+' cached')
        
    return tmpname
