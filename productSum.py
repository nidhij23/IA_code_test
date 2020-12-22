import unittest


def ProductSum(array):
    return inner_array(array, 1)


def inner_array(array, multiplier):
    sum = 0
    for i in range(len(array)):
        if type(array[i]) is list:
            if i % 2 == 0:
                sum += inner_array(array[i], multiplier * 2)
            else:
                sum += inner_array(array[i], multiplier * 3)
        else:
            sum += array[i] * multiplier
    return sum


class TestSum(unittest.TestCase):

    def test_product_sum(self):
        self.assertEqual(ProductSum([[6, [[[6, 8]]]]]), 348)
        self.assertEqual(ProductSum([2, 4, [3, -4, [2, 3], [5]], [6, [9]], 8]), 161)

    def test_product_sum_empty(self):
        self.assertEqual(ProductSum([]), 0)


if __name__ == "__main__":
    unittest.main()
