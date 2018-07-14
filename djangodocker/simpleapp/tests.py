from django.test import TestCase

# Create your tests here.
class TestSimpleApp:
    def test_one(self):
        x = "my simple app test"
        assert 'simple app' in x

    def test_fun1(self):
        assert 1 == 1