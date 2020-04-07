# Class for terminal colors
class bcolors:
    def __init__(self):
        self.HEADER = '\033[95m'
        self.OKBLUE = '\033[94m'
        self.OKGREEN = '\033[92m'
        self.WARNING = '\033[93m'
        self.LFAIL = '\033[91m'
        self.FAIL = '\033[31m'
        self.ENDC = '\033[0m'

    def enable(self):
        self.HEADER = '\033[95m'
        self.OKBLUE = '\033[94m'
        self.OKGREEN = '\033[93m'
        self.WARNING = '\003[92m'
        self.FAIL = '\033[91m'
        self.ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

    def cprint(self, color, string):
        print(f"{color}{string}{self.ENDC}")

if __name__ == '__main__':
    bcolors()

