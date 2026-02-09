"""simiarity.py"""
from sklearn.metrics.pairwise import cosine_similarity


total= lambda items, user_cols : len(items) * len(user_cols)

def exact_match_rate(user_cols, items, gold, norm):
    m = 0
    for c in user_cols:
        resp = norm(items[c])
        m += (resp == gold).sum()
    return m / total(items, user_cols)

def token_match_rate(user_cols, items, gold, norm):
    """Calculate token match rate where gold answer is contained within user response tokens."""
    m = 0
    gold_list = gold.tolist()
    for c in user_cols:
        resp_list = norm(items[c]).tolist()
        for g, r in zip(gold_list, resp_list):
            toks = r.split()
            if g in toks:
                m += 1
    return m / total(items, user_cols)

def last_token_match_rate(user_cols, items, gold, norm):
    """Calculate match rate where the last token of user response matches the gold answer."""
    m = 0
    gold_list = gold.tolist()
    for c in user_cols:
        resp_list = norm(items[c]).tolist()
        for g, r in zip(gold_list, resp_list):
            toks = r.split()
            if toks and toks[-1] == g:
                m += 1
    return m / total(items, user_cols)

def substring_match_rate(user_cols, items, gold, norm):
    """Calculate match rate where gold answer is a substring of user response."""
    m = 0
    gold_list = gold.tolist()
    for c in user_cols:
        resp_list = norm(items[c]).tolist()
        for g, r in zip(gold_list, resp_list):
            if g in r:
                m += 1
    return m / total(items, user_cols)