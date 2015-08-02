import sys
import numpy

def main():
    print sys.argv
    assert len(sys.argv) == 4, 'Need exactly 3 arguments'
    try:
        operand1, operand2 = float(sys.argv[1]), float(sys.argv[3])
    except ValueError:
        print 'cannot convert input to a number: bailing out'
        return
        
    operator = sys.argv[2]
    # currently this works with + and - but fails with * and / (either in quotes or not)
    assert operator in ['+', '-', '*' '/'], \
           'Operator is not one of +, -, * or /: bailing out' 
    do_arithmetic(operand1, operator, operand2)

def do_arithmetic(operand1, operator, operand2):

    if operator == '+':
        value = operand1 + operand2
    elif operator == '-':
        value = operand1 - operand2
    elif operator == '*':
        value = operand1 * operand2
    elif operator == '/':
        value = operand1 / operand2
    print value

main()
