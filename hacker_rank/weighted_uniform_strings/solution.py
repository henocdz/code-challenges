def weightedUniformStrings(s, queries):
    db = set()
    len_s = len(s)
    substring = []
    for i in range(0, len_s):
        current_char = s[i]
        if substring and substring[-1] == current_char:
            substring.append(current_char)
        else:
            substring = [current_char]

        new_index = (ord(current_char) - ord('a') + 1) * len(substring)
        if new_index not in db:
            db.add(new_index)


    response = []
    for query in queries:
        response_txt = 'Yes' if query in db else 'No'
        response.append(response_txt)
    return response


if __name__ == '__main__':
    print(
        weightedUniformStrings('abccddde', [1, 3, 12, 5, 9, 10])
    )
