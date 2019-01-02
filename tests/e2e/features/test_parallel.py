import time
from pytest import mark

@mark.parallel
class ParrallelTests:

    def test_parallel_1(self):
        time.sleep(5)
        print('Test 1 finished')

    def test_parallel_2(self):
        time.sleep(5)
        print('Test 2 finished')

    def test_parallel_3(self):
        time.sleep(5)
        print('Test 3 finished')

    def test_parallel_4(self):
        time.sleep(5)
        print('Test 4 finished')