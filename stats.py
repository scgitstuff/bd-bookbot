def countWords(s: str) -> int:
    count = len(s.split())

    return count


def countChars(s: str) -> dict[str, int]:
    chars: dict[str, int] = {}
    low = s.lower()

    for i in range(len(low)):
        c = low[i]
        if not c in chars.keys():
            chars[c] = 0
        chars[c] += 1

    return chars


def sortChars(chars: dict[str, int]) -> list[dict[str, int]]:

    def sort_on(d: dict[str, int]):
        return next(iter(d.values()))

    # type stuff got confused, x just to get rid of errors
    x = map(lambda c: {c: chars[c]}, chars)
    lst = list(x)
    lst.sort(reverse=True, key=sort_on)

    return lst


def filterChars(chars: dict[str, int]) -> dict[str, int]:
    return dict(filter(lambda c: c[0].isalpha(), chars.items()))
