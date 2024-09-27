from tkinter import *
from tkinter import messagebox
import random

timeleft = 60
correct_word = 0
wrong_word = 0
i = 0
used_words = []


# Function to set the time limit based on user selection and start the game
def set_time_limit_and_start(time):
    global timeleft
    timeleft = time
    reset_game()  # Ensure the game is reset before starting the new mode
    main_window.deiconify()  # Show the main game window
    time_countLabel.config(text=timeleft)
    popup.destroy()  # Close the popup window


def timer():
    global timeleft, i
    if timeleft > 0:
        timeleft -= 1
        time_countLabel.config(text=timeleft)
        time_countLabel.after(1000, timer)
    else:
        wordEntry.config(state=DISABLED)
        show_score()


def show_score():
    result = correct_word - wrong_word
    instructionLabel.config(text=f'Correct words: {correct_word}\nWrong Words: {wrong_word}\nFinal Score: {result}')

    if result < 15:
        emoji1Label.config(image=poorpic)
    elif result >= 15:
        emoji1Label.config(image=goodpic)

    # Delay the appearance of the 'back to main menu' messagebox until the score is fully displayed
    main_window.after(2000, ask_main_menu)


def ask_main_menu():
    res = messagebox.askyesno('Confirm', 'Do you want to go back to the main menu?')
    if res:
        back_to_main_menu()  # Go back to the main menu
    else:
        reset_game()  # Restart the game with the same mode


def back_to_main_menu():
    main_window.withdraw()  # Hide the main game window
    # Create popup window for game mode selection again
    global popup
    popup = Tk()
    popup.title("Hankai Typestar - Typing Competition 102")
    popup.geometry('500x300')
    popup.config(bg='lightblue')

    # Personalized Title
    Label(popup, text="Welcome to Nanjing Hankai Academy,\nBilingual School Department", font=('Helvetica', 16, 'bold'),
          bg='lightblue').pack(pady=10)
    Label(popup, text="Hankai Typestar - Typing Competition 102", font=('Helvetica', 14), bg='lightblue').pack(pady=5)
    Label(popup, text="Powered by The Brainiacs!", font=('Helvetica', 12, 'italic'), bg='lightblue').pack(pady=5)

    # Game mode buttons
    Button(popup, text="30 Seconds (Practice Mode)", font=('Helvetica', 14),
           command=lambda: set_time_limit_and_start(30)).pack(pady=10)
    Button(popup, text="60 Seconds (Competition Mode)", font=('Helvetica', 14),
           command=lambda: set_time_limit_and_start(60)).pack(pady=10)

    popup.mainloop()


def reset_game():
    global i, correct_word, wrong_word, used_words
    i = 0
    correct_word = 0
    wrong_word = 0
    used_words = []
    countLabel.config(text='0')  # Reset the word count
    time_countLabel.config(text=timeleft)  # Reset the timer display
    wordEntry.config(state=NORMAL)
    instructionLabel.config(text='Type Word And Hit Enter')  # Reset instructions
    emoji1Label.config(image='')  # Clear emoji
    random.shuffle(word_list)  # Shuffle words
    word_list_Label.config(text=word_list[0])  # Display the first word
    wordEntry.delete(0, END)  # Clear the word entry box


def play_game(event):
    if wordEntry.get() != '':
        global i, correct_word, wrong_word, used_words
        i += 1
        countLabel.config(text=i)

        if timeleft == 30 or timeleft == 60:  # Check if the timer is either 30s or 60s
            timer()

        current_word = word_list_Label['text']
        if wordEntry.get() == current_word:
            correct_word += 1
        else:
            wrong_word += 1

        used_words.append(current_word)

        # Ensure the next word is new
        available_words = [word for word in word_list if word not in used_words]
        if available_words:
            next_word = random.choice(available_words)
            word_list_Label.config(text=next_word)
        else:
            word_list_Label.config(text="No more words!")

        wordEntry.delete(0, END)


# Word list
word_list = ['abroad', 'casual', 'around', 'couple', 'beyond', 'budget', 'during', 'device', 'eager', 'final', 'going',
             'ideal', 'judge', 'metal', 'media', 'newly', 'known', 'local', 'might', 'noise', 'life', 'like', 'love',
             'more', 'nose', 'near', 'open', 'only', 'push', 'pull', 'sell', 'sale', 'bad', 'her', 'rag', 'box', 'jug',
             'sow', 'cut', 'lot', 'tap', 'dug', 'map', 'use', 'Nanjing', 'Hankai', 'Academy']

# Functionality part
sliderwords = ''
count = 0


def slider():
    global sliderwords, count
    text = 'HKA 2ND TYPING COMPETITION'
    if count >= len(text):
        count = 0
        sliderwords = ''
    sliderwords = sliderwords + text[count]
    movingLabel.config(text=sliderwords)
    count += 1
    movingLabel.after(250, slider)


# GUI part

# Create main game window first, but hide it
main_window = Tk()
main_window.title('HKA 2ND TYPING COMPETITION')
main_window.iconbitmap('hankailogo.ico')
main_window.geometry('1920x1080')
main_window.config(bg='burlywood3')

logoImage = PhotoImage(file='hkalogo4.png')
logoLabel = Label(main_window, image=logoImage, bg='burlywood3')
logoLabel.place(x=0, y=-27)

movingLabel = Label(main_window, text='', bg='burlywood3', font=('Helvetica', 58, 'bold italic'), fg=('blue4'))
movingLabel.place(x=270, y=50)
slider()

random.shuffle(word_list)
word_list_Label = Label(main_window, text=word_list[0], bg='burlywood3', font=('Helvetica', 45, ('italic bold')),
                        fg=('coral4'))
word_list_Label.place(x=790, y=350, anchor=CENTER)

wordLabel = Label(main_window, text='WORDS:', font=('Helvetica', 40, 'italic bold'), bg='burlywood3')
wordLabel.place(x=300, y=350, anchor=CENTER)

countLabel = Label(main_window, text='0', font=('Helvetica', 40, 'italic bold'), bg='burlywood3')
countLabel.place(x=300, y=420, anchor=CENTER)

timelabel = Label(main_window, text='TIME:', font=('Helvetica', 40, 'italic bold'), bg='burlywood3')
timelabel.place(x=1280, y=350, anchor=CENTER)

time_countLabel = Label(main_window, text='60', font=('Helvetica', 40, 'italic bold'), bg='burlywood3')
time_countLabel.place(x=1280, y=420, anchor=CENTER)

wordEntry = Entry(main_window, font=('arial', 25, 'italic bold'), bd=10, justify=CENTER)
wordEntry.place(x=790, y=500, anchor=CENTER)
wordEntry.focus_set()

instructionLabel = Label(main_window, text='Type the words and click enter!', font=('Helvetica', 35, 'italic bold'),
                         bg='burlywood3', fg=('coral4'))
instructionLabel.place(x=790, y=700, anchor=CENTER)

poorpic = PhotoImage(file='mickey1.png')
goodpic = PhotoImage(file='tyson1.png')

emoji1Label = Label(main_window, bg='burlywood3')
emoji1Label.place(x=1250, y=740)

main_window.bind('<Return>', play_game)
main_window.withdraw()  # Hide the main game window until the popup selection is made

# Create popup window for game mode selection (Main Menu)
popup = Tk()
popup.title("Hankai Typestar - Typing Competition 102")
popup.geometry('500x300')
popup.config(bg='lightblue')

# Personalized Title
Label(popup, text="Welcome to Nanjing Hankai Academy,\nBilingual School Department", font=('Helvetica', 16, 'bold'),
      bg='lightblue').pack(pady=10)
Label(popup, text="Hankai Typestar - Typing Competition 102", font=('Helvetica', 14), bg='lightblue').pack(pady=5)
Label(popup, text="Powered by The Brainiacs!", font=('Helvetica', 12, 'italic'), bg='lightblue').pack(pady=5)

# Game mode buttons
Button(popup, text="30 Seconds (Practice Mode)", font=('Helvetica', 14),
       command=lambda: set_time_limit_and_start(30)).pack(pady=10)
Button(popup, text="60 Seconds (Competition Mode)", font=('Helvetica', 14),
       command=lambda: set_time_limit_and_start(60)).pack(pady=10)

popup.mainloop()
