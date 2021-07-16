HOME_TEAM_WON = 1
def tournamentWinner(competitions,reusults):
    currentBestTeam=""
    scores = {currentBestTeam:0}
    for idx, competition in enumerate(competitions):
        result=result[idx]
        homeTeam, awayTeam = competition
        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam
        updateScores(winningTeam,3,scores)
        if scores[winningTeam]>scores[currentBestTeam]:
            currentBestTeam = winningTeam
    return currentBestTeam
def updateScores(team,point,scores):
    if team not in scores:
        scores[team] = 0
    scores[team] += points