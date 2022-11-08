def totalFruit(fruits: list[int]) -> int:
    n = len(fruits)

    assert(n > 0, "Cannot have an empty farm!")

    start = 0
    max_collected = 0

    while start < n:
        b1, b2 = fruits[start], ''
        curr = start + 1
        collected = 1
        
        while curr < n:
            if b1 != fruits[curr] and b2 == '':
                b2 = fruits[curr]

            if b1 != '' and b2 != '' and fruits[curr] not in [b1, b2]:
                break

            collected += 1
            curr += 1

        if collected > max_collected:
            max_collected = collected

        start += 1

    return max_collected
