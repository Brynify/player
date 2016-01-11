from setuptools import setup, find_packages
from glob import glob
from distutils.core import setup
import py2exe
def get_data():
 import accessible_output2
 import sound_lib
 return [
    ("requests", ["cacert.pem"]),
  ("accessible_output2/lib", glob("accessible_output2/lib/*.dll")),
]+sound_lib.find_datafiles()+accessible_output2.find_datafiles()

setup(windows=['pytest.py'],packages= find_packages(), options = {
   'py2exe': {   
    'optimize':2,
   'packages': ["dbhash"],
    'dll_excludes': ["MPR.dll", "api-ms-win-core-apiquery-l1-1-0.dll", "api-ms-win-core-console-l1-1-0.dll", "api-ms-win-core-delayload-l1-1-1.dll", "api-ms-win-core-errorhandling-l1-1-1.dll", "api-ms-win-core-file-l1-2-0.dll", "api-ms-win-core-handle-l1-1-0.dll", "api-ms-win-core-heap-obsolete-l1-1-0.dll", "api-ms-win-core-libraryloader-l1-1-1.dll", "api-ms-win-core-localization-l1-2-0.dll", "api-ms-win-core-processenvironment-l1-2-0.dll", "api-ms-win-core-processthreads-l1-1-1.dll", "api-ms-win-core-profile-l1-1-0.dll", "api-ms-win-core-registry-l1-1-0.dll", "api-ms-win-core-synch-l1-2-0.dll", "api-ms-win-core-sysinfo-l1-2-0.dll", "api-ms-win-security-base-l1-2-0.dll", "api-ms-win-core-heap-l1-2-0.dll", "api-ms-win-core-interlocked-l1-2-0.dll", "api-ms-win-core-localization-obsolete-l1-1-0.dll", "api-ms-win-core-string-l1-1-0.dll", "api-ms-win-core-string-obsolete-l1-1-0.dll", "WLDAP32.dll", "MSVCP90.dll", "CRYPT32.dll", "mfc90.dll"],
    'skip_archive': True
   },
  })