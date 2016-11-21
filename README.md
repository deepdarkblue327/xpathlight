# XPathLight
A lightweight xpath helper (in Python) which helps scraping websites easy and drastically reduce the lines of code needed.

Now scraping has become much easier with this flexible tool.

To use:
#Passed browser needs browser initialisation

```python
from selenium import webdriver
browser = webdriver.Chrome()
```
#Pass the above browser to XPathLight

```python
import XPathLight
xpl = XPathLight(browser)
```

#Functionality

Now use xpl to find an element, click an element, get the text of an element, see if an element is clickable, get a list of all elements having an attribute, fill a text form or even get a list of all elements.

```python
#returns element or False bool
xpl.find(tag="\*",attrs={},className="",idName="",name="",containsText="",xpath="",wait=10) 
```

Use any one of the arguments above to find the element you need. If it doesnt find the element, it will return false with a time out error message.

With similar attributes you can do the following examples:

```python
xpl.findAll(attrs={"value":"10"}) #returns list of elements
xpl.text(idName="title") #returns text string or False bool
xpl.texts(className="headers") #return list of text string
xpl.click(containsText="Movies &") #returns True or False bool
xpl.fill(name="q") #returns True or False bool
xpl.clickable(tag="button") #returns element or False bool
```

#Other Examples

You can also use tag along with attrs to get a specific tag you need:

```python
xpl.find("div",{"class":"input"},wait=3)
```
wait value is in seconds.
It just means that the method will keep searching for that element for 3 seconds or whatever value you give.

Go to ```C:\Python27\Lib\site-packages``` and put the contents of this git (Along with init.py) in a folder. Then import XPathLight directly into your python scripts.

Will keep updating more functionalities.
