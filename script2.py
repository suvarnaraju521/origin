import script1
import unittest
class sentim(unittest.TestCase):
    def test_add(self):
        s=script1.sample.add(self,20,10)
        print(s)
        self.assertEqual(s,30)
        script1.sample.classmet()
unittest.main()