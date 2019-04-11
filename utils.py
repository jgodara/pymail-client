import errno
import os


def create_file_if_needed(path):
    if not os.path.exists(os.path.dirname(path)):
        try:
            os.makedirs(os.path.dirname(path))
        except OSError as ex:
            if ex.errno != errno.EEXIST:
                raise
