"""TestCountry Testcase."""

from masonite.testing import TestCase


class TestCountry(TestCase):

    """All tests by default will run inside of a database transaction."""
    transactions = True

    def setUp(self):
        """Anytime you override the setUp method you must call the setUp method
        on the parent class like below.
        """
        super().setUp()

    def setUpFactories(self):
        """This runs when the test class first starts up.
        This does not run before every test case. Use this method to
        set your database up.
        """
        pass

    def test_has_countries(self):
        """Test to make sure the API return exactly 55 results"""
        self.assertTrue(
            self.json('GET', '/api/countries').count(55)
        )
