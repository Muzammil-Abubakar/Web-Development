ok so table heirarchy goes something like this, first we add table tag than we add tr for a record, then at first we add th for heading, then we add td for data. 
and then we can apply rowspan and colspan on that stuff

caption tag is used at the start of the table for adding information about the caption

we also have tags like tbody thead and tfoot, these are for grouping the table and applying css on it later on.

then we discussed about ul and ol, these are for unordered list and ordered list. there is also dl and dt and dd, these are for definition list and are used rarely
but atleast they look nice.

we can also change the type of ol using guess what? type attribute

---

Core web vitals, SEO
ok so first is loading of page, if two pages have same data but different loading speed, then the page that will load faster will be given preference by google.

CLS Cumulative layout shift, this means that how much the page is shifting while loading

Then there is largest contentful paint metric, this means that the biggest most important element loads in how much time

*
all these things are available for study at web.dev
*

then there is fid, first input delay, it just means how much time does it take for input to be processed.

all these things can be analyzed by using lighthouse report from google inspect using f12

ok then we also studied about meta description, it is used like this, meta name = description and then we add the content attribute and inside it we add the stuff we want to add as a description

Then we have meta keywords, but now these things are mostly deperecated because they were abused a lot.

for and id should always match in a form tag. also name should be same in radio buttons and also placeholder should be cutesy, huhhh? what does that even mean

br tag is not recommended at all by harry  and i dont know why

anyways next we are going to learn about select tag, and with selection tag we use option variable and inside it we have value attribute, this is important when we want to send data using js

name attribute is used to tell about the key value pair that will be sent to the server

then for input tags we have required tag, autofocus tag and pattern tag