import os
import os.path
import pickle
import sys


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
