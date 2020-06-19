import os
import os.path
import pickle
import re
import sys
from fnmatch import filter


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

    def get_files(self):
        """Get .jpg files in path ignoring the case."""
        config = self.load_config()
        return filter(os.listdir(config['path']), '*.[Jj][Pp][Gg]')

    def rename_files(self):
        """Renamed to files in a standard way."""
        updated = 0
        config = self.load_config()
        if 'path' not in config or config == {}:
            sys.exit('Path must be set.')
        _files = self.get_files()
        for file in _files:
            _from = ''.join([config['path'], file])
            _to = ''.join([config['path'], re.sub(
              '[^a-zA-Z0-9\n\\.]', '-', file).lower()])
            if _from != _to:
                print('renaming {}'.format(_from))
                os.rename(_from, _to)
                updated += 1
        return updated, config['path']


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
              '\n'
              'Configuration:\n'
              )
        print('  ' + str(p.load_config()) + '\n')
    else:
        if sys.argv[1] == 'set' and len(sys.argv) == 3:
            p.set_config_path(sys.argv[2])
        elif sys.argv[1] == 'rename' and len(sys.argv) == 2:
            updated, path = p.rename_files()
            print('> {} files renamed in {}'.format(updated, path))
