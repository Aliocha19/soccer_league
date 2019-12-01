import unittest

from league import League


class TestLeague(unittest.TestCase):

    

    def test_compute_points_per_match(self):
        #assume #action #assert
        
        league = League()
       
        homeGoal = 2
        AwayGoal = 1
        result = league.computePoints(homeGoal, AwayGoal)
        self.assertEqual(result, {'home': 3, 'away': 0})

        homeGoal = 1
        AwayGoal = 1
        result = league.computePoints(homeGoal, AwayGoal)
        self.assertEqual(result, {'home': 1, 'away': 1})

        homeGoal = 1
        AwayGoal = 2
        result = league.computePoints(homeGoal, AwayGoal)
        self.assertEqual(result, {'home': 0, 'away': 3})

    def test_assigning_points_per_team(self):

        #assume #action #assert

        matchPoints = {'teamName': 'Grouches', 'teamPts': 3}
        league = League()
        league.teamPointList = [{'tName': 'Grouches', 'tPts': 0}, {
            'tName': 'Tarantulas', 'tPts': 6}]
        expected = [{'tName': 'Grouches', 'tPts': 3},{'tName': 'Tarantulas', 'tPts': 6}] 
        league.assignPoints(matchPoints)
        self.assertEqual(league.teamPointList, expected)

    def test_format_team_data(self):

        #assume #action #assert

        sampleLine = 'Lions 3'
        league = League()
        result = league.getFormatedData(sampleLine)
        expected = {'tname': 'Lions', 'tscore': 3}
        self.assertEqual(result, expected)
        sampleLine = 'FC Awesome 1'
        result = league.getFormatedData(sampleLine)
        expected = {'tname': 'FC Awesome', 'tscore': 1}
        self.assertEqual(result, expected)

    def test_prepare_team_list(self):

        #assume #action #assert
        
        leagueData = ['Snakes 3, Lions 3', 'Snakes 3, Lions 3']
        league = League()
        league.prepareTeamList(leagueData)
        result = len(league.teamPointList)
        expected = 2
        self.assertEqual(result, expected)
        result = league.teamPointList[0]['tPts']
        self.assertEqual(result, 0)

    def test_ranking(self):

      #assume #action #assert
       league = League()
       league.teamPointList = [{'tName': 'Snakes', 'tPts': 1}, {'tName': 'FC Awesome', 'tPts': 1},{'tName': 'Lions', 'tPts': 5},
          {'tName': 'Grouches', 'tPts': 0},
          {'tName': 'Tarantulas', 'tPts': 6}
         ]
       result = league.rankTeams()
       self.assertEqual(result[0]['tPts'], 6)
       self.assertEqual(result[3]['tName'], 'Snakes')


   

