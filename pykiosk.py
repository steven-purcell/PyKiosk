import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument("--test-type")
# options.binary_location = "/Users/stevenpurcell/Downloads/chromedriver"
# driver = webdriver.Chrome(chrome_options=options)

urls = ['https://status.g2lytics.com',
'https://www.msn.com/en-us/weather/fullscreenmaps',
'https://weather.com/weather/5day/l/d31b209091908e29d78cfb58bcb998952d09db7e10e650e3f7b2d93516bcab18']

timer = 20

driver = webdriver.Chrome("/Users/stevenpurcell/Downloads/chromedriver")

def callNewPage(index):
    driver.get(urls[index])
    time.sleep(timer)
    if index < len(urls)-1:
        callNewPage(index+1)
    if index >= len(urls)-1:
        driver.delete_all_cookies()
        send_command = ('POST', '/session/$sessionId/chromium/send_command')
        driver.command_executor._commands['SEND_COMMAND'] = send_command
        driver.execute('SEND_COMMAND', dict(cmd='Network.clearBrowserCache', params={}))
        callNewPage(0)

callNewPage(0)