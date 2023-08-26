import re
import time
import concurrent.futures
from tqdm import tqdm

# Measure the script running time
start_time = time.time()


def search_keyword(keyword):
    matches = []
    pattern = re.compile(keyword)

    with open('domain-names.txt', 'r', encoding='utf-8') as dn:
        for dn_line in dn:
            match = pattern.search(dn_line)
            if match:
                matches.append(match.group())

    result = {
        'keyword': keyword,
        'matches': matches
    }

    return result


def is_valid_regex(pattern):
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

            if kw_line.startswith(("#", " ")) or not kw_line:
                #print("Skipped comment or special character:", kw_line)
                continue

            if not is_valid_regex(kw_line):
                print(kw_line, "is an invalid pattern! Exiting...")
                exit(-1)

            print(kw_line, "is a valid pattern")
            keywords.append(kw_line)

    # Utilizing parallel processing for searching keywords
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(tqdm(executor.map(search_keyword, keywords),
                            total=len(keywords), desc="Processing Keywords"))

    for result in results:
        print(f"\nPattern search: {result['keyword']}")
        for match in result['matches']:
            print(match)
        print("Total matches:", len(result['matches']))
        print("\n")


if __name__ == "__main__":
    keyword_check()

    # Calculate and print the execution time
    elapsed_time = time.time() - start_time
    print(f"\nScript executed in {elapsed_time:.2f} seconds.")
