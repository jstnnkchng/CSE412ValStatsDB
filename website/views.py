from flask import Blueprint, render_template, request
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        port=5435,
        database="postgres",
        user="postgres",
        password="postgres"
    )

curs = conn.cursor()

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/Teams', methods=['GET','POST'])
def Teams():
    curs.execute("SELECT Team.tname, Team.country, Team.winnings FROM Team")
    data=curs.fetchall()
    data2=0
    data3=0
    if request.method == 'POST':
        tName = request.form.get('teamName')
        if(len(tName)>0):
            curs.execute("SELECT Team.tname, Team.country, Team.winnings FROM Team WHERE Team.tname='{}'".format(tName))
            data = curs.fetchall()
            curs.execute("SELECT DISTINCT ESportPerson.espname, ESportPerson.age, ESportPerson.country, Player.winnings FROM ESportPerson, Player, Team WHERE Team.tid = Player.tid AND Player.pid = ESportPerson.uid AND Team.tname = '{}';".format(tName))
            data2=curs.fetchall()
            curs.execute("SELECT DISTINCT ESportPerson.espname, ESportPerson.age, ESportPerson.country FROM ESportPerson, Coach, Team WHERE ESportPerson.uid = Coach.cid AND Coach.tid = Team.tid AND Team.tname = '{}'".format(tName))
            data3 = curs.fetchall()
        else:
            curs.execute("SELECT Team.tname, Team.country, Team.winnings FROM Team")
            data = curs.fetchall()


    return render_template("Teams.html", data=data,data2=data2, data3=data3)

@views.route('/Players', methods=['GET','POST'])
def Players():
    curs.execute("SELECT DISTINCT ESportPerson.ESPname, ESportPerson.age, ESportPerson.country, Team.tname, Player.winnings FROM ESportPerson, Player, Team WHERE ESportPerson.uid = Player.pid AND Player.tid = Team.tid")
    data = curs.fetchall()
    data2=0
    if request.method == 'POST':
        pName = request.form.get('playerName')
        if (len(pName) > 0):
            curs.execute("SELECT DISTINCT ESportPerson.ESPname, ESportPerson.age, ESportPerson.country, Team.tname, Player.winnings FROM ESportPerson, Player, Team WHERE ESportPerson.uid = Player.pid AND Player.tid = Team.tid AND ESportPerson.ESPname = '{}';".format(pName))
            data = curs.fetchall()
            curs.execute("""SELECT DISTINCT Agent.name, Agent.kd, Agent.avgscore
                            FROM Agent, Player, ESportPerson
                            WHERE Player.pid = Agent.pid AND Player.pid = ESportPerson.uid AND ESportPerson.espname ='{}';""".format(pName))
            data2=curs.fetchall()
        else:
            curs.execute("SELECT DISTINCT ESportPerson.ESPname, ESportPerson.age, ESportPerson.country, Team.tname, Player.winnings FROM ESportPerson, Player, Team WHERE ESportPerson.uid = Player.pid AND Player.tid = Team.tid")
            data = curs.fetchall()
    return render_template("Players.html",data=data,data2=data2)

@views.route('/Coaches', methods=['GET','POST'])
def Coaches():
    curs.execute("SELECT DISTINCT ESportPerson.espname, ESportPerson.age, ESportPerson.country, Team.tname FROM ESportPerson, Coach, Team WHERE ESportPerson.uid = Coach.cid AND Coach.tid = Team.tid")
    data = curs.fetchall()
    if request.method == 'POST':
        cName = request.form.get('coachName')
        if (len(cName) > 0):
            curs.execute("SELECT DISTINCT ESportPerson.espname, ESportPerson.age, ESportPerson.country, Team.tname FROM ESportPerson, Coach, Team WHERE ESportPerson.uid = Coach.cid AND Coach.tid = Team.tid AND ESportPerson.espname = '{}'".format(cName))
            data = curs.fetchall()
        else:
            curs.execute("SELECT DISTINCT ESportPerson.espname, ESportPerson.age, ESportPerson.country, Team.tname FROM ESportPerson, Coach, Team WHERE ESportPerson.uid = Coach.cid AND Coach.tid = Team.tid")
            data = curs.fetchall()
    return render_template("Coaches.html",data=data)
