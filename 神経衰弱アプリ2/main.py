from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color
from kivy.graphics import Rectangle
from kivy.graphics import Line
from kivy.graphics import Ellipse
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.behaviors import ButtonBehavior
import random
import time
from kivy.clock import Clock
Window.size=(360,640)

#アプリkivy.pyをダウンロード
Builder.load_file("アプリkivy.py")


swich=[1]



#画像ファイルのリストを作成
x=["ape.jpg","cat.jpg","cheetah.jpg","cow.jpg",\
"dog.jpg","eagle.jpg","lion.jpg","mallard.jpg",\
"wolf.jpg","zebra.jpg","ape.jpg","cat.jpg",\
"cheetah.jpg","cow.jpg","dog.jpg","eagle.jpg",\
"lion.jpg","mallard.jpg","wolf.jpg","zebra.jpg"]


y=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

card_list=["card1_1","card1_2","card1_3","card1_4","card2_1","card2_2","card2_3","card2_4",\
           "card3_1","card3_2","card3_3","card3_4","card4_1","card4_2","card4_3","card4_4",\
           "card5_1","card5_2","card5_3","card5_4"]

#card_list中の要素にそれぞれ重複２で画像ファイルを指定
for a in range (len(card_list)):
    number=random.choice(y)
    y.remove(number)
    source=x[number]
    card_list[a]=source
    print(card_list[a])




open_card_list=[]    
#screenmanagerにより画面の切り替えが可能
class Title(Screen):
    def title_clicked(self):
        
        sm.current="title2"
    pass


class Title2(Screen):
#card_listからトランプカードの表の画像ファイルを指定        
    def buttonclicked1(self):
        if len(swich)>=1:
            self.ids.btn1.canvas.clear()
            self.ids.btn1.canvas.add(Rectangle(pos=(self.ids.btn1.x+3,self.ids.btn1.y+3),size=(self.ids.btn1.width-5,self.ids.btn1.height-5),source=card_list[0]))
            open_card_list.append(card_list[0])
            return self.deck()
    
    def buttonclicked21(self):
        self.ids.btn21.background_color=(0,0,0,0)
        swich.append(1)
        if len(open_card_list)==2:
            open_card_list.remove(open_card_list[0])
            open_card_list.remove(open_card_list[0])
            
        if len(open_card_list)==4:
            open_card_list.remove(open_card_list[2])
            open_card_list.remove(open_card_list[2])
            
        if len(open_card_list)==6:
            open_card_list.remove(open_card_list[4])
            open_card_list.remove(open_card_list[4])
            
        if len(open_card_list)==8:
            open_card_list.remove(open_card_list[6])
            open_card_list.remove(open_card_list[6])
            
        if len(open_card_list)==10:
            open_card_list.remove(open_card_list[8])
            open_card_list.remove(open_card_list[8])
            
        if len(open_card_list)==12:
            open_card_list.remove(open_card_list[10])
            open_card_list.remove(open_card_list[10])
            
        if len(open_card_list)==14:
            open_card_list.remove(open_card_list[12])
            open_card_list.remove(open_card_list[12])
            
        if len(open_card_list)==16:
            open_card_list.remove(open_card_list[14])
            open_card_list.remove(open_card_list[14])
            
        if len(open_card_list)==18:
            open_card_list.remove(open_card_list[16])
            open_card_list.remove(open_card_list[16])
            
        if len(open_card_list)==20:
            open_card_list.remove(open_card_list[18])
            open_card_list.remove(open_card_list[18])

        if  card_list[0] not in open_card_list:
            
            self.ids.btn1.canvas.clear()
            self.ids.btn1.canvas.add(Rectangle(pos=(self.ids.btn1.x+3,self.ids.btn1.y+3),size=(self.ids.btn1.width-5,self.ids.btn1.height-5),source="trump.png"))

        if  card_list[1] not in open_card_list:
            self.ids.btn2.canvas.add(Rectangle(pos=(self.ids.btn2.x+3,self.ids.btn2.y+3),size=(self.ids.btn2.width-5,self.ids.btn2.height-5),source="trump.png"))

        if card_list[2] not in open_card_list:
            self.ids.btn3.canvas.add(Rectangle(pos=(self.ids.btn3.x+3,self.ids.btn3.y+3),size=(self.ids.btn3.width-5,self.ids.btn3.height-5),source="trump.png"))

        if card_list[3] not in open_card_list:
            self.ids.btn4.canvas.add(Rectangle(pos=(self.ids.btn4.x+3,self.ids.btn4.y+3),size=(self.ids.btn4.width-5,self.ids.btn4.height-5),source="trump.png"))

        if card_list[4] not in open_card_list:
            self.ids.btn5.canvas.add(Rectangle(pos=(self.ids.btn5.x+3,self.ids.btn5.y+3),size=(self.ids.btn5.width-5,self.ids.btn5.height-5),source="trump.png"))

        if card_list[5] not in open_card_list:
            self.ids.btn6.canvas.add(Rectangle(pos=(self.ids.btn6.x+3,self.ids.btn6.y+3),size=(self.ids.btn6.width-5,self.ids.btn6.height-5),source="trump.png"))

        if card_list[6] not in open_card_list:
            self.ids.btn7.canvas.add(Rectangle(pos=(self.ids.btn7.x+3,self.ids.btn7.y+3),size=(self.ids.btn7.width-5,self.ids.btn7.height-5),source="trump.png"))

        if card_list[7] not in open_card_list:
            self.ids.btn8.canvas.add(Rectangle(pos=(self.ids.btn8.x+3,self.ids.btn8.y+3),size=(self.ids.btn8.width-5,self.ids.btn8.height-5),source="trump.png"))

        if card_list[8] not in open_card_list:
            self.ids.btn9.canvas.add(Rectangle(pos=(self.ids.btn9.x+3,self.ids.btn9.y+3),size=(self.ids.btn9.width-5,self.ids.btn9.height-5),source="trump.png"))

        if card_list[9] not in open_card_list:
            self.ids.btn10.canvas.add(Rectangle(pos=(self.ids.btn10.x+3,self.ids.btn10.y+3),size=(self.ids.btn10.width-5,self.ids.btn10.height-5),source="trump.png"))

        if card_list[10] not in open_card_list:
            self.ids.btn11.canvas.add(Rectangle(pos=(self.ids.btn11.x+3,self.ids.btn11.y+3),size=(self.ids.btn11.width-5,self.ids.btn11.height-5),source="trump.png"))

        if card_list[11] not in open_card_list:
            self.ids.btn12.canvas.add(Rectangle(pos=(self.ids.btn12.x+3,self.ids.btn12.y+3),size=(self.ids.btn12.width-5,self.ids.btn12.height-5),source="trump.png"))

        if card_list[12] not in open_card_list:
            self.ids.btn13.canvas.add(Rectangle(pos=(self.ids.btn13.x+3,self.ids.btn13.y+3),size=(self.ids.btn13.width-5,self.ids.btn13.height-5),source="trump.png"))
            
        if card_list[13] not in open_card_list:
            self.ids.btn14.canvas.add(Rectangle(pos=(self.ids.btn14.x+3,self.ids.btn14.y+3),size=(self.ids.btn14.width-5,self.ids.btn14.height-5),source="trump.png"))

        if card_list[14] not in open_card_list:
            self.ids.btn15.canvas.add(Rectangle(pos=(self.ids.btn15.x+3,self.ids.btn15.y+3),size=(self.ids.btn15.width-5,self.ids.btn15.height-5),source="trump.png"))

        if card_list[15] not in open_card_list:
            self.ids.btn16.canvas.add(Rectangle(pos=(self.ids.btn16.x+3,self.ids.btn16.y+3),size=(self.ids.btn16.width-5,self.ids.btn16.height-5),source="trump.png"))

        if card_list[16] not in open_card_list:
            self.ids.btn17.canvas.add(Rectangle(pos=(self.ids.btn17.x+3,self.ids.btn17.y+3),size=(self.ids.btn17.width-5,self.ids.btn17.height-5),source="trump.png"))

        if card_list[17] not in open_card_list:
            self.ids.btn18.canvas.add(Rectangle(pos=(self.ids.btn18.x+3,self.ids.btn18.y+3),size=(self.ids.btn18.width-5,self.ids.btn18.height-5),source="trump.png"))

        if card_list[18] not in open_card_list:
            self.ids.btn19.canvas.add(Rectangle(pos=(self.ids.btn19.x+3,self.ids.btn19.y+3),size=(self.ids.btn19.width-5,self.ids.btn19.height-5),source="trump.png"))

        if card_list[19] not in open_card_list:
            self.ids.btn20.canvas.add(Rectangle(pos=(self.ids.btn20.x+3,self.ids.btn20.y+3),size=(self.ids.btn20.width-5,self.ids.btn20.height-5),source="trump.png"))

        
    
    def buttonclicked2(self):
        if len(swich)>=1:
            self.ids.btn2.canvas.clear()
            self.ids.btn2.canvas.add(Rectangle(pos=(self.ids.btn2.x+3,self.ids.btn2.y+3),size=(self.ids.btn2.width-5,self.ids.btn2.height-5),source=card_list[1]))
            open_card_list.append(card_list[1])
        
            return self.deck()
    def buttonclicked3(self):
        if len(swich)>=1:
            self.ids.btn3.canvas.clear()
            self.ids.btn3.canvas.add(Rectangle(pos=(self.ids.btn3.x+3,self.ids.btn3.y+3),size=(self.ids.btn3.width-5,self.ids.btn3.height-5),source=card_list[2]))
            open_card_list.append(card_list[2])
            return self.deck()
    
    def buttonclicked4(self):
        if len(swich)>=1:
            self.ids.btn4.canvas.clear()
            self.ids.btn4.canvas.add(Rectangle(pos=(self.ids.btn4.x+3,self.ids.btn4.y+3),size=(self.ids.btn4.width-5,self.ids.btn4.height-5),source=card_list[3]))
            open_card_list.append(card_list[3])
            return self.deck()
    
    def buttonclicked5(self):
        if len(swich)>=1:
            self.ids.btn5.canvas.clear()
            self.ids.btn5.canvas.add(Rectangle(pos=(self.ids.btn5.x+3,self.ids.btn5.y+3),size=(self.ids.btn5.width-5,self.ids.btn5.height-5),source=card_list[4]))
            open_card_list.append(card_list[4])
            return self.deck()
    
    def buttonclicked6(self):
        if len(swich)>=1:
            self.ids.btn6.canvas.clear()
            self.ids.btn6.canvas.add(Rectangle(pos=(self.ids.btn6.x+3,self.ids.btn6.y+3),size=(self.ids.btn6.width-5,self.ids.btn6.height-5),source=card_list[5]))
            open_card_list.append(card_list[5])
            return self.deck()
    
    def buttonclicked7(self):
        if len(swich)>=1:
            self.ids.btn7.canvas.clear()
            self.ids.btn7.canvas.add(Rectangle(pos=(self.ids.btn7.x+3,self.ids.btn7.y+3),size=(self.ids.btn7.width-5,self.ids.btn7.height-5),source=card_list[6]))
            open_card_list.append(card_list[6])
            return self.deck()
    
    def buttonclicked8(self):
        if len(swich)>=1:
            self.ids.btn8.canvas.clear()
            self.ids.btn8.canvas.add(Rectangle(pos=(self.ids.btn8.x+3,self.ids.btn8.y+3),size=(self.ids.btn8.width-5,self.ids.btn8.height-5),source=card_list[7]))
            open_card_list.append(card_list[7])
            return self.deck()
    
    def buttonclicked9(self):
        if len(swich)>=1:
            self.ids.btn9.canvas.clear()
            self.ids.btn9.canvas.add(Rectangle(pos=(self.ids.btn9.x+3,self.ids.btn9.y+3),size=(self.ids.btn9.width-5,self.ids.btn9.height-5),source=card_list[8]))
            open_card_list.append(card_list[8])
            return self.deck()
    
    def buttonclicked10(self):
        if len(swich)>=1:
            self.ids.btn10.canvas.clear()
            self.ids.btn10.canvas.add(Rectangle(pos=(self.ids.btn10.x+3,self.ids.btn10.y+3),size=(self.ids.btn10.width-5,self.ids.btn10.height-5),source=card_list[9]))
            open_card_list.append(card_list[9])
            return self.deck()
    
    def buttonclicked11(self):
        if len(swich)>=1:
            self.ids.btn11.canvas.clear()
            self.ids.btn11.canvas.add(Rectangle(pos=(self.ids.btn11.x+3,self.ids.btn11.y+3),size=(self.ids.btn11.width-5,self.ids.btn11.height-5),source=card_list[10]))
            open_card_list.append(card_list[10])
            return self.deck()
    
    def buttonclicked12(self):
        if len(swich)>=1:
            self.ids.btn12.canvas.clear()
            self.ids.btn12.canvas.add(Rectangle(pos=(self.ids.btn12.x+3,self.ids.btn12.y+3),size=(self.ids.btn12.width-5,self.ids.btn12.height-5),source=card_list[11]))
            open_card_list.append(card_list[11])
            return self.deck()
    
    def buttonclicked13(self):
        if len(swich)>=1:
            self.ids.btn13.canvas.clear()
            self.ids.btn13.canvas.add(Rectangle(pos=(self.ids.btn13.x+3,self.ids.btn13.y+3),size=(self.ids.btn13.width-5,self.ids.btn13.height-5),source=card_list[12]))
            open_card_list.append(card_list[12])
            return self.deck()
    
    def buttonclicked14(self):
        if len(swich)>=1:
            self.ids.btn14.canvas.clear()
            self.ids.btn14.canvas.add(Rectangle(pos=(self.ids.btn14.x+3,self.ids.btn14.y+3),size=(self.ids.btn14.width-5,self.ids.btn14.height-5),source=card_list[13]))
            open_card_list.append(card_list[13])
            return self.deck()
    
    def buttonclicked15(self):
        if len(swich)>=1:
            self.ids.btn15.canvas.clear()
            self.ids.btn15.canvas.add(Rectangle(pos=(self.ids.btn15.x+3,self.ids.btn15.y+3),size=(self.ids.btn15.width-5,self.ids.btn15.height-5),source=card_list[14]))
            open_card_list.append(card_list[14])
            return self.deck()
    
    def buttonclicked16(self):
        if len(swich)>=1:
            self.ids.btn16.canvas.clear()
            self.ids.btn16.canvas.add(Rectangle(pos=(self.ids.btn16.x+3,self.ids.btn16.y+3),size=(self.ids.btn16.width-5,self.ids.btn16.height-5),source=card_list[15]))
            open_card_list.append(card_list[15])
            return self.deck()
    
    def buttonclicked17(self):
        if len(swich)>=1:
            self.ids.btn17.canvas.clear()
            self.ids.btn17.canvas.add(Rectangle(pos=(self.ids.btn17.x+3,self.ids.btn17.y+3),size=(self.ids.btn17.width-5,self.ids.btn17.height-5),source=card_list[16]))
            open_card_list.append(card_list[16])
            return self.deck()
    
    def buttonclicked18(self):
        if len(swich)>=1:
            self.ids.btn18.canvas.clear()
            self.ids.btn18.canvas.add(Rectangle(pos=(self.ids.btn18.x+3,self.ids.btn18.y+3),size=(self.ids.btn18.width-5,self.ids.btn18.height-5),source=card_list[17]))
            open_card_list.append(card_list[17])
            return self.deck()
    
    def buttonclicked19(self):
        if len(swich)>=1:

            self.ids.btn19.canvas.clear()
            self.ids.btn19.canvas.add(Rectangle(pos=(self.ids.btn19.x+3,self.ids.btn19.y+3),size=(self.ids.btn19.width-5,self.ids.btn19.height-5),source=card_list[18]))
            open_card_list.append(card_list[18])
            return self.deck()
    
    def buttonclicked20(self):
        if len(swich)>=1:
          
            self.ids.btn20.canvas.clear()
            self.ids.btn20.canvas.add(Rectangle(pos=(self.ids.btn20.x+3,self.ids.btn20.y+3),size=(self.ids.btn20.width-5,self.ids.btn20.height-5),source=card_list[19]))
            open_card_list.append(card_list[19])
            return self.deck()


    def btn21_change(self):
        self.ids.btn21.background_color=(3,0,0,1)
        swich.remove(1)

    def deck(self):
        if len(open_card_list)==2:
            return self.deck1()
        if len(open_card_list)==4:
            return self.deck2()
        if len(open_card_list)==6:
            return self.deck3()
        if len(open_card_list)==8:
            return self.deck4()
        if len(open_card_list)==10:
            return self.deck5()
        if len(open_card_list)==12:
            return self.deck6()
        if len(open_card_list)==14:
            return self.deck7()
        if len(open_card_list)==16:
            return self.deck8()
        if len(open_card_list)==18:
            return self.deck9()
        if len(open_card_list)==20:
            return self.deck10()
    
    def deck1(self):
        if open_card_list[0]==open_card_list[1]:
                print(open_card_list)
                
        elif open_card_list[0] is not open_card_list[1]:
                print(open_card_list)
                self.btn21_change()
                
    def deck2(self):
        if open_card_list[2]==open_card_list[3]:
                print(open_card_list)
                
        elif open_card_list[2] is not open_card_list[3]:
                print(open_card_list)
                self.btn21_change()

    def deck3(self):
        if open_card_list[4]==open_card_list[5]:
                print(open_card_list)
                
        elif open_card_list[4] is not open_card_list[5]:
                print(open_card_list)
                self.btn21_change()

    def deck4(self):
        if open_card_list[6]==open_card_list[7]:
                print(open_card_list)
                
        elif open_card_list[6] is not open_card_list[7]:
                print(open_card_list)
                self.btn21_change()

    def deck5(self):
        if open_card_list[8]==open_card_list[9]:
                print(open_card_list)
                
        elif open_card_list[8] is not open_card_list[9]:
                print(open_card_list)
                self.btn21_change()
    def deck6(self):
        if open_card_list[10]==open_card_list[11]:
                print(open_card_list)
                
        elif open_card_list[10] is not open_card_list[11]:
                print(open_card_list)
                self.btn21_change()
    def deck7(self):
        if open_card_list[12]==open_card_list[13]:
                print(open_card_list)
                
        elif open_card_list[12] is not open_card_list[13]:
                print(open_card_list)
                self.btn21_change()

    def deck8(self):
        if open_card_list[14]==open_card_list[15]:
                print(open_card_list)
                
        elif open_card_list[14] is not open_card_list[15]:
                print(open_card_list)
                self.btn21_change()

    def deck9(self):
        if open_card_list[16]==open_card_list[17]:
                print(open_card_list)
                
        elif open_card_list[16] is not open_card_list[17]:
                print(open_card_list)
                self.btn21_change()

    def deck10(self):
        if open_card_list[18]==open_card_list[19]:
                print(open_card_list)
                
        elif open_card_list[18] is not open_card_list[19]:
                print(open_card_list)
                self.btn21_change() 

        
sm=ScreenManager()
sm.add_widget(Title(name="title"))
sm.add_widget(Title2(name="title2"))    
    



class StudyApp(App):
    def build(self):
        return sm

StudyApp().run()


