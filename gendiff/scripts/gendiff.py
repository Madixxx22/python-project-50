from gendiff.cli import args_parse
from gendiff.difference_calculator.select_file import format_select


def main():
    '''
        The script is responsible for checking two flat json files
    '''
    args = args_parse()
    result = format_select(first_path_file=args.first_file,
                           second_path_file=args.second_file,
                           format=args.format)
    print(result)


if __name__ == '__main__':
    main()
