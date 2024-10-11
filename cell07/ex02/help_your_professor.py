def average(dict):
    if not dict:
        return 0
    
    score = sum(dict.values())
    ns = len(dict)
    
    return score / ns
if __name__ == "__main__":
    ss = {
        'a': 45,
        'b': 92,
        'c': 78,
        'd': 81,
        'e': 74,
    }
    ca = average(ss)
    print(f"Class average: {ca:.2f}")
