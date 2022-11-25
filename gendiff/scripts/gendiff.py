import argparse
import json
from gendiff.difference_calculator.gendiff import generate_diff


def main():
    '''
        The script is responsible for checking two flat json files
        Takes two lines of file paths as input
        and returns a line with the comparison
    '''
    desc = "Compares two configuration files and shows a difference."
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("first_file", type=str, default="")
    parser.add_argument("second_file", type=str, default="")
    parser.add_argument("-f", "--format", type=str, default="json",
                        help="set format of output")
    args = parser.parse_args()
    file1 = json.load(open(args.first_file, encoding='utf8'))
    file2 = json.load(open(args.second_file, encoding='utf8'))
    result = generate_diff(first_file=file1, second_file=file2)
    print(result)
    return result


if __name__ == '__main__':
    main()
