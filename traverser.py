from bs4 import PageElement


# keep track of visited links.
history = []


def traverse(element: PageElement, level: int = 1, unique=True) -> list[tuple[int, str, str]]:
    """
    traverse over all the links in the navbar and returns the list of links with their level.

    Args:
        element (PageElement): Navbar Element
        level (int, optional): The level or depth of the element. default to 1.
        unique (bool, optional): When set to true only returns unique links. Defaults to True.

    Returns:
        list[tuple[int, str, str]]: List of tuple containing level(depth), href and title.
    """

    links = []
    # traverse over all the list item containing navigation link
    for item in element.select(':scope ul > li'):
        # Find the link if it has any.
        anchor = item.find('a')
        if anchor:
            href = anchor.attrs.get('href')
            title = anchor.text
            # If we have already visited that link skip it.
            if (href not in history):
                links.append((level, title, href))
                if (unique):
                    history.append(href)

        links.extend(traverse(item, level + 1, unique=unique))

    return links
