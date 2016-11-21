from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

class XPathLight:
    def __init__(self,browser):
        self.browser = browser
        
    def find(self,tag="*", attrs={}, idName="", className="",name="",containsText="",xpath="",wait=10):
        if tag != "*" and len(attrs) == 0:
            try:
                element = WebDriverWait(self.browser, wait).until(EC.presence_of_element_located((By.TAG_NAME,tag)))
            except TimeoutException as e:
                print "Element Not Found. Timeout " + str(wait) + "s"
                return False
            return element
        if idName != "":
            try:
                element = WebDriverWait(self.browser, wait).until(EC.presence_of_element_located((By.ID,idName)))
            except TimeoutException as e:
                print "Element Not Found. Timeout " + str(wait) + "s"
                return False
            return element
        if className != "":
            try:
                element = WebDriverWait(self.browser, wait).until(EC.presence_of_element_located((By.CLASS_NAME,className)))
            except TimeoutException as e:
                print "Element Not Found. Timeout " + str(wait) + "s"
                return False
            return element
        if name != "":
            try:
                element = WebDriverWait(self.browser, wait).until(EC.presence_of_element_located((By.NAME,name)))
            except TimeoutException as e:
                print "Element Not Found. Timeout " + str(wait) + "s"
                return False
            return element
        if containsText != "":
            try:
                element = WebDriverWait(self.browser, wait).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,containsText)))
            except TimeoutException as e:
                print "Element Not Found. Timeout " + str(wait) + "s"
                return False
            return element
        if xpath != "":
            try:
                element = WebDriverWait(self.browser, wait).until(EC.presence_of_element_located((By.XPATH,xpath)))
            except TimeoutException as e:
                print "Element Not Found. Timeout " + str(wait) + "s"
                return False
            return element
        try:
            element = WebDriverWait(self.browser, wait).until(EC.presence_of_element_located((By.XPATH,"//"+tag+"[contains(@"+attrs.keys()[0]+",'"+attrs.values()[0]+"')]")))
        except TimeoutException as e:
            print "Element Not Found. Timeout " + str(wait) + "s"
            return False
        return element
    
    def findAll(self,tag="*", attrs={}, idName="", className="",name="",containsText="",xpath="",wait=10):
        if tag != "*" and len(attrs) == 0:
            try:
                elements = WebDriverWait(self.browser, wait).until(EC.presence_of_all_elements_located((By.TAG_NAME,tag)))
            except TimeoutException as e:
                print "Element Not Found. Timeout " + str(wait) + "s"
                return []
            return elements
        if idName != "":
            try:
                elements = WebDriverWait(self.browser, wait).until(EC.presence_of_all_elements_located((By.ID,idName)))
            except TimeoutException as e:
                print "Element Not Found. Timeout " + str(wait) + "s"
                return []
            return elements
        if className != "":
            try:
                elements = WebDriverWait(self.browser, wait).until(EC.presence_of_all_elements_located((By.CLASS_NAME,className)))
            except TimeoutException as e:
                print "Element Not Found. Timeout " + str(wait) + "s"
                return []
            return elements
        if name != "":
            try:
                elements = WebDriverWait(self.browser, wait).until(EC.presence_of_all_elements_located((By.NAME,name)))
            except TimeoutException as e:
                print "Element Not Found. Timeout " + str(wait) + "s"
                return []
            return elements
        if containsText != "":
            try:
                elements = WebDriverWait(self.browser, wait).until(EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT,containsText)))
            except TimeoutException as e:
                print "Element Not Found. Timeout " + str(wait) + "s"
                return []
            return elements
        if xpath != "":
            try:
                elements = WebDriverWait(self.browser, wait).until(EC.presence_of_all_elements_located((By.XPATH,xpath)))
            except TimeoutException as e:
                print "Element Not Found. Timeout " + str(wait) + "s"
                return []
            return elements
        try:
            elements = WebDriverWait(self.browser, wait).until(EC.presence_of_all_elements_located((By.XPATH,"//"+tag+"[contains(@"+attrs.keys()[0]+",'"+attrs.values()[0]+"')]")))
        except TimeoutException as e:
            print "Element Not Found. Timeout " + str(wait) + "s"
            return []
        return elements
    
    def clickable(self,tag="*", attrs={}, idName="", className="",name="",containsText="",xpath="",wait=10):
        if tag != "*" and len(attrs) == 0:
            try:
                element = WebDriverWait(self.browser, wait).until(EC.element_to_be_clickable((By.TAG_NAME,tag)))
            except TimeoutException as e:
                print "Element Not Found. Timeout " + str(wait) + "s"
                return False
            return element
        if idName != "":
            try:
                element = WebDriverWait(self.browser, wait).until(EC.element_to_be_clickable((By.ID,idName)))
            except TimeoutException as e:
                print "Element Not Found. Timeout " + str(wait) + "s"
                return False
            return element
        if className != "":
            try:
                element = WebDriverWait(self.browser, wait).until(EC.element_to_be_clickable((By.CLASS_NAME,className)))
            except TimeoutException as e:
                print "Element Not Found. Timeout " + str(wait) + "s"
                return False
            return element
        if name != "":
            try:
                element = WebDriverWait(self.browser, wait).until(EC.element_to_be_clickable((By.NAME,name)))
            except TimeoutException as e:
                print "Element Not Found. Timeout " + str(wait) + "s"
                return False
            return element
        if containsText != "":
            try:
                element = WebDriverWait(self.browser, wait).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,containsText)))
            except TimeoutException as e:
                print "Element Not Found. Timeout " + str(wait) + "s"
                return False
            return element
        if xpath != "":
            try:
                element = WebDriverWait(self.browser, wait).until(EC.element_to_be_clickable((By.XPATH,xpath)))
            except TimeoutException as e:
                print "Element Not Found. Timeout " + str(wait) + "s"
                return False
            return element
        try:
            element = WebDriverWait(self.browser, wait).until(EC.element_to_be_clickable((By.XPATH,"//"+tag+"[contains(@"+attrs.keys()[0]+",'"+attrs.values()[0]+"')]")))
        except TimeoutException as e:
            print "Element Not Found. Timeout " + str(wait) + "s"
            return False
        return element      
            
    def text(self,tag="*", attrs={}, idName="", className="",name="",containsText="",xpath="",wait=10):
        element = self.find(tag,attrs,idName,className,name,containsText,xpath,wait)
        if element:
            return element.text
        else:
            return False
    
    def fill(self,tag="*", attrs={}, idName="", className="",name="",containsText="",xpath="",value="",wait=10):
        element = self.find(tag,attrs,idName,className,name,containsText,xpath,wait)
        if element:
            element.clear()
            element.send_keys(value)
            return True
        else:
            return False
    
    def click(self,tag="*", attrs={}, idName="", className="",name="",containsText="",xpath="",wait=10):
        element = self.clickable(tag,attrs,idName,className,name,containsText,xpath,wait)
        if element:
            element.click()
            return True
        else:
            return False
        
    def texts(self,tag="*", attrs={}, idName="", className="",name="",containsText="",xpath="",wait=10):
        return [element.text for element in self.findAll(tag,attrs,idName,className,name,containsText,xpath,wait)]