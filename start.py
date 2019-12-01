import sys

from league import League


# # instantiate the league class && get user input

leagueData = []
for line in sys.stdin:
    leagueData.append(line)

league = League()

league.readMatchResults(leagueData)

league.displayTableLog()
