from prompt_toolkit import prompt

def report_count():
    corpus_tokens = word_tokenize(corpus.lower())
    text = nltk.Text(corpus_tokens)
    search_token = token.lower()
    token_count = corpus_tokens.count(search_token)
    print(f"The term '{search_token}' shows up in the corpus {token_count} times.")
