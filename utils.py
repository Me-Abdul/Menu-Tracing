from typing import List, Tuple, Union
from bs4 import PageElement
from bs4 import BeautifulSoup
import requests

# Constants

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"


# Utils
def get_nav(url: str) -> PageElement:
    """
    Send the request to given url and parse the navbar element of it.

    Args:
        url (str): Website URL

    Returns:
        PageElement: Navbar Element
    """

    response = requests.get(url, headers={"User-Agent": USER_AGENT})
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.find('nav')


def print_tree(
        lst: List[Tuple[int, str, Union[str, None]]],
        level: int = 0,
        verbose: bool = False,
        children_counter=None
        ) -> None:

    
    if not lst:
        return
    while lst:
        l, title, href = lst.pop(0)
        if l < level:
            lst.insert(0, (l, title, href))
            return
        indent = '| ' * (l - 1)
        if children_counter.get(title) is not None and children_counter.get(title) != 0:
            output = f"{indent}| - {title} ({children_counter[title]})"
        else:
            output = f"{indent}| - {title}"

        if verbose:
            if children_counter.get(title) is not None and children_counter.get(title) != 0:
                output = f"{indent}| - {title} ({href}) ({children_counter[title]})"
            else: 
                output = f"{indent}| - {title} ({href})"

        print(output)

        if lst and lst[0][0] > level:
            print_tree(lst, level + 1, verbose, children_counter)


def count_nested_elements(lst):
    # Initialize a dictionary to store the count of nested elements for each element

    nested_elements_count = {}
    # Initialize a stack to keep track of the current parent elements
    stack = []
    for item in lst:
        depth, element, _, = item
        while stack and stack[-1][0] >= depth:
            stack.pop()
        if stack:
            parent = stack[-1][1]
            nested_elements_count[parent] = nested_elements_count.get(parent, 0) + 1
        stack.append(item)
    return nested_elements_count
            