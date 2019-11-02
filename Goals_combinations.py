import itertools
Team1,Team2 = map(str,input().split(','))
Goals1 = int(input())
Goals2 = int(input())
Total = Team1 + Team2
Case = []
if Goals1 == 0 and Goals2 == 0:
    print(0)
else:
    Case.append(sorted(set([''.join(anagram) for anagram in itertools.product(Total,repeat=(Goals1+Goals2))if (anagram.count(Team1) == Goals1 and anagram.count(Team2) == Goals2)])))
    for p in range(len(Case[0])):
        print("{}".format(Case[0][p]))


