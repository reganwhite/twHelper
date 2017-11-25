# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Nov  6 2017)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.adv

###########################################################################
## Class mainFrame
###########################################################################

class mainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"twHelper", pos = wx.DefaultPosition, size = wx.Size( 393,548 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		wSizer3 = wx.WrapSizer( wx.VERTICAL )
		
		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.inDayPanel = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		wSizer2 = wx.WrapSizer( wx.HORIZONTAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3 = wx.StaticText( self.inDayPanel, wx.ID_ANY, u"Tribe Affix", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer2.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.farmSearchAbbrev = wx.SearchCtrl( self.inDayPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.farmSearchAbbrev.ShowSearchButton( False )
		self.farmSearchAbbrev.ShowCancelButton( True )
		self.farmSearchAbbrev.SetMinSize( wx.Size( 100,-1 ) )
		
		bSizer2.Add( self.farmSearchAbbrev, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.farmSearchGo = wx.Button( self.inDayPanel, wx.ID_ANY, u"Go", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.farmSearchGo, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		wSizer2.Add( bSizer2, 1, wx.EXPAND|wx.TOP, 5 )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.inDayPanel, wx.ID_ANY, u"Settings" ), wx.HORIZONTAL )
		
		self.farmBBcode = wx.CheckBox( sbSizer2.GetStaticBox(), wx.ID_ANY, u"BBCodes", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.farmBBcode.SetValue(True) 
		sbSizer2.Add( self.farmBBcode, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		farmTypeChoices = [ u"Plunders", u"Hauls" ]
		self.farmType = wx.Choice( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, farmTypeChoices, 0 )
		self.farmType.SetSelection( 0 )
		sbSizer2.Add( self.farmType, 0, wx.ALL, 5 )
		
		farmOrderChoices = [ u"Descending", u"Ascending", u"No Order" ]
		self.farmOrder = wx.Choice( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, farmOrderChoices, 0 )
		self.farmOrder.SetSelection( 0 )
		sbSizer2.Add( self.farmOrder, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		wSizer2.Add( sbSizer2, 1, wx.BOTTOM|wx.EXPAND, 5 )
		
		self.farmMemberList = wx.TextCtrl( self.inDayPanel, wx.ID_ANY, u"Tribe information will be printed here.", wx.DefaultPosition, wx.Size( 273,-1 ), wx.TE_DONTWRAP|wx.TE_MULTILINE|wx.TE_READONLY )
		self.farmMemberList.SetMinSize( wx.Size( 273,150 ) )
		
		wSizer2.Add( self.farmMemberList, 0, wx.BOTTOM|wx.RIGHT|wx.TOP, 5 )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.inDayPanel, wx.ID_ANY, u"Log" ), wx.VERTICAL )
		
		self.twHelperLog = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 260,80 ), wx.TE_MULTILINE|wx.TE_READONLY )
		sbSizer3.Add( self.twHelperLog, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		wSizer2.Add( sbSizer3, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 2 )
		
		
		self.inDayPanel.SetSizer( wSizer2 )
		self.inDayPanel.Layout()
		wSizer2.Fit( self.inDayPanel )
		self.m_notebook1.AddPage( self.inDayPanel, u"In A Day", False )
		self.m_panel2 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer9 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )
		
		wSizer8 = wx.WrapSizer( wx.HORIZONTAL )
		
		defendingPlayer = wx.StaticBoxSizer( wx.StaticBox( self.m_panel2, wx.ID_ANY, u"Defending Player" ), wx.VERTICAL )
		
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.snipeLabel = wx.StaticText( defendingPlayer.GetStaticBox(), wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.snipeLabel.Wrap( -1 )
		bSizer6.Add( self.snipeLabel, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.snipeSearch = wx.SearchCtrl( defendingPlayer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.snipeSearch.ShowSearchButton( False )
		self.snipeSearch.ShowCancelButton( True )
		self.snipeSearch.SetMaxSize( wx.Size( 125,-1 ) )
		
		bSizer6.Add( self.snipeSearch, 0, wx.ALL, 5 )
		
		self.snipeTribe = wx.TextCtrl( defendingPlayer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.snipeTribe.SetMaxSize( wx.Size( 70,-1 ) )
		
		bSizer6.Add( self.snipeTribe, 0, wx.ALL, 5 )
		
		
		defendingPlayer.Add( bSizer6, 1, wx.EXPAND, 5 )
		
		snipeDefendingVillageChoices = []
		self.snipeDefendingVillage = wx.ListBox( defendingPlayer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, snipeDefendingVillageChoices, wx.LB_ALWAYS_SB|wx.LB_SINGLE|wx.LB_SORT )
		self.snipeDefendingVillage.SetMinSize( wx.Size( 250,80 ) )
		self.snipeDefendingVillage.SetMaxSize( wx.Size( 250,80 ) )
		
		defendingPlayer.Add( self.snipeDefendingVillage, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		wSizer8.Add( defendingPlayer, 1, wx.EXPAND|wx.TOP, 5 )
		
		attackingPlayer = wx.StaticBoxSizer( wx.StaticBox( self.m_panel2, wx.ID_ANY, u"Attacking Player" ), wx.VERTICAL )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.snipeLabel2 = wx.StaticText( attackingPlayer.GetStaticBox(), wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.snipeLabel2.Wrap( -1 )
		bSizer4.Add( self.snipeLabel2, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.snipeSearch2 = wx.SearchCtrl( attackingPlayer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.snipeSearch2.ShowSearchButton( False )
		self.snipeSearch2.ShowCancelButton( True )
		self.snipeSearch2.SetMaxSize( wx.Size( 125,-1 ) )
		
		bSizer4.Add( self.snipeSearch2, 0, wx.ALL, 5 )
		
		self.snipeTribe2 = wx.TextCtrl( attackingPlayer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.snipeTribe2.SetMaxSize( wx.Size( 70,-1 ) )
		
		bSizer4.Add( self.snipeTribe2, 0, wx.ALL, 5 )
		
		
		attackingPlayer.Add( bSizer4, 0, wx.EXPAND, 5 )
		
		snipeAttackingVillageChoices = []
		self.snipeAttackingVillage = wx.ListBox( attackingPlayer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,80 ), snipeAttackingVillageChoices, wx.LB_ALWAYS_SB|wx.LB_MULTIPLE|wx.LB_SORT )
		self.snipeAttackingVillage.SetMinSize( wx.Size( 250,80 ) )
		self.snipeAttackingVillage.SetMaxSize( wx.Size( 250,80 ) )
		
		attackingPlayer.Add( self.snipeAttackingVillage, 0, wx.ALL, 5 )
		
		
		wSizer8.Add( attackingPlayer, 1, wx.EXPAND, 5 )
		
		
		bSizer5.Add( wSizer8, 1, wx.EXPAND|wx.RIGHT, 5 )
		
		wSizer9 = wx.WrapSizer( wx.VERTICAL )
		
		wSizer9.SetMinSize( wx.Size( -1,300 ) ) 
		speeds = wx.StaticBoxSizer( wx.StaticBox( self.m_panel2, wx.ID_ANY, u"Speeds" ), wx.VERTICAL )
		
		self.snipeSpeedNob = wx.CheckBox( speeds.GetStaticBox(), wx.ID_ANY, u"Nob", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.snipeSpeedNob.SetValue(True) 
		speeds.Add( self.snipeSpeedNob, 0, wx.ALL, 5 )
		
		self.snipeSpeedRam = wx.CheckBox( speeds.GetStaticBox(), wx.ID_ANY, u"Ram", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.snipeSpeedRam.SetValue(True) 
		speeds.Add( self.snipeSpeedRam, 0, wx.ALL, 5 )
		
		self.snipeSpeedSw = wx.CheckBox( speeds.GetStaticBox(), wx.ID_ANY, u"Sw", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.snipeSpeedSw.SetValue(True) 
		speeds.Add( self.snipeSpeedSw, 0, wx.ALL, 5 )
		
		self.snipeSpeedSp = wx.CheckBox( speeds.GetStaticBox(), wx.ID_ANY, u"Sp", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.snipeSpeedSp.SetValue(True) 
		speeds.Add( self.snipeSpeedSp, 0, wx.ALL, 5 )
		
		self.snipeSpeedHc = wx.CheckBox( speeds.GetStaticBox(), wx.ID_ANY, u"Hc", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.snipeSpeedHc.SetValue(True) 
		speeds.Add( self.snipeSpeedHc, 0, wx.ALL, 5 )
		
		self.snipeSpeedLc = wx.CheckBox( speeds.GetStaticBox(), wx.ID_ANY, u"Lc", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.snipeSpeedLc.SetValue(True) 
		speeds.Add( self.snipeSpeedLc, 0, wx.ALL, 5 )
		
		self.snipeSpeedSc = wx.CheckBox( speeds.GetStaticBox(), wx.ID_ANY, u"Sc", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.snipeSpeedSc.SetValue(True) 
		speeds.Add( self.snipeSpeedSc, 0, wx.ALL, 5 )
		
		self.snipeSpeedPal = wx.CheckBox( speeds.GetStaticBox(), wx.ID_ANY, u"Pal", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.snipeSpeedPal.SetValue(True) 
		speeds.Add( self.snipeSpeedPal, 0, wx.ALL, 5 )
		
		
		wSizer9.Add( speeds, 1, wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, 5 )
		
		self.snipeSort = wx.CheckBox( self.m_panel2, wx.ID_ANY, u"Sort", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.snipeSort.SetValue(True) 
		wSizer9.Add( self.snipeSort, 0, wx.ALL, 5 )
		
		self.snipeBBcode = wx.CheckBox( self.m_panel2, wx.ID_ANY, u"BBcode", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.snipeBBcode.SetValue(True) 
		wSizer9.Add( self.snipeBBcode, 0, wx.ALL, 5 )
		
		
		bSizer5.Add( wSizer9, 0, wx.ALL, 5 )
		
		
		bSizer9.Add( bSizer5, 1, wx.EXPAND, 5 )
		
		wSizer81 = wx.WrapSizer( wx.HORIZONTAL )
		
		self.m_staticText5 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Time:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		wSizer81.Add( self.m_staticText5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.attackArriveDate = wx.adv.DatePickerCtrl( self.m_panel2, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.DP_DEFAULT|wx.adv.DP_SPIN )
		wSizer81.Add( self.attackArriveDate, 0, wx.ALL, 5 )
		
		self.attackArriveTime = wx.adv.TimePickerCtrl( self.m_panel2, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.DefaultSize, wx.adv.TP_DEFAULT )
		self.attackArriveTime.SetMinSize( wx.Size( 85,-1 ) )
		
		wSizer81.Add( self.attackArriveTime, 0, wx.ALL, 5 )
		
		self.attackArriveMilliseconds = wx.SpinCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 50,-1 ), wx.SP_ARROW_KEYS, 0, 999, 0 )
		wSizer81.Add( self.attackArriveMilliseconds, 0, wx.ALL, 5 )
		
		
		bSizer9.Add( wSizer81, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.attackTimerGo = wx.Button( self.m_panel2, wx.ID_ANY, u"Go!", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.attackTimerGo.SetMinSize( wx.Size( 65,-1 ) )
		
		bSizer9.Add( self.attackTimerGo, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		wSizer91 = wx.WrapSizer( wx.HORIZONTAL )
		
		self.attackTimerOutput = wx.TextCtrl( self.m_panel2, wx.ID_ANY, u"The output will print to here.", wx.DefaultPosition, wx.Size( 300,100 ), wx.TE_DONTWRAP|wx.TE_MULTILINE|wx.TE_READONLY )
		wSizer91.Add( self.attackTimerOutput, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		bSizer9.Add( wSizer91, 0, wx.ALIGN_CENTER, 5 )
		
		
		self.m_panel2.SetSizer( bSizer9 )
		self.m_panel2.Layout()
		bSizer9.Fit( self.m_panel2 )
		self.m_notebook1.AddPage( self.m_panel2, u"Attack Timer", True )
		self.configPanel = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		wSizer41 = wx.WrapSizer( wx.HORIZONTAL )
		
		m_choice3Choices = []
		self.m_choice3 = wx.Choice( self.configPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice3Choices, 0 )
		self.m_choice3.SetSelection( 0 )
		wSizer41.Add( self.m_choice3, 0, wx.ALL, 5 )
		
		
		self.configPanel.SetSizer( wSizer41 )
		self.configPanel.Layout()
		wSizer41.Fit( self.configPanel )
		self.m_notebook1.AddPage( self.configPanel, u"Config", False )
		
		wSizer3.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( wSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.farmSearchAbbrev.Bind( wx.EVT_SEARCHCTRL_CANCEL_BTN, self.farmSearchClear )
		self.farmSearchAbbrev.Bind( wx.EVT_TEXT, self.farmSearchUpdate )
		self.farmSearchGo.Bind( wx.EVT_BUTTON, self.getList )
		self.snipeSearch.Bind( wx.EVT_SEARCHCTRL_CANCEL_BTN, self.snipeSearchClear )
		self.snipeSearch.Bind( wx.EVT_TEXT, self.snipeUpdateSearch )
		self.snipeDefendingVillage.Bind( wx.EVT_LISTBOX_DCLICK, self.snipeDefendingVillageSelect )
		self.snipeSearch2.Bind( wx.EVT_SEARCHCTRL_CANCEL_BTN, self.snipeSearchClear2 )
		self.snipeSearch2.Bind( wx.EVT_TEXT, self.snipeUpdateSearch2 )
		self.snipeAttackingVillage.Bind( wx.EVT_LISTBOX_DCLICK, self.snipeDefendingVillageSelect )
		self.attackTimerGo.Bind( wx.EVT_BUTTON, self.attackTimerGoPress )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def farmSearchClear( self, event ):
		event.Skip()
	
	def farmSearchUpdate( self, event ):
		event.Skip()
	
	def getList( self, event ):
		event.Skip()
	
	def snipeSearchClear( self, event ):
		event.Skip()
	
	def snipeUpdateSearch( self, event ):
		event.Skip()
	
	def snipeDefendingVillageSelect( self, event ):
		event.Skip()
	
	def snipeSearchClear2( self, event ):
		event.Skip()
	
	def snipeUpdateSearch2( self, event ):
		event.Skip()
	
	
	def attackTimerGoPress( self, event ):
		event.Skip()
	

