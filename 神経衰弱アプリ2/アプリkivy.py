<Title>:
    canvas:
        
        Rectangle:
            size:self.size
            pos:self.pos
            source:"jungle-1807476-2.jpg"
    
    BoxLayout:
        orientation:"vertical"
        size:root.size
        
        Label:
            text:"Animal Trump"
            font_size:30
            size_hint_y:60

        Button:
            id:start_btn
            text:"start"
            font_size:50
            size_hint_y:10
            color:(0,0,0)
            on_press:root.title_clicked()
            

<Title2>:
    canvas:
        
        Rectangle:
            size:self.size
            pos:self.pos
            source:"jungle-1807476-2.jpg"
            
    BoxLayout:
    
        orientation:"vertical"
        
        Label:
            size_hint_y:10
            text:"Let's get the same animals"
            color:3,3,3,3
            font_size:30

        GridLayout:
            cols:4
            size_hint_y:90
            
            
            Button:
                id:btn1
                on_press:root.buttonclicked1()
                background_color: 0, 0, 0, 0 
                size_hint_y:None                    
                height:100
                
                canvas:
           
                    Rectangle:
                        #id:btn1
                        pos:(self.x+3,self.y+3)
                        size: self.width-5,self.height-5
                        source:"trump.png"
                        
                    
                        

                    

                        
            Button:
                id:btn2
                on_press:root.buttonclicked2()
                background_color: 0, 0, 0, 0 
                size_hint_y:None                    
                height:100
                canvas:
           
                    Rectangle:
                        
                        pos:(self.x+3,self.y+3)
                        size: self.width-5,self.height-5
                        source:"trump.png"


                        
            Button:
                id:btn3
                on_press:root.buttonclicked3()
                background_color: 0, 0, 0, 0 
                size_hint_y:None                    
                height:100
                canvas:
           
                    Rectangle:
                        pos:(self.x+3,self.y+3)
                        size: self.width-5,self.height-5
                        source:"trump.png"
            Button:
                id:btn4
                on_press:root.buttonclicked4()
                background_color: 0, 0, 0, 0 
                size_hint_y:None                    
                height:100
                canvas:
           
                    Rectangle:
                        pos:(self.x+3,self.y+3)
                        size: self.width-5,self.height-5
                        source:"trump.png"
            Button:
                id:btn5
                on_press:root.buttonclicked5()
                background_color: 0, 0, 0, 0 
                size_hint_y:None                    
                height:100
                canvas:
           
                    Rectangle:
                        pos:(self.x+3,self.y+3)
                        size: self.width-5,self.height-5
                        source:"trump.png"

            Button:
                id:btn6
                on_press:root.buttonclicked6()
                background_color: 0, 0, 0, 0 
                size_hint_y:None                    
                height:100
                canvas:
           
                    Rectangle:
                        pos:(self.x+3,self.y+3)
                        size: self.width-5,self.height-5
                        source:"trump.png"

            Button:
                id:btn7
                on_press:root.buttonclicked7()
                background_color: 0, 0, 0, 0 
                size_hint_y:None                    
                height:100
                canvas:
           
                    Rectangle:
                        pos:(self.x+3,self.y+3)
                        size: self.width-5,self.height-5
                        source:"trump.png"

            Button:
                id:btn8
                on_press:root.buttonclicked8()
                background_color: 0, 0, 0, 0 
                size_hint_y:None                    
                height:100
                canvas:
           
                    Rectangle:
                        pos:(self.x+3,self.y+3)
                        size: self.width-5,self.height-5
                        source:"trump.png"


            Button:
                id:btn9
                on_press:root.buttonclicked9()
                background_color: 0, 0, 0, 0 
                size_hint_y:None                    
                height:100
                canvas:
           
                    Rectangle:
                        pos:(self.x+3,self.y+3)
                        size: self.width-5,self.height-5
                        source:"trump.png"

            Button:
                id:btn10
                on_press:root.buttonclicked10()
                background_color: 0, 0, 0, 0 
                size_hint_y:None                    
                height:100
                canvas:
           
                    Rectangle:
                        pos:(self.x+3,self.y+3)
                        size: self.width-5,self.height-5
                        source:"trump.png"

            Button:
                id:btn11
                on_press:root.buttonclicked11()
                background_color: 0, 0, 0, 0 
                size_hint_y:None                    
                height:100
                canvas:
           
                    Rectangle:
                        pos:(self.x+3,self.y+3)
                        size: self.width-5,self.height-5
                        source:"trump.png"

            Button:
                id:btn12
                on_press:root.buttonclicked12()
                background_color: 0, 0, 0, 0 
                size_hint_y:None                    
                height:100
                canvas:
           
                    Rectangle:
                        pos:(self.x+3,self.y+3)
                        size: self.width-5,self.height-5
                        source:"trump.png"

            Button:
                id:btn13
                on_press:root.buttonclicked13()
                background_color: 0, 0, 0, 0 
                size_hint_y:None                    
                height:100
                canvas:
           
                    Rectangle:
                        pos:(self.x+3,self.y+3)
                        size: self.width-5,self.height-5
                        source:"trump.png"

            Button:
                id:btn14
                on_press:root.buttonclicked14()
                background_color: 0, 0, 0, 0 
                size_hint_y:None                    
                height:100
                canvas:
           
                    Rectangle:
                        pos:(self.x+3,self.y+3)
                        size: self.width-5,self.height-5
                        source:"trump.png"


            Button:
                id:btn15
                on_press:root.buttonclicked15()
                background_color: 0, 0, 0, 0 
                size_hint_y:None                    
                height:100
                canvas:
           
                    Rectangle:
                        pos:(self.x+3,self.y+3)
                        size: self.width-5,self.height-5
                        source:"trump.png"

            Button:
                id:btn16
                on_press:root.buttonclicked16()
                background_color: 0, 0, 0, 0 
                size_hint_y:None                    
                height:100
                canvas:
           
                    Rectangle:
                        pos:(self.x+3,self.y+3)
                        size: self.width-5,self.height-5
                        source:"trump.png"

            Button:
                id:btn17
                on_press:root.buttonclicked17()
                background_color: 0, 0, 0, 0 
                size_hint_y:None                    
                height:100
                canvas:
           
                    Rectangle:
                        pos:(self.x+3,self.y+3)
                        size: self.width-5,self.height-5
                        source:"trump.png"

            Button:
                id:btn18
                on_press:root.buttonclicked18()
                background_color: 0, 0, 0, 0 
                size_hint_y:None                    
                height:100
                canvas:
           
                    Rectangle:
                        pos:(self.x+3,self.y+3)
                        size: self.width-5,self.height-5
                        source:"trump.png"

            Button:
                id:btn19
                on_press:root.buttonclicked19()
                background_color: 0, 0, 0, 0 
                size_hint_y:None                    
                height:100
                canvas:
           
                    Rectangle:
                        pos:(self.x+3,self.y+3)
                        size: self.width-5,self.height-5
                        source:"trump.png"

            Button:
                id:btn20
                on_press:root.buttonclicked20()
                background_color: 0, 0, 0, 0 
                size_hint_y:None                    
                height:100
                canvas:
           
                    Rectangle:
                        pos:(self.x+3,self.y+3)
                        size: self.width-5,self.height-5
                        source:"trump.png"

            Button:
                id:btn21
                text:"Reset"
                font_size:30
                on_press:root.buttonclicked21()
                background_color: 0, 0, 0, 0

             
