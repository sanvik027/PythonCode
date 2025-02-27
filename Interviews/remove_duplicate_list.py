def remove_duplicates(lst):
    seen = set()
    for idx in lst:
        if idx not in seen:
            seen.add(idx)
    return list(seen)
print(remove_duplicates(["abcd","apple","apple","Banana"]))