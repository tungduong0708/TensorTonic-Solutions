def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    res = {}

    for sentence in sentences:
        for word in sentence:
            if word not in res:
                res[word] = 0
            res[word] += 1

    return res
    