from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self):
        self.__testCases = {1: (6, [11,6], 3), 2: (7, [15,10,10], 5), 3: (1, [100000], 100000)}
        self.__obj = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_Case1(self):
        n, quantities, output = self.__testCases[1]
        result = self.__obj.minimizedMaximum(n = n, quantities = quantities)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case2(self):
        n, quantities, output = self.__testCases[2]
        result = self.__obj.minimizedMaximum(n = n, quantities = quantities)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

    @timeout(0.5)
    def test_Case3(self):
        n, quantities, output = self.__testCases[3]
        result = self.__obj.minimizedMaximum(n = n, quantities = quantities)
        self.assertIsInstance(result, int)
        self.assertEqual(result, output)

if __name__ == '__main__': unittest.main()