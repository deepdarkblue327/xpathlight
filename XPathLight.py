from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException

class XPathLight:
    def __init__(self,browser):
        self.browser = browser

    def element(self,by=By.ID,value="",wait=10):
        try:
            element = WebDriverWait(self.browser, wait).until(EC.presence_of_element_located((by,value)))
        except TimeoutException as e:
            print "Element Not Found. Timeout " + str(wait) + "s"
            return False
        except StaleElementReferenceException as e:
            try:
                element = WebDriverWait(self.browser, wait).until(EC.presence_of_element_located((by,value)))
            except StaleElementReferenceException as e:
                print "Element not attached after 2 tries"
                return False
        return element

    def elements(self,by=By.ID,value="",wait=10):
        try:
            elements = WebDriverWait(self.browser, wait).until(EC.presence_of_all_elements_located((by,value)))
        except TimeoutException as e:
            print "Element Not Found. Timeout " + str(wait) + "s"
            return []
        except StaleElementReferenceException as e:
            try:
                elements = WebDriverWait(self.browser, wait).until(EC.presence_of_all_elements_located((by,value)))
            except StaleElementReferenceException as e:
                print "Elements not attached after 2 tries"
                return False
        return elements

    def click_element(self,by=By.ID,value="",wait=10):
        try:
            element = WebDriverWait(self.browser, wait).until(EC.element_to_be_clickable((by,value)))
        except TimeoutException as e:
            print "Element Not Found. Timeout " + str(wait) + "s"
            return []
        except StaleElementReferenceException as e:
            try:
                element = WebDriverWait(self.browser, wait).until(EC.element_to_be_clickable((by,value)))
            except StaleElementReferenceException as e:
                print "Elements not attached after 2 tries"
                return False
        return element
    
    def find(self,tag="*", attrs={}, idName="", className="",name="",containsText="",xpath="",wait=10):
        if tag != "*" and len(attrs) == 0:
            return self.element(By.TAG_NAME,tag,wait)
        if idName != "":
            return self.element(By.ID,idName,wait)
        if className != "":
            return self.element(By.CLASS_NAME,className,wait)
        if name != "":
            return self.element(By.NAME,name,wait)
        if containsText != "":
            return self.element(By.PARTIAL_LINK_TEXT,containsText,wait)
        if xpath != "":
            return self.element(By.XPATH,xpath,wait)
        return self.element(By.XPATH,"//"+tag+"[contains(@"+attrs.keys()[0]+",'"+attrs.values()[0]+"')]",wait)
    
    def findAll(self,tag="*", attrs={}, idName="", className="",name="",containsText="",xpath="",wait=10):
        if tag != "*" and len(attrs) == 0:
            return self.elements(By.TAG_NAME,tag,wait)
        if idName != "":
            return self.elements(By.ID,idName,wait)
        if className != "":
            return self.elements(By.CLASS_NAME,className,wait)
        if name != "":
            return self.elements(By.NAME,name,wait)
        if containsText != "":
            return self.elements(By.PARTIAL_LINK_TEXT,containsText,wait)
        if xpath != "":
            return self.elements(By.XPATH,xpath,wait)
        return self.elements(By.XPATH,"//"+tag+"[contains(@"+attrs.keys()[0]+",'"+attrs.values()[0]+"')]",wait)
    
    def clickable(self,tag="*", attrs={}, idName="", className="",name="",containsText="",xpath="",wait=10):
        if tag != "*" and len(attrs) == 0:
            return self.click_element(By.TAG_NAME,tag,wait)
        if idName != "":
            return self.click_element(By.ID,idName,wait)
        if className != "":
            return self.click_element(By.CLASS_NAME,className,wait)
        if name != "":
            return self.click_element(By.NAME,name,wait)
        if containsText != "":
            return self.click_element(By.PARTIAL_LINK_TEXT,containsText,wait)
        if xpath != "":
            return self.click_element(By.XPATH,xpath,wait)
        return self.click_element(By.XPATH,"//"+tag+"[contains(@"+attrs.keys()[0]+",'"+attrs.values()[0]+"')]",wait)
            
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
        element = self.find(tag,attrs,idName,className,name,containsText,xpath,wait)
        if element:
            if self.clickable(tag,attrs,idName,className,name,containsText,xpath,wait):
                element.click()
                return True
            return False
        else:
            return False
        
    def texts(self,tag="*", attrs={}, idName="", className="",name="",containsText="",xpath="",wait=10):
        return [element.text for element in self.findAll(tag,attrs,idName,className,name,containsText,xpath,wait)]
