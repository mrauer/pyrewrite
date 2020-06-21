from lib import pyrewrite


class TestPyRewrite:
    """
    Unit tests for PyRewrite.
    """
    def setup(self):
        self.p = pyrewrite.PyRewrite()

    def test_sizeof_fmt_kb(self):
        """Test size returned is in KB."""
        assert self.p.sizeof_fmt(2272) == '2.2KiB'

    def test_sizeof_fmt_mb(self):
        """Test size returned is in MB."""
        assert self.p.sizeof_fmt(121821489) == '116.2MiB'

    def test_get_size_mock_dir(self):
        """Test size of an unexisting dir."""
        path = './mock_dir'
        assert self.p.get_size(path) == '0.0B'
