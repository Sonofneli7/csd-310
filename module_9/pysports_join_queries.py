import mysql.connector
from mysql.connector import errorcode
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}
try:
    db = mysql.connector.connect(**config)

    print("\n Database{} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    input("\n\n Press any key to continue...")

    cursor = db.cursor()
    
    ## Queries mysql for inner join player data
    
    

    cursor.execute("SELECT player_id, first_name, last_name, team_name  FROM player INNER JOIN team ON player.team_id = team.team_id;")

    players = cursor.fetchall()

    print("-- DISPLAYING PLAYER RECORDS --")
    for player in players:
        print("Player ID: {}".format(player[0]))
        print("First Name: {}".format(player[1]))
        print("Last Name: {}".format(player[2]))
        print("Team Name: {}".format(player[3]))
        print("\n")

except mysql.connector.Error as err:
    if err.errno == errorcode.ERR_ACCESS_DENIED_ERROR:
        print("  The specified database does not exist")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("    The specified database does not exist")

    else:
        print(err)

finally:
      db.close()

