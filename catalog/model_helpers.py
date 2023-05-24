def slug_generator(title):
    """
    Generates a slug string for the given title.

    Args:
        title (str): The title for which to generate the slug.

    Returns:
        str: The slug string generated from the title.

    Examples:
        > > > slug_generator("Hello world!")
        'hello-world'
        > > > slug_generator("YOU ARE amazing!")
        'you-are-amazing'
    """
    invalid_url_chars = ['<', '>', '"', "'", '{', '}', '|', '\\',
                         '^', '`', '[', ']', '\t', '\n', '\r', '%',
                         '#', '&', '+', ',', '/', ':', ';', '=', '?', '@']
    result = ''
    for symbol in title:
        if symbol not in invalid_url_chars:
            result += symbol

    result = result.lower().replace(' ', '-')
    return result
