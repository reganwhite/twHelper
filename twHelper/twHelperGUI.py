# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Nov  6 2017)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class mainFrame
###########################################################################

class mainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"twHelper", pos = wx.DefaultPosition, size = wx.Size( 315,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.Size( 315,480 ), wx.Size( 315,480 ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		wSizer3 = wx.WrapSizer( wx.VERTICAL )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Tribe Farming Checker" ), wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Tribe Affix", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer2.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.farmTribeAbbrev = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.farmTribeAbbrev, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.farmButton = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Go", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.farmButton, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		sbSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Settings" ), wx.HORIZONTAL )
		
		self.farmBBcode = wx.CheckBox( sbSizer2.GetStaticBox(), wx.ID_ANY, u"BBCode", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.farmBBcode.SetValue(True) 
		sbSizer2.Add( self.farmBBcode, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		farmTypeChoices = [ u"Plunders", u"Hauls" ]
		self.farmType = wx.Choice( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, farmTypeChoices, wx.CB_SORT )
		self.farmType.SetSelection( 1 )
		sbSizer2.Add( self.farmType, 0, wx.ALL, 5 )
		
		farmOrderChoices = [ u"Ascending", u"Descending", u"No Order" ]
		self.farmOrder = wx.Choice( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, farmOrderChoices, wx.CB_SORT )
		self.farmOrder.SetSelection( 0 )
		sbSizer2.Add( self.farmOrder, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		sbSizer1.Add( sbSizer2, 1, wx.EXPAND, 5 )
		
		self.memberList = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,200 ), wx.HSCROLL|wx.TE_MULTILINE|wx.TE_READONLY )
		self.memberList.SetMaxSize( wx.Size( -1,200 ) )
		
		sbSizer1.Add( self.memberList, 0, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		wSizer3.Add( sbSizer1, 1, wx.BOTTOM|wx.LEFT|wx.RIGHT|wx.TOP, 5 )
		
		self.twHelperLog = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,70 ), wx.HSCROLL|wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL|wx.VSCROLL )
		self.twHelperLog.SetMinSize( wx.Size( -1,70 ) )
		self.twHelperLog.SetMaxSize( wx.Size( -1,70 ) )
		
		wSizer3.Add( self.twHelperLog, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( wSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.farmButton.Bind( wx.EVT_BUTTON, self.getList )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def getList( self, event ):
		event.Skip()
	

