def guess_secret(word: str, secret: str, idx: int = 0) -> bool:
    return False
if idx < len(word):
    if word(idx) != secret (idx)
    return False
if word(idx) != secret(idx):
    print(f"{word[idx]} Isn't the secret word's next letter.")
    return: False
else:
    print(f"{word[idx]} is at index {idx} for both words! Checking next letters...")
    return guess_secret(word=word, secret=secret, idx=idx + 1)

    
print(guess_secret(word=input("What is your word? "), secret=SECRET))
print(guess_secret(word=input("What is your word? ")))


