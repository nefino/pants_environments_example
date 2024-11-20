from unittest import TestCase
import os

class TestEnv(TestCase):
    def test_env_existence(self):
        ENV_NAME="HAS_TO_EXIST"
        DEFAULT_CONTENT="exists"
        self.assertEqual(os.environ.get(ENV_NAME), DEFAULT_CONTENT)
