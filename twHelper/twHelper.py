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
import traceback

# self.attackArriveTime = wx.adv.TimePickerCtrl( self.m_panel2, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.TP_DEFAULT )


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
			list = sorted(list, key=lambda x: float(x[1]), reverse = descending)
		if True:
			string = '[table]\n[**]Name[||]Tribe Rank[||]Global Rank[||]' + title + '[||]Date[/**]\n'
			for i in range(0,len(list)):
				list[i][0] = "[player]" + list[i][0] + "[/player][|]" + str(i + 1)
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
		index = [i for i, abbrev in enumerate(self.tribesCol[2]) if tribeAbbrev == abbrev]
		id = self.tribesCol[0][index[0]]
		return id

	def getTribeMemberList(self, tribeID):
		index = [i for i, id in enumerate(self.playersCol[2]) if tribeID == id]
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

	def getSnipeString2(self, target, landTime, bbcode, sortList, temp):
		landTimeUnix = self.stringToUnix(landTime)
		print(landTimeUnix)
		#if bbcode:
		#	print("[ally]" + player + "[/ally] hitting [village]" + target + "[/village] at " + landTime)
		#else:
		#	print(player + " hitting " + target + " at " + landTime)

		sendList = []

		for i in range(0, len(temp)):
			distance = self.distanceCalc(target, temp[i][1])
			for j in range(0, len(self.speeds)):
				timeTo = self.timeToVillage(distance, self.speeds[j])
				if landTimeUnix - timeTo > time.time():
					timeLaunchString = self.unixToString(landTimeUnix - timeTo)
					if bbcode:
						unitName = str(self.speeds[j].upper())
						sA = timeLaunchString
						sB = "Launch " + unitName.ljust(3) + " from [village]" + temp[i][1] + "[/village] at " + timeLaunchString
						sendList.append([sA, sB])

					else:
						sendList.append("Launch " + self.speeds[j] + " from " + temp[i][1] + " at " + timeLaunchString)

		outstring = ""
		if sortList:
			sendListSorted = sorted(sendList, key=lambda x: x[0])
			for i in range(0,len(sendListSorted)):
				outstring = outstring + sendListSorted[i][1] + "\n"
		else:
			for i in range(0,len(sendList)):
				outstring = outstring + sendList[i][1] + "\n"

		return outstring


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

	def findUserInfo(self, type, query):
		"""Find the userID of a username."""
		if type == "idFromUser":
			index = [i for i, names in enumerate(self.playersCol[1]) if query.lower() in names.lower()]
			return self.playersCol[0][index[0]]
		elif type == "tribeFromUser":
			print(query.lower())
			index = [i for i, names in enumerate(self.playersCol[1]) if query.lower() in names.lower()]
			tribe = [i for i, id in enumerate(self.tribesCol[0]) if str(self.playersCol[2][index[0]]) in str(id)]
			print(self.playersCol[0][index[0]])
			print(tribe)
			if tribe == []:
				return ""
			else:
				return self.tribesCol[2][tribe[0]]

	def findPlayerTribe(self, userID):
		"""Find the userID of a username."""
		index = [i for i, names in enumerate(self.tribesCol[1]) if username in names]

		return self.playersCol[0][index[0]]

	def searchUserID(self, username):
		"""Find the userID of a username."""
		index = [i for i, names in enumerate(self.playersCol[1]) if username in names]
		response = []
		for i in range(0,len(index)):
			response.append(self.playersCol[1][index[i]])

		return response

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

		# get the world name from the user, temporary implementation
		#self.worldName = input("Which world are we looking at? (en93, en97, etc.): ")

		# get the appdata directory
		self.storageDirectory = os.getenv('APPDATA') + "/twHelper/"
		if not os.path.exists(self.storageDirectory):
		# if there is no twHelper directory in appdata/roaming, make one
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
class twHelperMain(twHelperGUI.mainFrame):
	#constructor
	def __init__(self,parent):
	#initialize parent class
		twHelperGUI.mainFrame.__init__(self,parent)
		self.helper = twHelper()
		self.plunderList = []
		self.haulList = []
		self.plunderListString = ''
		self.haulListString = ''

		# ignore event texts
		self.snipeIgnoreEvtText = False
		self.snipeIgnoreEvtText2 = False
		self.farmIgnoreEvtText = False

		# snipe timer variables
		self.villageListStorage1 = []
		self.villageListStorage2 = []

	# when go is clicked
	def snipeUpdateSearch(self,event):
		if self.snipeIgnoreEvtText:
			self.snipeIgnoreEvtText = False
			return
		currentText = event.GetString()
		if currentText != "" and len(currentText) >= 4: # check that the input isnt empty, and is 4 characters or longer
			found = False
			for choice in self.helper.playersCol[1]: # for all usernames
				lowerChoice = choice.lower() # case insensitive search
				if lowerChoice.startswith(currentText.lower()): # case insensitive search
					# Set the search prediction
					self.snipeIgnoreEvtText = True
					self.snipeSearch.SetValue(choice) # apply the value to thne current prediction

					# highlight the part of the prediction that we havent typed yet
					self.snipeSearch.SetInsertionPoint(len(currentText))
					self.snipeSearch.SetSelection(len(currentText), len(choice))

					# Set the tribe abbreviation
					self.snipeTribe.SetValue(self.helper.findUserInfo("tribeFromUser",choice))

					# Find Villages
					userID = self.helper.findUserInfo("idFromUser", currentText) # get user id of current prediction/choice
					villages = self.helper.findVillage(userID) # get all villages belonging to the choice
					self.villageListStorage1 = self.helper.rowToVillage(villages) # get formatted village list

					# process formatted village list so that we only get a pretty string
					queryVillages = []
					for i in range(0, len(self.villageListStorage1)):
						queryVillages.append(self.villageListStorage1[i][2]) # append the "NAME (XXX|YYY)" string
					self.snipeDefendingVillage.SetItems(queryVillages) # send to output window

					found = True
					break
			if not found:
				event.Skip()
		else:
			event.Skip()

	def snipeSearchClear(self, event):
		self.snipeSearch.Clear()
		self.snipeTribe.Clear()
		self.snipeDefendingVillage.SetItems([])
		self.snipeIgnoreEvtText = True

	# when go is clicked
	def snipeUpdateSearch2(self,event):
		if self.snipeIgnoreEvtText2:
			self.snipeIgnoreEvtText2 = False
			return
		currentText = event.GetString()
		if currentText != "" and len(currentText) >= 4:
			found = False
			for choice in self.helper.playersCol[1]:
				lowerChoice = choice.lower()
				if lowerChoice.startswith(currentText.lower()):
					# Set the search prediction
					self.snipeIgnoreEvtText2 = True
					self.snipeSearch2.SetValue(choice)
					self.snipeSearch2.SetInsertionPoint(len(currentText))
					self.snipeSearch2.SetSelection(len(currentText), len(choice))

					# Set the tribe abbreviation
					self.snipeTribe2.SetValue(self.helper.findUserInfo("tribeFromUser",choice))

					# Find Villages
					userID = self.helper.findUserInfo("idFromUser", currentText)
					villages = self.helper.findVillage(userID)
					self.villageListStorage2 = self.helper.rowToVillage(villages)
					queryVillages = []
					for i in range(0, len(self.villageListStorage2)):
						queryVillages.append(self.villageListStorage2[i][2])
					self.snipeAttackingVillage.SetItems(queryVillages)

					found = True
					break
			if not found:
				event.Skip()
		else:
			event.Skip()

	def snipeSearchClear2(self, event):
		self.snipeSearch2.Clear()
		self.snipeTribe2.Clear()
		self.snipeAttackingVillage.SetItems([])
		self.snipeIgnoreEvtText2 = True

	def attackTimerGoPress(self, event):
		Thread(target = self.attackTimerThread).start()

	def attackTimerThread(self):
		# get the target village
		target = self.villageListStorage1[self.snipeDefendingVillage.GetSelection()][1]

		# get the destination villages
		sendLocations = self.snipeAttackingVillage.GetSelections()
		sendLocationCoordinates = []
		for i in sendLocations:
			sendLocationCoordinates.append(self.villageListStorage2[i])

		# get the unit speeds
		# yes, this is very messy
		self.helper.speeds = []
		if self.snipeSpeedPal.IsChecked():
			self.helper.speeds.append("pal")
		if self.snipeSpeedSc.IsChecked():
			self.helper.speeds.append("sc")
		if self.snipeSpeedLc.IsChecked():
			self.helper.speeds.append("lc")
		if self.snipeSpeedHc.IsChecked():
			self.helper.speeds.append("hc")
		if self.snipeSpeedSp.IsChecked():
			self.helper.speeds.append("sp")
		if self.snipeSpeedSw.IsChecked():
			self.helper.speeds.append("sw")
		if self.snipeSpeedRam.IsChecked():
			self.helper.speeds.append("ram")
		if self.snipeSpeedNob.IsChecked():
			self.helper.speeds.append("noble")


		attackDate = self.attackArriveDate.GetValue()
		attackTime = self.attackArriveTime.GetValue()
		milliseconds = self.attackArriveMilliseconds.GetValue()
		timeString = str(attackDate.day) + "." + str(attackDate.month + 1) + "." + str(attackDate.year) + " " + str(attackTime.hour) + ":" + str(attackTime.minute) + ":" + str(attackTime.second) + "." + str(milliseconds)
		# get the timing string
		string = self.helper.getSnipeString2(target, timeString, self.snipeBBcode.IsChecked(), self.snipeSort.IsChecked(), sendLocationCoordinates)
		self.attackTimerOutput.SetValue(string) # put the timing string in the output window

	# when go is clicked
	def farmSearchUpdate(self,event):
		if self.farmIgnoreEvtText:
			self.farmIgnoreEvtText = False
			return
		currentText = event.GetString()
		if currentText != "":
			found = False
			for choice in self.helper.tribesCol[2]:
				if choice.startswith(currentText):
					self.farmIgnoreEvtText = True
					self.farmSearchAbbrev.SetValue(choice)
					self.farmSearchAbbrev.SetInsertionPoint(len(currentText))
					self.farmSearchAbbrev.SetSelection(len(currentText), len(choice))
					found = True
					break
			if not found:
				event.Skip()
		else:
			event.Skip()

	def farmSearchClear(self, event):
		self.farmSearchAbbrev.Clear()
		self.farmIgnoreEvtText = True

	# when go is clicked
	def getList(self,event):
		try:
			# start a new thread with 
			Thread(target = self.fillMemberList).start()
		except Exception as e:
			traceback.print_exc()
			print('error')

	def fillMemberList(self):
		# get the input type
		typ = self.farmType.GetString(self.farmType.GetSelection())

		# get desired list ordering
		order = self.farmOrder.GetString(self.farmOrder.GetSelection())
		if order == "Ascending" or order == "Descending":
			descending = False
			if order == "Descending":
				descending = True
			order = True
		else:
			order = False
			descending = False

		# do we want to spit out results with BB codes?
		check = self.farmBBcode.IsChecked()

		# print information to display before we run
		self.farmMemberList.SetValue(str("Processing data... this may take some time."))

		# get the ranking list string
		string = self.farmRankList(self.farmSearchAbbrev.GetValue(), order = order, descending = descending, type = typ, bbcode = check)
		self.farmMemberList.SetValue(string) # print the list to display

	def farmRankList(self, tribeAbbrev, order = False, descending = True, bbcode = True, type = "Hauls"):
		'''Get the farm ranks of a tribe.'''
		# reset values
		self.helper.plunderList = []
		self.helper.haulList = []
		self.helper.plunderListString = ''
		self.helper.haulListString = ''
		string = ''

		# get the member list
		members = self.helper.getTribeMembers(tribeAbbrev)
		for i in range(0, len(members)):
		# for each tribe member
			self.twHelperLog.SetValue("[" + str(i + 1) + "/" + str(len(members)) + "]\n") # update the progress value in the log
			self.helper.getInDayInfo(members[i], type) # get info for member[i]
			
		self.twHelperLog.AppendText("Finished getting info for " + tribeAbbrev) # pri nt that we are finished to the log
		
		# turn our list of member ranks into a string
		if type == "Plunders":
			string = self.helper.farmRankProcessList(self.helper.plunderList, order = order, descending = descending, bbcode = bbcode, title = "Total Plunders")
		else:
			string = self.helper.farmRankProcessList(self.helper.haulList, order = order, descending = descending, bbcode = bbcode, title = "Total Haul")

		return string

if __name__ == '__main__':
	# initialize app
	app = wx.App(False)

	# create an object of CalcFrame
	frame = twHelperMain(None)
	# show the frame
	frame.Show(True)
	# start the applications
	app.MainLoop()