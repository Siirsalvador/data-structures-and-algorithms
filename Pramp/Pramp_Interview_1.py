def decodeVariations(S):
    # if '0' in list(S):
    #     return 0

    return decodeVariationsRecur(S)


def decodeVariationsRecur(S):
    if len(S) == 0:
        return 1

    total = 0
    if S[0] != 0:
        total += decodeVariationsRecur(S[1:])
        if len(S) > 1 and 27 > int(S[0:2]) >= 10:
            total += decodeVariationsRecur(S[2:])
        elif 26 < int(S[0:2]) < 10:
            return 0

    return total


def main():
    _string = '20'
    print(decodeVariations(_string))


if __name__ == "__main__":
    main()
