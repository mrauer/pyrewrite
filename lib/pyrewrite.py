import os
import os.path
import pickle
import re
import sys
from fnmatch import filter

from PIL import Image


class PyRewrite():

    def __init__(self):
        self.config_path = '/'.join(
            [os.getenv('HOME'), '.pyrewrite'])

    def check_if_config_file_exists(self):
        """Check if config file exists."""
        return os.path.isfile(self.config_path)

    def load_config(self):
        """Load or create config file."""
        config = {}
        if self.check_if_config_file_exists():
            config = pickle.load(open(self.config_path, 'rb'))
        else:
            pickle.dump(config, open(self.config_path, 'wb'))
        return config

    def set_config_path(self, path):
        """Set the config path."""
        config = self.load_config()
        config['path'] = path
        pickle.dump(config, open(self.config_path, 'wb'))

    def get_images(self):
        """Get .jpg files in path ignoring the case."""
        config = self.load_config()
        return filter(os.listdir(config['path']), '*.[Jj][Pp][Gg]')

    def rename_images(self):
        """Renamed to files in a standard way."""
        updated = 0
        config = self.load_config()
        if 'path' not in config or config == {}:
            sys.exit('Path must be set.')
        _files = self.get_images()
        for file in _files:
            _from = ''.join([config['path'], file])
            _to = ''.join([config['path'], re.sub(
              '[^a-zA-Z0-9\n\\.]', '-', file).lower()])
            if _from != _to:
                print('renaming {}'.format(_from))
                os.rename(_from, _to)
                updated += 1
        return updated, config['path']

    def compress_images(self, quality):
        """Compress the images to a given quality."""
        config = self.load_config()
        if 'path' not in config or config == {}:
            sys.exit('Path must be set.')
        _pre_size = self.get_size(config['path'])
        _files = self.get_images()
        for file in _files:
            fpath = ''.join([config['path'], file])
            print('compressing {}'.format(fpath))
            try:
                Image.open(fpath).save(
                    fpath, quality=int(quality),
                    optimize=True, progressive=True)
            except Exception:
                pass
        _post_size = self.get_size(config['path'])
        return _pre_size, _post_size

    def sizeof_fmt(self, num, suffix='B'):
        """Convert size of directory in readable units."""
        for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
            if abs(num) < 1024.0:
                return "%3.1f%s%s" % (num, unit, suffix)
            num /= 1024.0
        return "%.1f%s%s" % (num, 'Yi', suffix)

    def get_size(self, path):
        """Get the size of a directory."""
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        return self.sizeof_fmt(total_size)


if __name__ == "__main__":
    p = PyRewrite()
    """No argvs == help."""
    if len(sys.argv) == 1:
        print('\nPyRewrite\n'
              '============\n'
              '\n'
              'Available commands:\n'
              '\n'
              '  pyrewrite set <path>\n'
              '  pyrewrite rename\n'
              '  pyrewrite compress <quality>\n'
              '\n'
              'Configuration:\n'
              )
        print('  ' + str(p.load_config()) + '\n')
    else:
        if sys.argv[1] == 'set' and len(sys.argv) == 3:
            p.set_config_path(sys.argv[2])
        elif sys.argv[1] == 'rename' and len(sys.argv) == 2:
            updated, path = p.rename_images()
            print('> {} images renamed in {}'.format(updated, path))
        elif sys.argv[1] == 'compress' and len(sys.argv) == 3:
            pre, post = p.compress_images(sys.argv[2])
            print('> compressed images from {} to {}'.format(pre, post))
