
class League:

    def __init__(self):

        self.teamPointList = []
        # self.leagueResults = teamResultsData

    def assignPoints(self, matchPoints):

        for teamPointVal in self.teamPointList:

            if matchPoints['teamName'] in teamPointVal.values():

                teamPointVal['tPts'] = int(
                    teamPointVal['tPts']) + int(matchPoints['teamPts'])

                break

    def getFormatedData(self,rawData):

        clean = rawData.strip() 

        return {'tname': clean[:clean.rfind(' ')].strip(), 'tscore': int(clean[clean.rfind(' '):].strip())}

    def prepareTeamList(self, leagueData):

        myListTeam = set()
        for leagueGame in leagueData:
            mdRes = leagueGame.split(',')
            homeFrmt = self.getFormatedData(mdRes[0])
            awayFrmt = self.getFormatedData(mdRes[1])
            myListTeam.add(homeFrmt['tname'])
            myListTeam.add(awayFrmt['tname'])

        for x in myListTeam:
                self.teamPointList.append({'tName': x, 'tPts': 0})

    def computePoints(self, homeScore, awayScore):

        if homeScore > awayScore:
            return {'home': 3, 'away': 0}
        if homeScore < awayScore:
            return {'home': 0, 'away': 3}
        if homeScore == awayScore:
            return {'home': 1, 'away': 1}

    def rankTeams(self):

        teamList = sorted(self.teamPointList, key=lambda myTeam: (
        -myTeam['tPts'], myTeam['tName']))
        return teamList

    def displayTableLog(self):
        teamList = self.rankTeams()
        for idx, val in enumerate(teamList, start=1):
             name = val['tName']
             points = val['tPts']
             ptText = 'pts'
             if points == 1:
                ptText = 'pt'
             print(f'{idx}. {name},  {points} {ptText}')

    def updateTableData(self, homeVal, awayVal):

        currentPoint = self.computePoints(homeVal['tscore'], awayVal['tscore'])
        matchPointsHome = {
        'teamName': homeVal['tname'], 'teamPts': currentPoint['home']}
        matchPointsAway = {
        'teamName': awayVal['tname'], 'teamPts': currentPoint['away']}
        self.assignPoints(matchPointsHome)
        self.assignPoints(matchPointsAway)

    def readMatchResults(self, leagueData):
   
        self.prepareTeamList(leagueData)
        for matchDay in leagueData:
            mdRes = matchDay.split(',')
            homeFrmt = self.getFormatedData(mdRes[0])
            awayFrmt = self.getFormatedData(mdRes[1])
            homeValNow = {'tname': homeFrmt['tname'],
                        'tscore': int(homeFrmt['tscore'])}
            awayValNow = {'tname': awayFrmt['tname'],
                        'tscore': int(awayFrmt['tscore'])}
            self.updateTableData(homeValNow, awayValNow)




