#bad_version_checker.py

"""
Handcrafted module to check and store OS platform name/Python interpreter
version number for bad_file_copy_thing.py

""" 

import sys 

class VersionError(Exception): 
    """
    Used when a certain component doesn't match the specified version
    number.
    
    """




sys_info = {} # Variable to be returned 
 
def oschecker(os_to_check):  
    """
    Verifies if platform program is being run on is equivalent to
    specified platform 

    Doesn't return sys_info since below function already does

    """
    os_version = sys.platform  

    if os_version == os_to_check: 
        sys_info['system'] = os_to_check 
    else:  
        try:
            raise VersionError
        except VersionError:
            print(f'This program is only compatiable with {os_to_check} systems')
            

def pychecker(x, y, z): 
    """
    
    Verifies if Python interpreter is at least specified version
    
    x = major, y = minor, z = micro, version numbers
    
    """
    py_version = sys.version_info.major, sys.version_info.minor, sys.version_info.micro

    if py_version < (x, y, z):
        try: 
            raise VersionError
        except VersionError:
            print("Please update your Python interpreter.")
    else: 
        sys_info['python_vno_major'] = py_version[0]
        sys_info['python_vno_minor'] = py_version[1]  
        sys_info['python_vno_micro'] = py_version[2]
    return sys_info
 