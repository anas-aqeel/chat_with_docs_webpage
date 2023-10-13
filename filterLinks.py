from urllib.parse import urlparse

def is_valid_url(input_str):
    try:
        parsed_url = urlparse(input_str)
        
        if parsed_url.scheme and parsed_url.netloc:
            return True
        else:
            return False
    except ValueError:
        return False

def isUseFullLink(input_str):
    if (
        '@' not in input_str
        and 'mailto:' not in input_str
        and 'tel:' not in input_str
        and 'javascript:' not in input_str
        and ' ' not in input_str
        and input_str != ''
        and (
            "docs" in input_str
            or "guide" in input_str
            or "tutorial" in input_str
            or "examples" in input_str
            or "reference" in input_str
            or "api" in input_str
            or "documentation" in input_str
            or "learn" in input_str
            or "support" in input_str
            or "faq" in input_str
            or "faqs" in input_str  # Added 'or' here
        )
    ):
        return True
    else:
        return False


def filterLinks(input_strings):
    valid_urls = []
    for input_str in input_strings:
        if is_valid_url(input_str) and isUseFullLink(input_str):
            valid_urls.append(input_str)
    return valid_urls


