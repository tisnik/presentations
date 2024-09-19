import os
from collections import defaultdict
from glob import iglob

from pygments.lexer import *
from pygments.lexers import get_lexer_by_name
from pygments.token import *

# slovnik s citacem frekvenci vsech klicovych slov
keywords_freq = defaultdict(lambda: 0)

# lexer pro zvoleny programovaci jazyk
lexer = get_lexer_by_name("go")


def all_sources(path, pattern):
    """Ziskani seznamu souboru na PATH a v rekurzivne i v podadresarich."""
    path = os.path.join(path, "**/", pattern)
    sources = [filename for filename in iglob(path, recursive=True)]
    return sources


def keywords_for_file(filename):
    """Ziskani seznamu klicovych slov nalezenych ve specifikovanem souboru."""
    with open(filename) as fin:
        source = fin.read()
        tokens = lexer.get_tokens(source)

    keywords = []
    for token in tokens:
        t_type = token[0]
        if (
            t_type is Token.Keyword
            or t_type in Token.Keyword.Namespace
            or t_type in Token.Keyword.Declaration
        ):
            keywords.append(token[1])
    return keywords


def print_frequency_table(keywords_freq):
    """Tisk tabulky s frekvenci klicovych slov."""
    # sort tridi n-tice nejprve podle prvniho prvku,
    # takze musime slovnik prevest na sekvenci n-tic (frekvence, klicove_slovo)
    swapped = [(v, k) for k, v in keywords_freq.items()]
    swapped.sort()  # reverse=True pro opacne trideni

    for counter, keyword in swapped:
        print(counter, keyword)


for source in all_sources("src/", "*.go"):
    print(source)
    for keyword in keywords_for_file(source):
        keywords_freq[keyword] += 1

print("\n\n")

print_frequency_table(keywords_freq)
