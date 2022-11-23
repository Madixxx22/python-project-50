import argparse
from gendiff.difference_calculator.gendiff import generate_diff

def main():
    parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file", type=str, default="")
    parser.add_argument("second_file", type=str, default="")
    parser.add_argument("-f", "--format", type=str, default="json", help="set format of output")
    args = parser.parse_args()
    print(generate_diff(first_file = args.first_file, second_file = args.second_file))

if __name__ == '__main__':
    main()
