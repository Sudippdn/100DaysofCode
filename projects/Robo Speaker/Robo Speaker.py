from gtts import gTTS
import os    
def continue_program():
    # your command
    Command = input("What is your input command? ")
    tts = gTTS(text=f'{Command}', lang='en')
    tts.save("This_is_made_by_Sudip_Pradhan.mp3")
    # to start the file from python
    os.system("start This_is_made_by_Sudip_Pradhan.mp3")
    answer = False
    
if __name__ == "__main__":
    continue_program()
    
