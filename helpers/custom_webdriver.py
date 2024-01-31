from time import sleep
from platform import system
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class ChromeWebDriver(Chrome):
    def __init__(self, headless):
        if headless:
            self.opts = Options()
            self.opts.add_argument('--headless')
            self.opts.add_argument('window-size=1920,1080')
            self.opts.add_argument('log-level=2')
            #self.opts.add_argument('--no-sandbox')
            #self.opts.add_argument('--disable-dev-shm-usage')
        else:
            self.opts = Options()
            if system() == 'Darwin': self.opts.add_argument("user-data-dir=./selenium_logs")
            if system() == 'Windows': self.opts.add_argument("user-data-dir=.\\selenium_logs")
            self.opts.add_argument('log-level=3')
        
        super().__init__(options=self.opts)

    def wait_for_name(self, elementName, timeout=15, pollFrequency=1):
        WebDriverWait(self, timeout, poll_frequency=pollFrequency).until(EC.visibility_of_any_elements_located((By.NAME,elementName)))

    def wait_for_id(self, elementID, timeout=15, pollFrequency=1):
        WebDriverWait(self, timeout, poll_frequency=pollFrequency).until(EC.visibility_of_any_elements_located((By.ID,elementID)))

    def wait_for_class(self, elementClass, timeout=15, pollFrequency=1):
        WebDriverWait(self, timeout, poll_frequency=pollFrequency).until(EC.element_to_be_clickable((By.CLASS_NAME,elementClass)))
    
    def wait_for_xpath_element(self, xpathValue, timeout=15, pollFrequency=1):
        WebDriverWait(self, timeout, poll_frequency=pollFrequency).until(EC.visibility_of_element_located((By.XPATH,xpathValue)))

    def wait_for_class_loading_done(self, elementClass ,timeout=15, pollFrequency=1):
        WebDriverWait(self, timeout, poll_frequency=pollFrequency).until(EC.invisibility_of_element((By.CLASS_NAME,elementClass)))

    def wait_for_xpath_element_gone(self, xpathValue, timeout=15, pollFrequency=1):
        WebDriverWait(self, timeout, poll_frequency=pollFrequency).until(EC.invisibility_of_element_located((By.XPATH,xpathValue)))

    def wait_time(self, seconds):
        sleep(seconds)

    def type_into(self, element, attributeName, attributeValue, inputValue, timeout=15, pollFrequency=1, waitBefore=0, waitAfter=0, inputClear=True, selectAllForDelete=False):
        if waitBefore > 0:
            self.wait_time(waitBefore)

        try:
            WebDriverWait(self, timeout, poll_frequency=pollFrequency).until(EC.element_to_be_clickable((By.XPATH,'//' + element + '[@' + attributeName + '="' + attributeValue + '"]')))
        except:
            WebDriverWait(self, timeout=1, poll_frequency=pollFrequency).until(EC.visibility_of_element_located((By.XPATH,'//' + element + '[@' + attributeName + '="' + attributeValue + '"]')))

        inputElement = self.find_element(By.XPATH, '//' + element + '[@' + attributeName + '="' + attributeValue + '"]')

        if (element == 'input' or element == 'textarea') and inputClear:
            inputElement.clear()
        
        if str(inputValue) == 'nan' or inputValue == '':
            if selectAllForDelete:
                inputElement.send_keys(Keys.CONTROL, 'A')
        
            inputElement.send_keys(Keys.DELETE)
        else:
            inputElement.send_keys(str(inputValue))
        
        if waitAfter > 0:
            self.wait_time(waitAfter)

    def type_into_contains(self, element, attributeName, attributeValueContains, inputValue, timeout=15, pollFrequency=1, waitBefore=0, waitAfter=0, inputClear=True, selectAllForDelete=False):
        if waitBefore > 0:
            self.wait_time(waitBefore)

        try:
            WebDriverWait(self, timeout, poll_frequency=pollFrequency).until(EC.element_to_be_clickable((By.XPATH,'//' + element + '[contains(@' + attributeName + ',"' + attributeValueContains + '")]')))
        except:
            WebDriverWait(self, timeout=1, poll_frequency=pollFrequency).until(EC.visibility_of_element_located((By.XPATH,'//' + element + '[contains(@' + attributeName + ',"' + attributeValueContains + '")]')))

        inputElement = self.find_element(By.XPATH, '//' + element + '[contains(@' + attributeName + ',"' + attributeValueContains + '")]')

        if (element == 'input' or element == 'textarea') and inputClear:
            inputElement.clear()
        
        if str(inputValue) == 'nan' or inputValue == '':
            if selectAllForDelete:
                inputElement.send_keys(Keys.CONTROL, 'A')
        
            inputElement.send_keys(Keys.DELETE)
        else:
            inputElement.send_keys(str(inputValue))
        
        if waitAfter > 0:
            self.wait_time(waitAfter)

    def type_into_xpath(self, xpathValue, inputValue, timeout=15, pollFrequency=1, waitBefore=0, waitAfter=0, inputClear=True, selectAllForDelete=False):
        if waitBefore > 0:
            self.wait_time(waitBefore)

        try:
            WebDriverWait(self, timeout, poll_frequency=pollFrequency).until(EC.element_to_be_clickable((By.XPATH, xpathValue)))
        except:
            WebDriverWait(self, timeout=1, poll_frequency=pollFrequency, ignored_exceptions=StaleElementReferenceException).until(EC.presence_of_element_located((By.XPATH, xpathValue)))

        inputElement = self.find_element(By.XPATH, xpathValue)

        if inputClear:       
            try:
                inputElement.clear()
            except:
                pass

        if str(inputValue) == 'nan' or inputValue == '':
            if selectAllForDelete:
                inputElement.send_keys(Keys.CONTROL, 'A')
        
            inputElement.send_keys(Keys.DELETE)
        else:
            inputElement.send_keys(str(inputValue))

        if waitAfter > 0:
            self.wait_time(waitAfter)

    def click_text_button(self, buttonText, timeout=15, pollFrequency=1, waitBefore=0, waitAfter=0, doubleClick=False):
        if waitBefore > 0:
            self.wait_time(waitBefore)

        try:
            WebDriverWait(self, timeout, poll_frequency=pollFrequency).until(EC.element_to_be_clickable((By.XPATH,'//*[text()="' + buttonText + '"]')))
        except:
            WebDriverWait(self, timeout=1, poll_frequency=pollFrequency, ignored_exceptions=StaleElementReferenceException).until(EC.presence_of_element_located((By.XPATH,'//*[text()="' + buttonText + '"]')))
        
        Button = self.find_element(By.XPATH, '//*[text()="' + buttonText + '"]')
        
        try:
            if doubleClick:
                Button.double_click()
            else:
                Button.click()
        except:
            if doubleClick:
                self.execute_script('arguments[0].dblclick()', Button)
            else:
                self.execute_script('arguments[0].click()', Button)
        
        if waitAfter > 0:
            self.wait_time(waitAfter)

    def click_element(self, element, attributeName, attributeValue, timeout=15, pollFrequency=1, waitBefore=0, waitAfter=0, doubleClick=False):
        if waitBefore > 0:
            self.wait_time(waitBefore)

        try:
            WebDriverWait(self, timeout, poll_frequency=pollFrequency).until(EC.element_to_be_clickable((By.XPATH,'//' + element + '[@' + attributeName + '="' + attributeValue + '"]')))
        except:
            WebDriverWait(self, timeout=1, poll_frequency=pollFrequency, ignored_exceptions=StaleElementReferenceException).until(EC.presence_of_element_located((By.XPATH,'//' + element + '[@' + attributeName + '="' + attributeValue + '"]')))

        elementToClick = self.find_element(By.XPATH, '//' + element + '[@' + attributeName + '="' + attributeValue + '"]')
        
        try:
            if doubleClick:
                elementToClick.double_click()
            else:
                elementToClick.click()
        except:
            if doubleClick:
                self.execute_script('arguments[0].dblclick()', elementToClick)
            else:
                self.execute_script('arguments[0].click()', elementToClick)

        if waitAfter > 0:
            self.wait_time(waitAfter)

    def click_element_xpath(self, xpathValue, timeout=15, pollFrequency=1, waitBefore=0, waitAfter=0, doubleClick=False):
        if waitBefore > 0:
            self.wait_time(waitBefore)

        try:
            WebDriverWait(self, timeout, poll_frequency=pollFrequency).until(EC.element_to_be_clickable((By.XPATH, xpathValue)))
        except:
            WebDriverWait(self, timeout, poll_frequency=pollFrequency).until(EC.presence_of_element_located((By.XPATH, xpathValue)))

        elementToClick = self.find_element(By.XPATH, xpathValue)
        
        try:
            if doubleClick:
                elementToClick.double_click()
            else:
                elementToClick.click()
        except:
            if doubleClick:
                self.execute_script('arguments[0].dblclick()', elementToClick)
            else:
                self.execute_script('arguments[0].click()', elementToClick)

        if waitAfter > 0:
            self.wait_time(waitAfter)
   
    def click_element_contains(self, element, attributeName, attributeValueContains, timeout=15, pollFrequency=1, waitBefore=0, waitAfter=0, doubleClick=False):
        if waitBefore > 0:
            self.wait_time(waitBefore)

        try:
            WebDriverWait(self, timeout, poll_frequency=pollFrequency).until(EC.element_to_be_clickable((By.XPATH,'//' + element + '[contains(@' + attributeName + ',"' + attributeValueContains + '")]')))
        except:
            WebDriverWait(self, timeout=1, poll_frequency=pollFrequency, ignored_exceptions=StaleElementReferenceException).until(EC.presence_of_element_located((By.XPATH,'//' + element + '[contains(@' + attributeName + ',"' + attributeValueContains + '")]')))

        elementToClick = self.find_element(By.XPATH, '//' + element + '[contains(@' + attributeName + ',"' + attributeValueContains + '")]')
        
        try:
            if doubleClick:
                elementToClick.double_click()
            else:
                elementToClick.click()
        except:
            if doubleClick:
                self.execute_script('arguments[0].dblclick()', elementToClick)
            else:
                self.execute_script('arguments[0].click()', elementToClick)

        if waitAfter > 0:
            self.wait_time(waitAfter)

    def click_text_link(self, linkText, timeout=15, pollFrequency=1, waitBefore=0, waitAfter=0, doubleClick=False):
        if waitBefore > 0:
            self.wait_time(waitBefore)

        try:
            WebDriverWait(self, timeout, poll_frequency=pollFrequency).until(EC.element_to_be_clickable((By.XPATH,'//a[@text()="' + linkText + '"]')))
        except:
            WebDriverWait(self, timeout=1, poll_frequency=pollFrequency, ignored_exceptions=StaleElementReferenceException).until(EC.presence_of_element_located((By.XPATH,'//a[@text()="' + linkText + '"]')))

        elementToClick = self.find_element(By.LINK_TEXT, linkText)
        
        try:
            if doubleClick:
                elementToClick.double_click()
            else:
                elementToClick.click()
        except:
            if doubleClick:
                self.execute_script('arguments[0].dblclick()', elementToClick)
            else:
                self.execute_script('arguments[0].click()', elementToClick)

        if waitAfter > 0:
            self.wait_time(waitAfter)

    def hover_over_xpath(self, xpathValue, timeout=15, pollFrequency=1, waitBefore=0, waitAfter=0):
        if waitBefore > 0:
            self.wait_time(waitBefore)

        try:
            WebDriverWait(self, timeout, poll_frequency=pollFrequency).until(EC.element_to_be_clickable((By.XPATH, xpathValue)))
        except:
            WebDriverWait(self, timeout=1, poll_frequency=pollFrequency, ignored_exceptions=StaleElementReferenceException).until(EC.presence_of_element_located((By.XPATH, xpathValue)))

        elementToHoverOver = self.find_element(By.XPATH, xpathValue)
        hover = ActionChains(self).move_to_element(elementToHoverOver)
        hover.perform()

        if waitAfter > 0:
            self.wait_time(waitAfter)

    def hover_over_element(self, element, attributeName, attributeValue, timeout=15, pollFrequency=1, waitBefore=0, waitAfter=0):
        if waitBefore > 0:
            self.wait_time(waitBefore)

        try:
            WebDriverWait(self, timeout, poll_frequency=pollFrequency).until(EC.element_to_be_clickable((By.XPATH,'//' + element + '[@' + attributeName + '="' + attributeValue + '"]')))
        except:
            WebDriverWait(self, timeout=1, poll_frequency=pollFrequency, ignored_exceptions=StaleElementReferenceException).until(EC.presence_of_element_located((By.XPATH,'//' + element + '[@' + attributeName + '="' + attributeValue + '"]')))

        elementToHoverOver = self.find_element(By.XPATH, '//' + element + '[@' + attributeName + '="' + attributeValue + '"]')
        hover = ActionChains(self).move_to_element(elementToHoverOver)
        hover.perform()

        if waitAfter > 0:
            self.wait_time(waitAfter)

    def grab_element_text(self, element, attributeName, attributeValue, timeout=15, pollFrequency=1, waitBefore=0, waitAfter=0):
        if waitBefore > 0:
            self.wait_time(waitBefore)

        try:
            WebDriverWait(self, timeout, poll_frequency=pollFrequency).until(EC.visibility_of_element_located((By.XPATH,'//' + element + '[@' + attributeName + '="' + attributeValue + '"]')))
        except:
            WebDriverWait(self, timeout=1, poll_frequency=pollFrequency, ignored_exceptions=StaleElementReferenceException).until(EC.presence_of_element_located((By.XPATH,'//' + element + '[@' + attributeName + '="' + attributeValue + '"]')))

        elementToGrabText = self.find_element(By.XPATH, '//' + element + '[@' + attributeName + '="' + attributeValue + '"]')

        if waitAfter > 0:
            self.wait_time(waitAfter)

        literalText = elementToGrabText.text
        propertyText = elementToGrabText.get_property('value')

        if propertyText != None and literalText == '':
            return propertyText
        else:
            return literalText

    def grab_elements_text_to_list(self, element, attributeName, attributeValue, timeout=15, pollFrequency=1, waitBefore=0, waitAfter=0):
        if waitBefore > 0:
            self.wait_time(waitBefore)

        try:
            WebDriverWait(self, timeout, poll_frequency=pollFrequency).until(EC.visibility_of_element_located((By.XPATH,'//' + element + '[@' + attributeName + '="' + attributeValue + '"]')))
        except:
            WebDriverWait(self, timeout=1, poll_frequency=pollFrequency, ignored_exceptions=StaleElementReferenceException).until(EC.presence_of_element_located((By.XPATH,'//' + element + '[@' + attributeName + '="' + attributeValue + '"]')))
      
        outputList = []
        elementsToGrabText = self.find_elements(By.XPATH, '//' + element + '[@' + attributeName + '="' + attributeValue + '"]')

        for item in elementsToGrabText:
            literalText = item.text
            propertyText = item.get_property('value')
            
            if literalText != '' or propertyText != None:
                if literalText == '' and propertyText != None:
                    outputList.append(propertyText)
                else:
                    outputList.append(literalText)

        if waitAfter > 0:
            self.wait_time(waitAfter)

        return outputList

    def grab_element_text_xpath(self, xpathValue, timeout=15, pollFrequency=1, waitBefore=0, waitAfter=0):
        if waitBefore > 0:
            self.wait_time(waitBefore)

        try:
            WebDriverWait(self, timeout, poll_frequency=pollFrequency).until(EC.visibility_of_element_located((By.XPATH,xpathValue)))
        except:
            WebDriverWait(self, timeout=1, poll_frequency=pollFrequency, ignored_exceptions=StaleElementReferenceException).until(EC.presence_of_element_located((By.XPATH,xpathValue)))

        elementToGrabText = self.find_element(By.XPATH, xpathValue)

        if waitAfter > 0:
            self.wait_time(waitAfter)

        literalText = elementToGrabText.text
        propertyText = elementToGrabText.get_property('value')

        if propertyText != None and literalText == '':
            return propertyText
        else:
            return literalText

    def find_and_click_element_text_in_list(self, element, attributeName, attributeValue, searchText, timeout=15, pollFrequency=1, waitBefore=0, waitAfter=0, doubleClick=False, printDictionary=False):
        if waitBefore > 0:
            self.wait_time(waitBefore)

        try:
            WebDriverWait(self, timeout, poll_frequency=pollFrequency).until(EC.visibility_of_element_located((By.XPATH,'//' + element + '[@' + attributeName + '="' + attributeValue + '"]')))
        except:
            WebDriverWait(self, timeout=1, poll_frequency=pollFrequency, ignored_exceptions=StaleElementReferenceException).until(EC.presence_of_element_located((By.XPATH,'//' + element + '[@' + attributeName + '="' + attributeValue + '"]')))
        
        outputDict = {}
        elementsToGrab = self.find_elements(By.XPATH, '//' + element + '[@' + attributeName + '="' + attributeValue + '"]')

        for item in elementsToGrab:
            if item.text != '':
                outputDict[item.text.lower()] = item
        
        if printDictionary:
            print(outputDict)

        elementToClick = outputDict[searchText.lower()]

        try:
            if doubleClick:
                elementToClick.double_click()
            else:
                elementToClick.click()
        except:
            self.execute_script('arguments[0].click()', elementToClick)

        if waitAfter > 0:
            self.wait_time(waitAfter)

    def find_and_click_element_text_contains_in_list(self, element, attributeName, attributeValueContains, searchText, timeout=15, pollFrequency=1, waitBefore=0, waitAfter=0, doubleClick=False, printDictionary=False):
        if waitBefore > 0:
            self.wait_time(waitBefore)

        try:
            WebDriverWait(self, timeout, poll_frequency=pollFrequency).until(EC.element_to_be_clickable((By.XPATH,'//' + element + '[contains(@' + attributeName + ',"' + attributeValueContains + '")]')))
        except:
            WebDriverWait(self, timeout=1, poll_frequency=pollFrequency, ignored_exceptions=StaleElementReferenceException).until(EC.presence_of_element_located((By.XPATH,'//' + element + '[contains(@' + attributeName + ',"' + attributeValueContains + '")]')))
        
        outputDict = {}
        elementsToGrab = self.find_elements(By.XPATH, '//' + element + '[contains(@' + attributeName + ',"' + attributeValueContains + '")]')

        for item in elementsToGrab:
            if item.text != '':
                outputDict[item.text.lower()] = item
        
        if printDictionary:
            print(outputDict)

        elementToClick = outputDict[searchText.lower()]
        
        try:
            if doubleClick:
                elementToClick.double_click()
            else:
                elementToClick.click()
        except:
            self.execute_script('arguments[0].click()', elementToClick)

        if waitAfter > 0:
            self.wait_time(waitAfter)

    def grab_element_position_in_list(self, element, attributeName, attributeValue, searchText, timeout=15, pollFrequency=1, waitBefore=0, waitAfter=0, printDictionary=False):
        if waitBefore > 0:
            self.wait_time(waitBefore)

        try:
            WebDriverWait(self, timeout, poll_frequency=pollFrequency).until(EC.visibility_of_element_located((By.XPATH,'//' + element + '[@' + attributeName + '="' + attributeValue + '"]')))
        except:
            WebDriverWait(self, timeout=1, poll_frequency=pollFrequency, ignored_exceptions=StaleElementReferenceException).until(EC.presence_of_element_located((By.XPATH,'//' + element + '[@' + attributeName + '="' + attributeValue + '"]')))
        
        outputDict = {}
        elementsToGrab = self.find_elements(By.XPATH, '//' + element + '[@' + attributeName + '="' + attributeValue + '"]')

        for item in elementsToGrab:
            if item.text != '':
                outputDict[item.text.lower()] = item
        
        if printDictionary:
            print(outputDict)
        
        position = list(outputDict.keys()).index(searchText.lower())

        if waitAfter > 0:
            self.wait_time(waitAfter)

        return position

    def select_in_dropdown(self, element, attributeName, attributeValue, optionToSelect, timeout=15, pollFrequency=1, waitBefore=0, waitAfter=0):
        if waitBefore > 0:
            self.wait_time(waitBefore)

        try:
            WebDriverWait(self, timeout, poll_frequency=pollFrequency).until(EC.visibility_of_element_located((By.XPATH,'//' + element + '[@' + attributeName + '="' + attributeValue + '"]')))
        except:
            WebDriverWait(self, timeout=1, poll_frequency=pollFrequency, ignored_exceptions=StaleElementReferenceException).until(EC.presence_of_element_located((By.XPATH,'//' + element + '[@' + attributeName + '="' + attributeValue + '"]')))
        
        dropDownList = Select(self.find_element(By.XPATH, '//' + element + '[@' + attributeName + '="' + attributeValue + '"]'))

        dropDownList.select_by_visible_text(optionToSelect)

        if waitAfter > 0:
            self.wait_time(waitAfter)

    def select_in_dropdown_xpath(self, xpathValue, optionToSelect, timeout=15, pollFrequency=1, waitBefore=0, waitAfter=0):
        if waitBefore > 0:
            self.wait_time(waitBefore)

        try:
            WebDriverWait(self, timeout, poll_frequency=pollFrequency).until(EC.visibility_of_element_located((By.XPATH,xpathValue)))
        except:
            WebDriverWait(self, timeout=1, poll_frequency=pollFrequency, ignored_exceptions=StaleElementReferenceException).until(EC.presence_of_element_located((By.XPATH,xpathValue)))
        
        dropDownList = Select(self.find_element(By.XPATH, xpathValue))
        dropDownList.select_by_visible_text(optionToSelect)

        if waitAfter > 0:
            self.wait_time(waitAfter)

    def save_results(self, resultSet, fileLocation, delimiter, waitBefore=0, waitAfter=0):
        if waitBefore > 0:
            self.wait_time(waitBefore)

        with open(fileLocation, 'w') as fileHandle:
            for row in resultSet:
                rowLength = len(row)
                valueCounter = 1
                for value in row:
                    if valueCounter == rowLength:
                        fileHandle.write('%s' % value)
                    else:
                        fileHandle.write('%s' % value + delimiter + ' ')
                    valueCounter += 1
                fileHandle.write('\n')
                valueCounter = 1

        if waitAfter > 0:
            self.wait_time(waitAfter)
