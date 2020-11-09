#Very simple program testing GUI automation
import pyautogui, time

pyautogui.moveTo(21, 330, duration=1.5) #Move to the right of the screen
pyautogui.moveRel(170, 0, duration=1.5)	#Move to tweet
pyautogui.click() #Click on tweet
time.sleep(2) #Wait while page is loading
pyautogui.scroll(-275) #Scroll down a little
time.sleep(2) #Wait more
x,y = pyautogui.locateCenterOnScreen('.\\twitter_like_bot_img\\tweet_bar.png', confidence=0.8) #Find tweet bar
pyautogui.moveTo(x, y, duration=1.5) #Move to tweet bar
pyautogui.moveRel(85, 0, duration=1.5) #Move to like button
pyautogui.click() #Finally, click on like button