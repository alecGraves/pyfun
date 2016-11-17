
'''This module is used to generate WhiteSpace code.'''
class WhiteSpace(object):
    '''This class can be used to generate whitespace code'''
    def __init__(self, explain=True):
        self.string = ""
        self.explain = explain
    def __str__(self):
        '''how to print the object the whitespace code'''
        return self.string
    def __add__(self, other):
        '''join together two pieces of whitespace code'''
        return self.string.replace("\n\n\n", "") + other.string
    def number(self, num):
        '''
        add a number to the code
        Many commands require numbers or labels as parameters. Numbers
            can be any number of bits wide, and are simply represented as
            a series of [Space] and [Tab],terminated by a [LF].
        [Space] represents the binary digit 0, [Tab] represents 1.
        The sign of a number is given by its first character,
            [Space] for positive and [Tab] for negative.
        Note that this is not twos complement, it just indicates a sign.
        Labels are simply [LF] terminated lists of spaces and tabs.
        There is only one global namespace so all labels must be unique.
        '''
        if self.explain:
            return ('num_{0}'.format(num) +
                    '{0:b}'.format(num).replace('0', ' ').replace('1', '\t') + '\n')
        return '{0:b}'.format(num).replace('0', ' ').replace('1', '\t') + '\n'
    def write(self, string):
        '''add new item to the whitespace program'''
        self.string += string

#Stack manipulation commands:
    def stack_manip(self):
        '''Instruction modification parameter (IMP) stack manipulation'''
        if self.explain:
            self.write("IMP:stack_manip")
        self.write(" ")
    def push(self, num):
        '''push a num to the stack'''
        self.stack_manip()
        if self.explain:
            self.write("push")
        self.write(" " + self.number(num))
    def dupl(self):
        '''duplicate the top item on the stack'''
        self.stack_manip()
        if self.explain:
            self.write("dupliate_top")
        self.write("\n ")
    def swap(self):
        '''swap the top swo items in the stack'''
        self.stack_manip()
        if self.explain:
            self.write("swap_top_two")
        self.write("\n\t")
    def dis(self):
        '''discard the top item int the swap'''
        self.stack_manip()
        if self.explain:
            self.write("discard_top")
        self.write("\n\n")

#Arithmetic commands:
    def arith(self):
        '''
        IMP: Arithmetic
        Arithmetic commands operate on the top two items on the stack,
        and replace them with the result of the operation.
        The first item pushed is considered to be left of the operator.
        '''
        if self.explain:
            self.write("IMP:arithmetic")
        self.write("\t ")
    def add(self):
        '''add top of stack'''
        self.arith()
        if self.explain:
            self.write("add")
        self.write("  ")
    def sub(self):
        '''sub top of stack'''
        self.arith()
        if self.explain:
            self.write("sub")
        self.write(" \t")
    def mult(self):
        '''mult top of stack'''
        self.arith()
        if self.explain:
            self.write("mult")
        self.write(" \n")
    def div(self):
        '''intiger division on top of stack'''
        self.arith()
        if self.explain:
            self.write("div")
        self.write("\t ")
    def mod(self):
        '''modulo on top of stack'''
        self.arith()
        if self.explain:
            self.write("mod")
        self.write("\t\t")

# Heap access commands:
    def heap(self):
        '''
        IMP: Heap Access
        Heap access commands look at the stack to find the
        address of items to be stored or retrieved. To store
        an item, push the address then the value and run the store command.
        To retrieve an item, push the address and run the retrieve command,
        which will place the value stored in the location
        at the top of the stack.
        '''
        if self.explain:
            self.write("heap_access")
        self.write("\t\t")
    def store(self):
        '''
        push an address then a val and run this command to store it
        '''
        self.heap()
        if self.explain:
            self.write("store")
        self.write("\t\t")
    def retrieve(self):
        '''
        push an address then run this command,
        and the val in the address will be pushed to the stack.
        '''
        self.heap()
        if self.explain:
            self.write("store")
        self.write("\t\t")

# Flow Control
    def flow(self):
        '''
        IMP: Flow Control
        Flow control operations are also common.
        Subroutines are marked by labels, as well as the targets
            of conditional and unconditional jumps,
            by which loops can be implemented.
        Programs must be ended by means of [LF][LF][LF]
            so that the interpreter can exit cleanly.
        '''
        if self.explain:
            self.write("IMP:Flow_Control")
        self.write("\n")
    def label(self, label):
        '''Mark	a location in the program'''
        self.flow()
        if self.explain:
            self.write("add_label")
        self.write("  " + self.number(label))
    def subr(self, label):
        '''Call a subroutine in the program'''
        self.flow()
        if self.explain:
            self.write("call_subroutine")
        self.write(" \t" + self.number(label))
    def jump(self, label):
        '''jump to a label unconditionally'''
        self.flow()
        if self.explain:
            self.write("jump_to_following_label")
        self.write(" \t" + self.number(label))
    def jumpzero(self, label):
        '''jump to a label if the top of the stack is 0'''
        self.flow()
        if self.explain:
            self.write("jump_to_following_label_if_top_zer")
        self.write(" \t" + self.number(label))
# Serial com commands
    def iostream(self):
        '''IMP: serial commands'''
        if self.explain:
            self.write("IMP:I/O")
        self.write("\t\n")