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
        self.ui.typeComboBox.currentIndexChanged.connect(self.comboBoxReset)
    
    def comboBoxReset(self):
        self.ui.fileUploadTxt.setText("")
        self.ui.inputTxt.setText("")
        self.ui.outputTxt.setText("")

    def search(self,pat, txt):
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
                self.ui.outputTxt.append("Found pattern at index " + str(i-j))
                totalNumberOfPatternFound += 1
                i-= M - 1
                j=0
            
        end = time.time()
        print("End of search")
        print("Time taken = "  + str(end-start))
        print(totalNumberOfPatternFound)


    def StringSearch(self, pat, txt): 
        M = len(pat) 
        N = len(txt)
        #indexM indicates the highest index of the pattern string
        indexM = M-1
        count=0
        i= indexM
        j= indexM
        backtrack = 1
        shift=0
        count = 0
         # To indicate where should the next index[i] move to 
        ptr = indexM
        start = time.perf_counter()
        while i<N:
            if j>=0:
                # final character of pattern matches
                if txt[i] == pat[j]:
                    i-=1
                    j-=1

                else:
                    # check if current text index matches if it matches pattern for index j-backtrack
                    if txt[i] == pat[j-backtrack]:
                        j = j-backtrack
                        #to let the program know how many index it should move forward
                        shift = indexM-j
                        # shifting the i according to where the j matches with the current i
                        i= i+shift
                        #reset j to the last character of the pattern
                        j=indexM
                        #shift the pointer to the next character it is supposed to point to 
                        ptr=i
                        #reset the backtrack to 1
                        backtrack=1
                    else:
                        backtrack +=1
                        if j-backtrack < 0:
                            #when index i doesnt appear in any of the M, shift i by the length of the pattern
                            i+=M
                            #reset j to the last character of the pattern
                            j=indexM
                            #reset the backtrack to 1
                            backtrack=1
                            #set the pointer to where i is currently at
                            ptr = i
            
            if j<0:
                #shift i to the next character
                i+=1
                #set pointer to the next character
                ptr+=1
                print("Pattern found at index ", i)
                self.ui.outputTxt.append("Found pattern at index " + str(i))

                #increment the number of pattern found
                count+=1
                # set i to the character it is supposed to point to
                i=ptr
                #reset j to the last character 
                j=indexM
                #when all the txt string has reached the end, exit loop
                if i==N-1:
                    break

        end = time.perf_counter()
        print("End of search")
        if count==0:
            self.ui.outputTxt.append("No matches found, please try with a new input")
        self.ui.outputTxt.append("Time taken = "  + str(end-start))
        print("Time taken = "  + str(end-start))
        self.ui.outputTxt.append("Count = "  + str(count))
        print(count) 
        
   
    def displayOutput(self):
        global pat,txt
        pat = str(self.ui.inputTxt.text())
        txt = str(my_file_contents)
        if (self.ui.typeComboBox == 0):
            self.search(pat, txt)
        else:
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