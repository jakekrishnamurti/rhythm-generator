import wx
if wx.Platform == '__WXMSW__':
    from wx.lib.pdfwin import PDFWindow

import rhythm_generator as rg

import os


#This window displays the generated PDF file
class RhythmWindow(wx.Frame):

    #Initialise window and set icon
    def __init__(self, *args, **kw):
        super(RhythmWindow, self).__init__(None, title='Rhythms', style=wx.DEFAULT_FRAME_STYLE)

        ico = wx.Icon('files/icon.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(ico)

        self.DisplayPDF()


    #Load the PDF file into the window
    def DisplayPDF(self):

        panel = wx.Panel(self)
        
        panel_sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.pdf = PDFWindow(panel, style=wx.SUNKEN_BORDER)
        
        panel_sizer.Add(self.pdf, proportion=1, flag=wx.EXPAND)

        
        panel.SetSizer(panel_sizer)
        panel.SetAutoLayout(True)

        self.pdf.LoadFile("files/Rhythms.pdf")

        #Delete the PDF and ly files once loaded as we don't need them anymore
        os.remove("files/Rhythms.pdf")
        os.remove("files/Rhythms.ly")


        self.SetSize((1280, 800))
        self.Centre()
        self.Show(True)


        
#This window lets the user control the rhythms to be generated
class MainWindow(wx.Frame):

    #Initialise window and set icon      
    def __init__(self, *args, **kw):
        super(MainWindow, self).__init__(None, title='Rhythm Generator', style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX)

        self.difficulty = 1
        self.bars = 1

        self.generated = False

        ico = wx.Icon('files/icon.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(ico)

        self.CreateUI()

        

    #Create the widgets for the user to interact with   
    def CreateUI(self):   

        panel = wx.Panel(self)


        difficulty_text = wx.StaticText(panel, label="Select Difficulty (1=easy, 5=difficult):",  pos=(20,10)) 
        difficulties = ['1', '2', '3', '4', '5']
        self.difficulty_combo = wx.ComboBox(panel, value='1', pos=(220,8), size=(140, 20), choices=difficulties, style=wx.CB_READONLY)


        bars_text = wx.StaticText(panel, label="Enter the number of bars:",  pos=(80,50))
        self.bars_spin = wx.SpinCtrl(panel, value='1', pos=(220, 48), size=(60, -1), min=1, max=200) #Max of 200 bars

        
        generate_button = wx.Button(panel, label='Generate', pos=(160, 90), size=(80,25))
        generate_button.Bind(wx.EVT_BUTTON, self.Generate)

        
        self.SetSize((400, 160))
        self.Centre()
        self.Show(True)          


    #Generate the rhythms when the button is clicked    
    def Generate(self, e):

        self.difficulty = self.difficulty_combo.GetValue()
        self.bars = self.bars_spin.GetValue()

        rg.generate_rhythms(int(self.difficulty), int(self.bars))

        self.set_generated(True)

        self.Close()
        

    #Used so that the rhythm window won't be created unless a PDF was generated
    def check_generated(self):
        return self.generated

    def set_generated(self, value):
        self.generated = value

        
        
def main():

    #Create the main window
    rhythm_generator = wx.App()
    mw = MainWindow(None)
    rhythm_generator.MainLoop()

    #Only create the rhythm window if a PDF was generated and the platform is Windows (wxPython PDFWindow only works on Windows)
    if mw.check_generated() and wx.Platform == '__WXMSW__':
        rhythm_display = wx.App()
        RhythmWindow(None)
        rhythm_display.MainLoop()

if __name__ == '__main__':
    main() 
