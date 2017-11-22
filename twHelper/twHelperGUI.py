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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"twHelper", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		wSizer3 = wx.WrapSizer( wx.VERTICAL )
		
		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel1 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		wSizer2 = wx.WrapSizer( wx.HORIZONTAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Tribe Affix", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer2.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.farmTribeAbbrev = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.farmTribeAbbrev, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.m_button1 = wx.Button( self.m_panel1, wx.ID_ANY, u"Go", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		wSizer2.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"Settings" ), wx.HORIZONTAL )
		
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
		
		
		wSizer2.Add( sbSizer2, 1, wx.EXPAND, 5 )
		
		self.farmMemberList = wx.TextCtrl( self.m_panel1, wx.ID_ANY, u"Tribe information will be printed here.", wx.DefaultPosition, wx.Size( 273,-1 ), wx.TE_DONTWRAP|wx.TE_MULTILINE|wx.TE_READONLY )
		self.farmMemberList.SetMinSize( wx.Size( 273,150 ) )
		
		wSizer2.Add( self.farmMemberList, 0, wx.BOTTOM|wx.RIGHT, 5 )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"Log" ), wx.VERTICAL )
		
		self.twHelperLog = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 260,80 ), wx.TE_MULTILINE|wx.TE_READONLY )
		sbSizer3.Add( self.twHelperLog, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		wSizer2.Add( sbSizer3, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 2 )
		
		
		self.m_panel1.SetSizer( wSizer2 )
		self.m_panel1.Layout()
		wSizer2.Fit( self.m_panel1 )
		self.m_notebook1.AddPage( self.m_panel1, u"In A Day", True )
		self.m_panel2 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_notebook1.AddPage( self.m_panel2, u"a page", False )
		
		wSizer3.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( wSizer3 )
		self.Layout()
		wSizer3.Fit( self )
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.getList )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def getList( self, event ):
		event.Skip()
	

