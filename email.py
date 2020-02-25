import webbrowser
import pyautogui
import time


# open web browser and wait for webpage to load
webbrowser.open('https://gmail.com/')
time.sleep(5)

# drag mouse to and click on compose email button
pyautogui.moveTo(160, 190, 2)
pyautogui.click()
time.sleep(5)

# new tab
webbrowser.open_new_tab('https://docs.google.com/document/d/1_eKCtu-WelHdYRWOAFLXAdFa53DqXJaaC1LfvK0Ib64/edit')
time.sleep(5)

# copy, tab
pyautogui.hotkey('command', 'a')
pyautogui.hotkey('command', 'c')
pyautogui.moveTo(190, 98, 1)
pyautogui.click()
time.sleep(2)

# write, paste
pyautogui.write('jen@coefficientlabs.com')
pyautogui.press('enter')
pyautogui.write('austin@coefficientlabs.com')
pyautogui.press('enter')
pyautogui.moveTo(710, 1020, 2)
time.sleep(5)
pyautogui.click()
pyautogui.write('Hope you are having a great Monday!')
pyautogui.moveTo(720, 1095, 2)
pyautogui.click()
time.sleep(2)
pyautogui.hotkey('command', 'v')

# send
pyautogui.moveTo(630, 1408, 2)
# pyautogui.click()