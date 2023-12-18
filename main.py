#! /usr/bin/python

import argparse
from traverser import traverse
from utils import get_nav, print_tree, count_nested_elements


def main():
    parser = argparse.ArgumentParser(
        description='Navigation Links Depth Parser')

    parser.add_argument('url', type=str, help='The URL (compulsory).')
    parser.add_argument('-u', '--unique',
                        action='store_true',
                        help='Unique flag (optional).'
                        )

    parser.add_argument('-v',  '--verbose',
                        action='store_true',
                        help='Verbose flag (optional).'
                        )

    args = parser.parse_args()

    if args.url:

        items = []
        nav = get_nav(args.url)
        if args.verbose:

            items = traverse(element=nav, level=1, unique=not args.unique)
            counter = count_nested_elements(items)
            print("BREADTH:", len(items))
            print("|")
            print_tree(lst=items, level=1, verbose=True, children_counter=counter)
        else:
            items = traverse(element=nav, level=1, unique=not args.unique)
            counter = count_nested_elements(items)
            print("BREADTH:", len(items))
            print("|")
            print_tree(lst=items, level=1, children_counter=counter)

    else:
        print('Error: URL not found.')
        parser.print_help()


if __name__ == "__main__":
    main()
