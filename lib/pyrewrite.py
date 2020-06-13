import sys


class PyRewrite():

    def __init__(self):
        self.config_path = '/tmp'

    def list_config_file(self):
        """Open and list the config file."""
        print('list config file')
        return 0


if __name__ == "__main__":
    p = PyRewrite()
    """No arvs == help."""
    if len(sys.argv) == 1:
        print('\nAvailable commands:\n'
              '  pyrewrite ls\n'
              '  pyrewrite add <path>\n'
              '  pyrewrite rm <path>\n')
    else:
        if sys.argv[1] == 'ls':
            p.list_config_file()
