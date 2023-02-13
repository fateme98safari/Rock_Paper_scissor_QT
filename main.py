import random
from functools import partial
from PySide6.QtWidgets import QApplication,QMessageBox
from PySide6.QtUiTools import QUiLoader

def win():
    global comp_score
    global user_score
    if int(user_score)==3 and int(comp_score)<int(user_score):
        window.lineEdit_3.setText("🎉YOU WIN🎉")
        msg_box=QMessageBox()
        msg_box.setText("play again?")
        msg_box.exec()
        user_score=0
        comp_score=0
        window.lineEdit_2.setText("")
        window.lineEdit_3.setText("")
        window.lineEdit_6.setText("")
        window.lineEdit_7.setText("")
        window.lineEdit_5.setText("")

    elif int(comp_score)==3 and int(user_score) < int(comp_score):
        window.lineEdit_3.setText("🎉COMPUTER WIN🎉")
        QMessageBox.information("Information" , "Game is finished")
        msg_box=QMessageBox()
        msg_box.setText("play again?")
        msg_box.exec()
        user_score=0
        comp_score=0
        window.lineEdit_2.setText("")
        window.lineEdit_3.setText("")
        window.lineEdit_6.setText("")
        window.lineEdit_7.setText("")
        window.lineEdit_5.setText("")

comp_score=0
user_score=0
def check():
    global comp_score
    global user_score
  
    if window.lineEdit_2.text()=="Rock" and window.lineEdit_5.text()=="Paper":
        user_score +=1
        window.lineEdit_7.setText(str(user_score))
        win()

    elif window.lineEdit_2.text()=="Rock" and window.lineEdit_5.text()=="Scissor":
        comp_score +=1
        window.lineEdit_6.setText(str(comp_score))
        win()
      
    elif window.lineEdit_2.text()=="Paper" and window.lineEdit_5.text()=="Rock":
        comp_score +=1
        window.lineEdit_6.setText(str(comp_score))
        win()
        
    elif window.lineEdit_2.text()=="Paper" and window.lineEdit_5.text()=="Scissor":
        user_score +=1
        window.lineEdit_7.setText(str(user_score))
        win()
        
    elif window.lineEdit_2.text()=="Scissor" and window.lineEdit_5.text()=="Rock":
        user_score +=1
        window.lineEdit_7.setText(str(user_score))
        win()
        
    elif window.lineEdit_2.text()=="Scissor" and window.lineEdit_5.text()=="Paper":
        comp_score+=1
        window.lineEdit_6.setText(str(comp_score))
        win()
       
    

status="player"

app=QApplication([])
loader=QUiLoader()
window=loader.load("RPS.ui")
window.setWindowTitle("RockPaperScissors")

# window.setGeometry(900,200,250,300)
window.show()
# while score_computer==3 or score_player==3:
def play(x):
    
        global status
        global user_choice
        global comp_choice
        if status=="player":
            window.lineEdit_5.setText(x)
            user_choice=x
            status="computer"
        # for i in range(5):
        if status=="computer":
            comp_choice=random.randint(1,3)
            if comp_choice==1:
                window.lineEdit_2.setText("Rock")
                status="player"
                check()
            elif comp_choice==2:
                window.lineEdit_2.setText("Paper")
                status="player"
                check()
            elif comp_choice==3:
                window.lineEdit_2.setText("Scissor")
                status="player"
                check()


window.pbrock.clicked.connect(partial (play , "Rock"))
window.pbpaper.clicked.connect(partial (play , "Paper"))
window.pbsci.clicked.connect(partial (play , "Scissor"))



app.exec()