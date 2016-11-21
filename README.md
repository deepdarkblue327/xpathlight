# XPathLight
A lightweight xpath helper (in Python) which helps scraping websites easy and drastically reduce the lines of code needed.

Now scraping has become much easier with this flexible tool.

To use:
#Passed browser needs browser initialisation

```
from selenium import webdriver
browser = webdriver.Chrome()
```
#Pass the above browser to XPathLight

```
import XPathLight
xpl = XPathLight(browser)
```

#Functionality

Now use xpl to find an element, click an element, get the text of an element, see if an element is clickable, get a list of all elements having an attribute, fill a text form or even get a list of all elements.

```
xpl.find(tag="\*",attrs={},className="",idName="",name="",xpath="",wait=100)
```

Use any one of the arguments above to find the element you need. If it doesnt find the element, it will return false with a time out error message.

With similar attributes you can do the following:

```
xpl.findAll(SAME_ATTRIBUTES)
xpl.text(SAME_ATTRIBUTES)
xpl.texts(SAME_ATTRIBUTES)
xpl.click(SAME_ATTRIBUTES)
xpl.fill(SAME_ATTRIBUTES)
xpl.clickable(SAME_ATTRIBUTES)
```

#Other Examples

You can also use tag along with attrs to get a specific tag you need:

```
xpl.find("div",{"class":"input"})
```

Will keep updating more functionalities.
