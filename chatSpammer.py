import time, pyautogui
while(True):
    print("Chose spam via custom message - 1 || spam via paste(ctrl + v) - 2")
    choice = int(input())
    if(choice == 1):
        print("How many times do u want to send the message\n enter 0 to exit\n if u want to change your choice input 1")
        repetitions = int(input())
        if (repetitions == 0): exit(0)
        elif (repetitions == 1): continue
        print("what do you want to spam")
        message = input()
        delay = int(input("How many ms  do u want to wait between messages"))
        time.sleep(5)
        for i in range(repetitions):
            pyautogui.typewrite(message)
            pyautogui.press("enter")
            time.sleep(delay/1000)

    elif (choice == 2):
        print( "How many times do u want to send the message\n enter 0 to exit\n if u want to change your choice input 1")
        repetitions = int(input())
        delay = int(input("How many ms  do u want to wait between messages"))
        if (repetitions == 0): exit(0)
        elif (repetitions == 1): continue
        time.sleep(5)
        for i in range(repetitions):
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press("enter")
            time.sleep(delay / 1000)

    elif (choice == 3):
        print( "How many times do u want to send the message\n enter 0 to exit\n if u want to change your choice input 1")
        repetitions = int(input())
        delay = int(input("How many ms  do u want to wait between messages"))
        if (repetitions == 0): exit(0)
        elif (repetitions == 1): continue
        time.sleep(5)
        for i in range(repetitions):
            pyautogui.press('/')
            pyautogui.press("enter")
            time.sleep(delay / 1000)

