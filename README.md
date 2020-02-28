# rhythm-generator
My personal project that generates random rhythm exercises

Useful for producing clapping exercises for students or to test your own rhythmic accuracy

## **How to Use:**

Simply run main.py and enter the difficulty of the exercise and the number of bars to create

Press generate and a window will open with the sheet music of the exercise

The sheet music can also be saved or printed


## **Running the Code:**

This program currently only supports Windows and has a few dependencies which need to be installed

[wxPython](https://wxpython.org/) is used for the GUI\
Install with `pip install -U wxPython`  

[LilyPond](http://lilypond.org/) is used for the creation of the sheet music\
Download the installer from [here](http://lilypond.org/windows.html) and make sure to add LilyPond to the PATH environment variable as shown on the webpage

I have tested the code on OSX and after following the instructions [here](https://stackoverflow.com/questions/48531006/wxpython-this-program-needs-access-to-the-screen) it runs. However, the PDF file gets saved in the main directory rather than displayed by wxPython (PDFWindow only supports Windows) and the layout of the interface isn't right. I will test on Linux soon.

## **Future Plans:**

* Add more time signatures (currently only outputs in 4/4)
* Add more rhythm patterns (and make a better system for creating them)
* Add the ability to change time signatures during the exercise
* Add support for ties
* Add a playback feature which can demonstrate the correct rhythms
* Add the abilty to generate multiple exercises in one document
* Add cross-platform support (i.e. replace wxPython): PDFWindow from wxPython only supports Windows and wxPython has issues with OSX so I need to use something else

## **Attributions**

Icon made by [Freepik](https://www.flaticon.com/authors/freepik) from [www.flaticon.com](www.flaticon.com)
