


def duplicate_count(text):
    repeats = set()
    seen = set()
    for i in text.lower():
        if i in seen:
            repeats.add(i)
        else:
            seen.add(i)
    return len(repeats)

print(len(duplicate_count("abcdeaB")))