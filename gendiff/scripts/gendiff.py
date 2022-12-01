import argparse
from gendiff.difference_calculator.select_file import file_format_selection


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
    result = file_format_selection(first_path_file=args.first_file,
                                   second_path_file=args.second_file)
    print(result)


if __name__ == '__main__':
    main()
