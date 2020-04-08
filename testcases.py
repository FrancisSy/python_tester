'''
This is the test case file for python_tester. The purpose of this file is to help
create Python output value and dtype test cases for user programs.
'''

from bcolors import bcolors
bc = bcolors() # global colors object

'''
This is the Test Case class. This holdes the test case's id, the function call, the 
input value it is bonded to, the expected value that the function outputs based on
the input value, and the types of both data values.
'''
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
            bc.cprint(bc.FAIL, "Check function or expected value")
        return ret_val

    '''
    Function to display test information. This would be the function, input value, expected value, 
    and value types and addresses.
    '''
    def display_test_info(self):
        pass
       
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
    
    '''
    Evaluate the tests stored in the array
    '''
    def evaluate_tests(self):
        bc.cprint(bc.OKBLUE, "Now evaluating all test cases")
        for t in self.test_array:
            eval_val = t.evaluate()

            if eval_val == True:
                self.total_score += 1

        score = self.total_score/len(self.test_array)
        if score == 1.0:
            bc.cprint(bc.OKGREEN, "Total Score: %.1f/%.1f" % (self.total_score, len(self.test_array)))
        elif score == 0.0:
            bc.cprint(bc.FAIL, "Total Score: %.1f/%.1f" % (self.total_score, len(self.test_array)))
        else:
            bc.cprint(bc.WARNING, "Total Score: %.1f/%.1f" % (self.total_score, len(self.test_array)))


if __name__ == '__main__':
    TestCases()
