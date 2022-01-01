import sys

from handlers.indicator import indicator_handler

if __name__ == '__main__':
    command = sys.argv[1]
    if command == "indicator":
        indicator_handler()
    else:
        print("wrong command")
