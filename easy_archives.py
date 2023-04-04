from shutil import make_archive

#            archive-name  archive-type   input-folder
make_archive('setup',       'zip',        'SETUP')
make_archive('setup', 'gztar', 'SETUP')
make_archive('setup', 'bztar', './SETUP')
make_archive('C:/Users/student/Desktop/setup', 'tar', './SETUP')
