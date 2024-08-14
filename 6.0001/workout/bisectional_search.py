import unittest

def bisectional_search(L, e):
    def bisectional_search_helper(L,e,low,  high):
        if low == high:
            return L[low] == e
        mid = (low+ high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e :
            if low == mid : # nothing left to return
                return False
            else:
                return bisectional_search_helper(L,e,low,mid-1)
        else:
            return bisectional_search_helper(L,e,mid+1,high)
    if len(L)==0:
        return False
    else :
        return bisectional_search_helper(L,e,0,len(L)-1)

class TestBisectionalSearch(unittest.TestCase):
    def test_element_found(self):
        self.assertTrue(bisectional_search([1, 2, 3, 4, 5], 3))
        self.assertTrue(bisectional_search([1, 2, 3, 4, 5, 6], 6))
        self.assertTrue(bisectional_search([1], 1))
        self.assertTrue(bisectional_search([i for i in range(10000,20001,2)], 15000))

    def test_element_not_found(self):
        self.assertFalse(bisectional_search([1, 2, 3, 4, 5], 0))
        self.assertFalse(bisectional_search([1, 2, 3, 4, 5], 6))
        self.assertFalse(bisectional_search([], 1))
        self.assertFalse(bisectional_search([i for i in range(10000,20001,2)], 15001))

    def test_empty_list(self):
        self.assertFalse(bisectional_search([], 10))

    def test_single_element_list(self):
        self.assertTrue(bisectional_search([2], 2))
        self.assertFalse(bisectional_search([2], 3))

if __name__ == '__main__':
    unittest.main()