from typing import List
from solution import Solution

class Test:
    def run(self, case=None):
        tests = [
            [[1,3],[2],2.00000],
            [[1,2],[3,4],2.50],
            [[1,3],[2,7],2.50],
            [[1,2,3,4,5],[6,7,8,9,10,11,12,13,14,15,16,17],9]
        ]
        solution = Solution()
        if case==None:
            for test in tests:
                p1,p2,p3 = test
                print(f'Test : {p1,p2}')
                res = solution.findMedianSortedArrays(p1,p2)
                print(f'{"PASS" if res==p3 else "FAIL"}\n\n')
        else:
            test = tests[case]
            p1,p2,p3 = test
            print(f'Test : {p1,p2}\n{"-"*16}')
            res = solution.findMedianSortedArrays(p1,p2)
            print(f'res:{res:>10}\nexp:{p3:>10}\n{"-"*16}\n{"PASS" if res==p3 else "FAIL"}\n\n')


test = Test()
test.run()