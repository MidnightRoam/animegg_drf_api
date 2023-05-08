def slug_generator(title):
    """
    Takes a title and returns
    correct string for
    model slug field
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
