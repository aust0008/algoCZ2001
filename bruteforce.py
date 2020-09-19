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

    def search(self, pat, txt): 
        M = len(pat) 
        N = len(txt) 
        count=0
        start = time.time()
        # A loop to slide pat[] one by one */ 
        for i in range(N - M + 1): 
            j = 0
            
            # For current index i, check  
            # for pattern match */ 
            while(j < M): 
                if (txt[i + j] != pat[j]): 
                    break
                j += 1
    
            if (j == M):  
                foundPattern = "Pattern found at index " + str(i)
                print("Pattern found at index ", i)
                count+=1
        end = time.time()
        print("End of search")
        print("Time taken = "  + str(end-start))
        print(count)
        self.ui.outputTxt.setText(foundPattern + "\nTime taken = " + str(end-start))


    def displayOutput(self):
        global pat,txt
        pat = str(self.ui.inputTxt.text())
        txt = str(my_file_contents)
        self.search(pat, txt)

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