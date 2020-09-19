from PyQt5 import QtWidgets, QtCore, QtGui

import algodna
import time
class MyWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.ui = algodna.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.uploadBtn.clicked.connect(self.getfiles)
        self.ui.submitBtn.clicked.connect(self.displayOutput)

    def StringSearch(self,pat, txt):
        M = len(pat)
        N = len(txt) 

        # index for the fna file
        i = 0
        # index for string query
        j = 0
        start = time.time()
        totalNumberOfPatternFound = 0
    
        while i < N:

            #when char of string and fna file matches
            if pat[j] == txt[i]:
                i += 1
                j += 1

            # proceed to next index for both string query and fna
            else:

                #if mismatch occur after initial match
                if j != 0:
                    # to know how many char in the string has been searched
                    j = j-1
                    # set index of string to backtrack
                    i-=j
                    #restart comparison of the string query from the first character
                    j=0

                    
                else:
                    #increase fna index to compare next char
                    i += 1
            # if string query matches fna indexes, return index found at
            if j == M:
                print("Found pattern at index " + str(i-j))
                totalNumberOfPatternFound += 1
                i-= M - 1
                j=0
        end = time.time()
        print("End of search")
        print("Time taken = "  + str(end-start))
        print(totalNumberOfPatternFound)


    def displayOutput(self):
        global pat,txt
        pat = str(self.ui.inputTxt.text())
        txt = str(my_file_contents)
        self.StringSearch(pat, txt)

    def getfiles(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File', QtCore.QDir.rootPath(), '*.fna')
        self.ui.fileUploadTxt.setText(fileName)
        my_file_name = str(self.ui.fileUploadTxt.text())
        my_file = open(my_file_name)
        global my_file_contents
        my_file_contents = my_file.read().rstrip("\n")
        my_file_contents = my_file_contents.replace('\n', '')

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
