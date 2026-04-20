import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    res = np.zeros(len(vocab), dtype=int)
    vocab_id = {word:i for i, word in enumerate(vocab)}

    for token in tokens:
        id = vocab_id.get(token);
        if id is not None:
            res[id]+=1

    return res