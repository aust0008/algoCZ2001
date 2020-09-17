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

    def KMPSearch(self,pat, txt):
        M = len(pat)
        N = len(txt)
        # create lps[] that will hold the longest prefix suffix
        # values for pattern
        lps = [0]*M
        j = 0  # index for pat[]
        # Preprocess the pattern (calculate lps[] array)
        start = time.time()
        count = 0
        self.computeLPSArray(pat, M, lps)
        i = 0  # index for txt[]
        while i < N:
            if pat[j] == txt[i]:
                i += 1
                j += 1

            # mismatch after j matches
            #elif i < N and pat[j] != txt[i]:
            else:
                # Do not match lps[0..lps[j-1]] characters,
                # they will match anyway
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1
            if j == M:
                print("Found pattern at index " + str(i-j))
                count += 1
                j = lps[j-1]
        end = time.time()
        print("End of search")
        print("Time taken = "  + str(end-start))
        print(count)

    def computeLPSArray(self,pat, M, lps):
        len = 0  # length of the previous longest prefix suffix

        lps[0]  # lps[0] is always 0
        i = 1
        # the loop calculates lps[i] for i = 1 to M-1
        while i < M:
            if pat[i] == pat[len]:
                len += 1
                lps[i] = len
                i += 1
            else:
                # This is tricky. Consider the example.
                # AAACAAAA and i = 7. The idea is similar
                # to search step.
                if len != 0:
                    len = lps[len-1]

                    # Also, note that we do not increment i here
                else:
                    lps[i] = 0
                    i += 1


    def displayOutput(self):
        global pat,txt
        pat = str(self.ui.inputTxt.text())
        txt = str(my_file_contents)
        self.KMPSearch(pat, txt)

    def getfiles(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File', QtCore.QDir.rootPath(), '*.fna')
        self.ui.fileUploadTxt.setText(fileName)
        my_file_name = str(self.ui.fileUploadTxt.text())
        my_file = open(my_file_name)
        global my_file_contents
        my_file_contents = my_file.read().rstrip("\n")
        my_file_contents = my_file_contents.replace('\n', '')
        print(my_file_contents)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
