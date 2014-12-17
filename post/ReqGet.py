#!/usr/local/bin/python
#coding=utf-8 
import wx
import urllib2
import urllib

class TextBox(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"Example For TextCtrl",size=(600,500))
        self.panel=wx.Panel(self,-1)
        self.param1=wx.StaticText(self.panel,-1,"param:")
        self.pvalue1=wx.TextCtrl(self.panel,-1,"",size=(175,-1))
        self.pvalue1.SetInsertionPoint(0)
        self.value=wx.StaticText(self.panel,-1,"value:")
        self.value1=wx.TextCtrl(self.panel,-1,"",size=(175,-1))
        self.value1.SetInsertionPoint(0)
        self.sub=wx.Button(self.panel,-1,"提交")
        self.Bind(wx.EVT_BUTTON,self.OnClick,self.sub)
        self.param2=wx.StaticText(self.panel,-1,"param:")
        self.pvalue2=wx.TextCtrl(self.panel,-1,"",size=(175,-1))
        self.pvalue2.SetInsertionPoint(0)
        self.nvalue2=wx.StaticText(self.panel,-1,"value:")
        self.value2=wx.TextCtrl(self.panel,-1,"",size=(175,-1))
        self.value2.SetInsertionPoint(0)
        self.result=wx.StaticText(self.panel,-1,"result:")
        self.json=wx.TextCtrl(self.panel,-1,"",size=(400,300),style=wx.TE_MULTILINE|wx.TE_RICH2)
        self.json.SetInsertionPoint(0)
        sizer=wx.GridBagSizer(5, 5)
        sizer.Add(self.param1,pos=(0,0),flag=wx.LEFT | wx.TOP)
        sizer.Add(self.pvalue1,pos=(0,1),flag=wx.TOP)
        sizer.Add(self.value,pos=(0,2),flag=wx.TOP)
        sizer.Add(self.value1,pos=(0,3),flag=wx.TOP)
        sizer.Add(self.sub,pos=(0,4))
        sizer.Add(self.param2,pos=(1,0))
        sizer.Add(self.pvalue2,pos=(1,1))
        sizer.Add(self.nvalue2,pos=(1,2))
        sizer.Add(self.value2,pos=(1,3))

        sizer.Add(self.result,pos=(2,0))
        sizer.Add(self.json,pos=(2,1),span=(2,3))
        self.panel.SetSizer(sizer)
        #style=wx.TE_MULTILINE|wx.TE_RICH2
    def OnClick(self,event):
        p1=self.pvalue1.GetValue()
        p2=self.pvalue2.GetValue()
        v1=self.value1.GetValue()
        v2=self.value2.GetValue()
        param={}
        if p1 != '' and v1 != '':
            param={p1:v1}
        if  p1 != '' and v1 != '' and p2 != '' and v2 != '':
            param={p1:v1,p2:v2}
        url='http://115.182.51.172:9003/qAllInfo'
        data=urllib.urlencode(param)
        req=urllib2.Request(url,data)
        res=urllib2.urlopen(req)
        jsons=res.read()
        self.json.SetValue(jsons)
class MyApp(wx.App):
    def OnInit(self):
        frame=TextBox()
        frame.Show(True)
        return True
def main():
    app=MyApp()
    app.MainLoop()
main()