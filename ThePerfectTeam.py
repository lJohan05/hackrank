def perfectTeam(skills):
    str = "pcmbz"
    freq = [0] * 26
    for c in skills:
        freq[ord(c) - 97] = freq[ord(c) - 97] + 1
    mn = len(skills)
    for c in str:
        mn = min(mn, freq[ord(c) - 97])
    return mn

print(perfectTeam("pcmpcmbbbzz"))
    