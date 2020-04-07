'''
This is the test case file for python_tester. The purpose of this file is to help
create Python output value and dtype test cases for user programs.
'''

from bcolors import bcolors
bc = bcolors()

class TestCase(object):
    def __init__(self, test_id, func, expected_value):
        self.id = test_id
        self.func = func
        self.input_value = None
        self.input_value_type = None
        self.output_value = None
        self.expected_value = expected_value
        self.expected_value_type = type(self.expected_value)

    def bond_value(self, bc, value):
        try:
            self.input_value = value
            self.input_value_type = type(self.input_value)
            bc.cprint(bc.OKBLUE, "Test Case {} successfully bonded to value at mem address {}"
                    .format(self.id, hex(id(self.input_value))))
        except:
            bc.cprint(bc.FAIL, "Error: missing input value")

    def evaluate(self):
        ret_val = False
        self.output_value = self.func(self.input_value)

        if self.output_value == self.expected_value:
            bc.cprint(bc.OKGREEN, "Successfully passed Test Case {}".format(self.id))
            ret_val = True
        else:
            bc.cprint(bc.FAIL, "Error: Did not pass Test Case {} due to varying values: {} vs {}"
                    .format(self.id, self.output_value, self.expected_value))

        return ret_val

class TestCases(object):
    def __init__(self):
        self.test_counter = 0
        self.test_array = []
        self.total_score = 0
        bc.cprint(bc.OKGREEN, "Sucessfully initialized test cases")

    '''
    Adding a test case requires three different parameters: The python function to evaluate, 
    the input value, and the expected output value. Reason for this is so that we can 
    evaluate the correctness of the function by doing the function calls on the input value
    on the spot and evaluate that output value to the expected output value
    '''
    def add_testcase(self, func, input_value, expected_value):
        self.test_counter += 1
        new_tc = TestCase(self.test_counter, func, expected_value)
        new_tc.bond_value(bc, input_value)
        self.test_array.append(new_tc)

    def evaluate_tests(self):
        bc.cprint(bc.OKBLUE, "Now evaluating all test cases")
        for t in self.test_array:
            eval_val = t.evaluate()

            if eval_val == True:
                self.total_score += 1

        print("Total Score: %.1f/%.1f" % (self.total_score, len(self.test_array)))

if __name__ == '__main__':
    TestCases()
