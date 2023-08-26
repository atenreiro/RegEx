import re

"""
NOTES:

1) Added code to validate if a line is a comment or not.
2) Added code to validate if the regex pattern is valid or not.
3) First, validate all keywords and then perform the search.
   Instead of validating and searching one by one.
   Invalid patterns will make the script to abort and quit.
4) All keywords are added to a list and then the search is performed.
"""


def keyword_search(keywords):
    for keyword in keywords:
        # Search counter
        counter = 0

        print("Pattern search:", keyword)

        pattern = re.compile(keyword)

        with open('domain-names.txt', 'r', encoding='utf-8') as dn:
            for dn_line in dn:
                compliance = pattern.search(dn_line)
                if compliance:
                    print(compliance.group())  # Print the matched string
                    counter += 1

        print("Total matches:", counter)
        print("\n")


def is_valid_regex(pattern):
    """
    Check if a given string is a valid regex pattern.

    Args:
        pattern (str): The string to check.

    Returns:
        bool: True if the string is a valid regex pattern,ls
         False otherwise.
    """
    try:
        re.compile(pattern)
        return True
    except re.error:
        return False


def keyword_check():
    keywords = []

    with open('keywords.txt', 'r', encoding='utf-8') as kw:
        for kw_line in kw:
            kw_line = kw_line.strip()

            # Skip comments, empty lines, or lines starting with space
            if not kw_line or kw_line[0] in ["#", " "]:
                print("Skipped comment or special character:", kw_line)
                continue

            if is_valid_regex(kw_line):
                print(kw_line, "is a valid pattern")
            else:
                print(kw_line, "is an invalid pattern! Exiting...")
                exit(-1)

            keywords.append(kw_line)

    keyword_search(keywords)


if __name__ == "__main__":
    keyword_check()
