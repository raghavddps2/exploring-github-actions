from app import addition, multiplication, uniqueInArray
import unittest

class OperationTest(unittest.TestCase):

    def testAddition(self):
        self.assertEqual(addition(2,3,4),9)
        self.assertEqual(addition(2),2)        
        self.assertEqual(addition(),0)
        self.assertEqual(addition(10,20,-9,-1),20)
        self.assertEqual(addition(2,3,4,5),14)

    def testMultiplication(self):
        self.assertEqual(multiplication(2,3,4),24)
        self.assertEqual(multiplication(2),2)        
        self.assertEqual(multiplication(),0)
        self.assertEqual(multiplication(10,20,-9,-1),1800)
        self.assertEqual(multiplication(2,3,4,5),120)

    def testUniqueInArray(self):
        self.assertEqual(uniqueInArray([1,2,3,4,1,2,3,4,5]),5)
        self.assertEqual(uniqueInArray([1,2,3,4,1,2,3,4]),-1)      
        self.assertEqual(uniqueInArray([1,2,3,4,1,2,3,4,5,6,5]),6)  