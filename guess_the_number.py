from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import random

class GuessTheNumberApp(App):
    def build(self):
        self.random_number = random.randint(1,1000)
        self.attempts = 0
        layout = BoxLayout(orientation ='vertical')
        
        self.label = Label(text ="Guess a number between 1 and 1000!")
        layout.add_widget(self.label)
        
        self.guess_input = TextInput(hint_text="Enter your guess.",multiline=False)
        layout.add_widget(self.guess_input)
        
        guess_button = Button(text="Sumbit Guess",on_press=self.check_guess)
        layout.add_widget(guess_button)
        
        return layout
    def check_guess(self,instance):
        try:
            guess = int(self.guess_input.text)
            
            self.attempts+=1
            
            if guess<self.random_number:
                self.label.text="too low!"
            elif guess>self.random_number:
                self.label.text="Too High!"
            else:
                self.label.text = f"Congratulations! you guessed it in {self.attempts} attempts."
        except ValueError:
            self.label.text= "Please entre a valid number."
            
if __name__ =="__main__":
    GuessTheNumberApp().run()
                
            
                