import argparse


def args_parse():
    '''
    Takes two lines of file paths as input
    and returns a line with the comparison
    '''
    desc = "Compares two configuration files and shows a difference."
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("first_file", type=str, default="")
    parser.add_argument("second_file", type=str, default="")
    parser.add_argument("-f", "--format", type=str,
                        default="stylish",
                        choices=['stylish', 'plain', 'json'],
                        help="set format of output")
    args = parser.parse_args()
    return args
