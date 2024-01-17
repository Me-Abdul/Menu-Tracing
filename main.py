import json
import argparse
import xml.etree.ElementTree as ET
from traverser import traverse
from utils import get_nav, print_tree, count_nested_elements

def main():
    parser = argparse.ArgumentParser(description='Navigation Links Depth Parser')

    parser.add_argument('url', type=str, help='The URL (compulsory).')
    parser.add_argument('-u', '--unique', action='store_true', help='Unique flag (optional).')
    parser.add_argument('-v',  '--verbose', action='store_true', help='Verbose flag (optional).')
    parser.add_argument('-o', '--output', type=str, help='Output file (optional).')
    parser.add_argument('-f', '--format', type=str, help='Output format (optional).')

    args = parser.parse_args()

    if args.url:
        items = []
        nav = get_nav(args.url)
        items = traverse(element=nav, level=1, unique=not args.unique)
        counter = count_nested_elements(items)

        # If an output file is specified, write the output to that file
        if args.output:
            if args.format == 'json':
                # Convert the list of tuples to a list of dictionaries for JSON serialization
                items_dict = [{"level": level, "title": title, "href": href} for level, title, href in items]

                with open(args.output, 'w') as f:
                    json.dump(items_dict, f, indent=4)
            elif args.format == 'xml':
                root = ET.Element("root")
                for level, title, href in items:
                    item = ET.SubElement(root, "item")
                    ET.SubElement(item, "level").text = str(level)
                    ET.SubElement(item, "title").text = title
                    ET.SubElement(item, "href").text = href

                tree = ET.ElementTree(root)
                tree.write(args.output)

        print("BREADTH:", len(items))
        print("|")
        print_tree(lst=items, level=1, verbose=args.verbose, children_counter=counter)

    else:
        print('Error: URL not found.')
        parser.print_help()

if __name__ == "__main__":
    main()
