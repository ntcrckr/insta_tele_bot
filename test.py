from pyvirtualdisplay import Display
from selenium import webdriver

display = Display(visible=False, size=(800, 600))
display.start()

# now Firefox will run in a virtual display.
# you will not see the browser.
browser = webdriver.Chrome(executable_path="./chromedriver.exe")
browser.get('http://www.google.com')
print(browser.title)
browser.quit()

display.stop()