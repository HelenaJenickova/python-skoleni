
https://www.youtube.com/watch?v=NqO59tkgmpk&list=PLTCx5oiCrIJ5DNsAC3_gkRGfQudzv1DtZ

import unittest

def arabske_na_rimske(ar):
    ar_na_rim = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
    if ar in ar_na_rim:
        return ar_na_rim[ar]
    for key in ar_na_rim:
        if ar == (key +1) :
            return ar_na_rim[ar-1] + "I"
        
    for key in ar_na_rim:
        if ar == (key +2) :
            return ar_na_rim[ar-2] + "II"
        

    if ar == 1 + 1:
        return "II"
    if ar == 6:
        return "VI"
    if ar == 11:
        return "XI"
    if ar == 51:
        return "LI"
    if ar == 101:
        return "CI"
    if ar == 501:
        return "DI"
    if ar == 1001:
        return "MI"

class TestArabskeNaRimske(unittest.TestCase):
    def test_basic_plus_two(self):
        self.assertEqual(arabske_na_rimske(3), "III")
        self.assertEqual(arabske_na_rimske(7), "VII")
        self.assertEqual(arabske_na_rimske(12), "XII")
        self.assertEqual(arabske_na_rimske(52), "LII")
        self.assertEqual(arabske_na_rimske(102), "CII")
        self.assertEqual(arabske_na_rimske(502), "DII")
        self.assertEqual(arabske_na_rimske(1002), "MII")    

class TestArabskeNaRimske(unittest.TestCase):
    def test_basic_plus_one(self):
        self.assertEqual(arabske_na_rimske(2), "II")
        self.assertEqual(arabske_na_rimske(6), "VI")
        self.assertEqual(arabske_na_rimske(11), "XI")
        self.assertEqual(arabske_na_rimske(51), "LI")
        self.assertEqual(arabske_na_rimske(101), "CI")
        self.assertEqual(arabske_na_rimske(501), "DI")
        self.assertEqual(arabske_na_rimske(1001), "MI")

    def test_basic(self):
        self.assertEqual(arabske_na_rimske(1), "I")
        self.assertEqual(arabske_na_rimske(5), "V")
        self.assertEqual(arabske_na_rimske(10), "X")
        self.assertEqual(arabske_na_rimske(50), "L")
        self.assertEqual(arabske_na_rimske(100), "C")
        self.assertEqual(arabske_na_rimske(500), "D")
        self.assertEqual(arabske_na_rimske(1000), "M")