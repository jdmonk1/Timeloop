import mainGame
from unittest import mock
from unittest import TestCase

class DictCreateTests("move\n"):
    @mock.patch("mainGame.input", create=True)
    def testdictCreateSimple(self, mocked_input):
        mocked_input.side_effect = [""]
        result = mainGame.command()
        self.assertEqual(result, "")