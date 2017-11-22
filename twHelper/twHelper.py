import requests
import math
import time, datetime
import sys, os
import re
from urllib.parse import unquote
from threading import Thread
import wx
import wx.xrc
import twHelperGUI


class twHelper:
	"""Handler"""

	def __init__(self):
		"""Initialize."""
		self.worldspeed = 0
		self.unitspeed = 0
		self.worldName = "en97"
		self.storageDirectory = ''

		# set unit movement speeds
		self.units = {
			'sp' : 18,
			'sw' : 22,
			'axe' : 18,
			'ar' : 18,
			'sc' : 9,
			'lc' : 10,
			'ma' :10,
			'hc' : 11,
			'ram' : 30,
			'cat' : 30,
			'pal' : 10,
			'noble' : 35
		}

		self.speeds = [ "ram", "sw", "sp", "hc", "pal" ]
				
		villageTarget = "500|500"

		# loaded villages in rows
		self.villages = []
		# In the format:
		#
		#	[ID, NAME, XXX, YYY, PLAYER_ID, POINTS, CONQ]

		self.players = []
		self.tribes = []
		
		# loaded villages in columns
		self.villagesCol = [[],[],[],[],[],[],[]]
		self.playersCol = [[],[],[],[],[],[]]
		self.tribesCol = [[],[],[],[],[],[],[],[]]

		self.plunderList = []
		self.haulList = []
		self.plunderListString = ''
		self.haulListString = ''

		self.getWorldInfo()
		self.loadWorldData()

		#kappa = self.farmRankList("~A~")

		#self.getSnipeString("359|559", "spideysenses", "13.11.2017 18:00:00.473", True, True)

	def farmRankProcessList(self, list, order = False, descending = True, bbcode = True, title = "ERROR"):
		if order:
			list = sorted(list, key=lambda x: x[2], reverse = descending)
		if True:
			string = '[table]\n[**]Name[||]Rank[||]' + title + '[||]Date[/**]\n'
			for i in range(0,len(list)):
				list[i][0] = "[ally]" + list[i][0] + "[/ally]"
				string = string + "[*]" + "[|]".join(list[i]) + "\n"
			string = string + "[/table]"

		return string


	def getInDayInfo(self, name, type):
		if type == "Plunders":
			# get loot_vil data
			temp = requests.get("https://" + self.worldName + ".tribalwars.net/guest.php?screen=ranking&mode=in_a_day&type=loot_vil&name=" + name)
			text = temp.text.replace('<span class="grey">.</span>',"")
			list = re.findall('lit-item\">(.*)</td>', text)
			self.plunderList.append([name] + list)
		else:
			# get loot_res data
			temp = requests.get("https://" + self.worldName + ".tribalwars.net/guest.php?screen=ranking&mode=in_a_day&type=loot_res&name=" + name)
			text = temp.text.replace('<span class="grey">.</span>',"")
			list = re.findall('lit-item\">(.*)</td>', text)
			self.haulList.append([name] + list)

	def getTribeMembers(self, tribeAbbrev):
		id = self.findTribe(tribeAbbrev)
		return self.getTribeMemberList(id)
	
	def findTribe(self, tribeAbbrev):
		"""Find the userID of a username."""
		index = [i for i, abbrev in enumerate(self.tribesCol[2]) if tribeAbbrev in abbrev]
		id = self.tribesCol[0][index[0]]
		return id

	def getTribeMemberList(self, tribeID):
		index = [i for i, id in enumerate(self.playersCol[2]) if tribeID in id]
		members = []
		for i in range(0, len(index)):
			members.append(self.playersCol[1][index[i]])
		return members


	def getSnipeString(self, target, player, landTime, bbcode, sortList):
		userID = self.findUserID(player)
		villages = self.findVillage(userID)
		temp = self.rowToVillage(villages)

		landTimeUnix = self.stringToUnix(landTime)
		print(landTimeUnix)
		if bbcode:
			print("[ally]" + player + "[/ally] hitting [village]" + target + "[/village] at " + landTime)
		else:
			print(player + " hitting " + target + " at " + landTime)

		sendList = []

		for i in range(0, len(temp)):
			distance = self.distanceCalc(target, temp[i][1])
			for j in range(0, len(self.speeds)):
				timeTo = self.timeToVillage(distance, self.speeds[j])
				timeLaunchString = self.unixToString(landTimeUnix - timeTo)
				if bbcode:
					unitName = str(self.speeds[j])
					sA = timeLaunchString
					sB = "Launch " + unitName.ljust(3) + " from [village]" + temp[i][1] + "[/village] at " + timeLaunchString
					sendList.append([sA, sB])

				else:
					sendList.append("Launch " + self.speeds[j] + " from " + temp[i][1] + " at " + timeLaunchString)

		if sortList:
			sendListSorted = sorted(sendList, key=lambda x: x[0])
			for i in range(0,len(sendListSorted)):
				print(sendListSorted[i][1])
		else:
			for i in range(0,len(sendList)):
				print(sendListSorted[i][1])


	def rowToVillage(self, villages):
		"""Take a list of village parameters and give us back some more important things"""
		# Returns villages in the following format:
		#
		# ['VILLAGE_NAME', 'XXX|YYY', 'VILLAGE_NAME (XXX|YYY)'],
		#

		temp = []
		for i in range(0, len(villages)):
			print(self.villages[villages[i]])
			temp.append([unquote(self.villages[villages[i]][1].replace("+"," ")),
							self.villages[villages[i]][2] + "|" + self.villages[villages[i]][3],
							unquote(self.villages[villages[i]][1].replace("+"," ")) + " (" +
							self.villages[villages[i]][2] + "|" + self.villages[villages[i]][3] + ")"])
		return temp


	def stringToUnix(self, string):
		# Example string format:
		#		12.11.2017 16:25:08.473

		dt_struct = datetime.datetime.strptime(string, "%d.%m.%Y %H:%M:%S.%f")
		return float(time.mktime(dt_struct.timetuple())) + dt_struct.microsecond / 1000000

	def unixToString(self, unixTime):
		# Example string format:
		#		12.11.2017 16:25:08.473
		t_string = str(datetime.datetime.fromtimestamp(unixTime).strftime('%d.%m.%Y %H:%M:%S.%f'))
		
		return t_string[:-3]
		

	def distanceCalc(self, a, b):
		"""Find the distance between two villages."""
		# Split the strings
		aSplit = re.split('\|',a)
		bSplit = re.split('\|',b)

		# Get the difference between the points
		xDiff = float(abs(int(aSplit[0]) - int(bSplit[0])))
		yDiff = float(abs(int(aSplit[1]) - int(bSplit[1])))
		
		# Calculate the distance
		distance = math.sqrt(math.pow(xDiff, 2) + math.pow(yDiff, 2))
		
		return distance

	def timeToVillage(self, distance, unit):
		"""Calculate the time to travel a distance given a unit speed."""
		return float(round(distance * self.units[unit] * 60 * self.worldspeed * self.unitspeed))

	def findUserID(self, username):
		"""Find the userID of a username."""
		index = [i for i, names in enumerate(self.playersCol[1]) if username in names]

		return self.playersCol[0][index[0]]

	def findVillage(self, userID):
		"""Find the userID of a username."""
		index = [i for i, ids in enumerate(self.villagesCol[4]) if userID in ids]
		return index

	def loadWorldData(self):
		"""Loads the world data into lists of strings in RAM."""

		# load villages
		print("Loading villages...")
		temp = open(self.storageDirectory + self.worldName + "Villages.txt", "r")
		self.villages = (temp.read()).splitlines()
		for i in range(0, len(self.villages)):
			self.villages[i] = re.split(',',self.villages[i])
			temp = self.villages[i]
			for i in range(0,7):
				self.villagesCol[i].append(unquote(temp[i].replace("+"," ")))
		
		# load players
		print("Loading players...")
		temp = open(self.storageDirectory + self.worldName + "players.txt", "r")
		self.players = (temp.read()).splitlines()
		for i in range(0, len(self.players)):
			self.players[i] = re.split(',',self.players[i])
			temp = self.players[i]
			for i in range(0,6):
				self.playersCol[i].append(unquote(temp[i].replace("+"," ")))

		# load tribes
		print("Loading tribes...")
		temp = open(self.storageDirectory + self.worldName + "tribes.txt", "r")
		self.tribes = (temp.read()).splitlines()
		for i in range(0, len(self.tribes)):
			self.tribes[i] = re.split(',',self.tribes[i])
			temp = self.tribes[i]
			for i in range(0,8):
				self.tribesCol[i].append(unquote(temp[i].replace("+"," ")))

		# get other world information
		content = requests.get("https://" + self.worldName + ".tribalwars.net/interface.php?func=get_config").text
		self.worldspeed = self.getWorldElement(content, "speed")
		self.unitspeed = self.getWorldElement(content, "unit_speed")
		
		return
	
	def getWorldElement(self, text, target):
		temp = re.search('<' + target + '>(.*)</' + target + '>', text)
		return float(temp.group(1))

	def getWorldInfo(self):
		"""Gets map information from the Tribalwars website."""

		self.worldName = input("Which world are we looking at? (en93, en97, etc.): ")

		self.storageDirectory = os.getenv('APPDATA') + "/twHelper/"
		if not os.path.exists(self.storageDirectory):
			os.makedirs(self.storageDirectory)

		# check how long since update
		if not os.path.isfile(self.storageDirectory + self.worldName + "Villages.txt") or (time.time() - os.path.getmtime(self.storageDirectory + self.worldName + "Villages.txt")) / 60 >= 60:
			# load villages
			print("Downloading village information... ")
			map = requests.get("https://" + self.worldName + ".tribalwars.net/map/village.txt")
			villages = open(self.storageDirectory + self.worldName + "Villages.txt", "w")
			villages.write(map.text)
			villages.close()
		
			# load players
			print("Downloading player information... ")
			map = requests.get("https://" + self.worldName + ".tribalwars.net/map/tribe.txt")
			players = open(self.storageDirectory + self.worldName + "players.txt", "w")
			players.write(map.text)
			players.close()
		
			# load tribes
			print("Downloading tribe information... ")
			map = requests.get("https://" + self.worldName + ".tribalwars.net/map/ally.txt")
			tribes = open(self.storageDirectory + self.worldName + "tribes.txt", "w")
			tribes.write(map.text)
			tribes.close()


#inherit from the MainFrame created in wxFowmBuilder and create CalcFrame
class CalcFrame(twHelperGUI.mainFrame):
	#constructor
	def __init__(self,parent):
	#initialize parent class
		twHelperGUI.mainFrame.__init__(self,parent)
		self.helper = twHelper()
		self.plunderList = []
		self.haulList = []
		self.plunderListString = ''
		self.haulListString = ''

	# when go is clicked
	def getList(self,event):
		try:
			# start a new thread with 
			Thread(target = self.fillMemberList).start()
		except Exception as e:
			print('error')

	def fillMemberList(self):
		typ = self.farmType.GetString(self.farmType.GetSelection())
		order = self.farmOrder.GetString(self.farmOrder.GetSelection())
		if order == "Ascending" or order == "Descending":
			descending = False
			if order == "Descending":
				descending = True
			order = True
		else:
			order = False
		check = self.farmBBcode.IsChecked()
		self.memberList.SetValue(str("Processing the list.  This may take some time."))
		string = self.farmRankList(self.farmTribeAbbrev.GetValue(),descending = order, type = typ, bbcode = check)
		self.memberList.SetValue(string)

	def farmRankList(self, tribeAbbrev, order = False, descending = True, bbcode = True, type = "Hauls"):
		'''Get the farm ranks of a tribe.'''
		self.plunderList = []
		self.haulList = []
		self.plunderListString = ''
		self.haulListString = ''

		members = self.helper.getTribeMembers(tribeAbbrev)
		for i in range(0, len(members)):
			self.twHelperLog.SetValue("[" + str(i + 1) + "/" + str(len(members)) + "]\n")
			self.helper.getInDayInfo(members[i], type)
			
		self.twHelperLog.AppendText("Finished getting info for " + tribeAbbrev)
		
		string = ''

		if type == "Plunders":
			string = self.helper.farmRankProcessList(self.helper.plunderList, order = order, descending = descending, bbcode = bbcode, title = "Total Plunders")
		else:
			string = self.helper.farmRankProcessList(self.helper.haulList, order = order, descending = descending, bbcode = bbcode, title = "Total Haul")

		return string

if __name__ == '__main__':
	#mandatory in wx, create an app, False stands for not deteriction stdin/stdout
	#refer manual for details
	app = wx.App(False)

	##create an object of CalcFrame
	frame = CalcFrame(None)
	##show the frame
	frame.Show(True)
	##start the applications
	app.MainLoop()