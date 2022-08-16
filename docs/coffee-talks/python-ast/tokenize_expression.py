import tokenize

with tokenize.open("expression.py") as fin:
    token_generator = tokenize.generate_tokens(fin.readline)
    for token in token_generator:
        print("{:2}  {:2}  {}".format(token.type, token.exact_type, token))
