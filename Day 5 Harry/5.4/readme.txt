units are: px, rem, em, vh, vw, %

px: Not the best thing to use, because it will be different for each monitor as they may have differerent resolutions.

vw: used as a percentage and is based upon the viewport width, then we can also use margin auto if vw is not 100 to centre the element. But this will only work if it is an block level element, if it is an inline element then it will not center.

vh is very similar but it works with height instead of width, pffft

em: means to change the size that was going to be inherited by the parent container, e.g if the parent container was supposed to have  font size of 10 then using 2em would give us a font size of 20 and 3 em would give us a font size of 30

vmin and vmax are used to change based on the minimum and maximum from height and width of the viewport 

min and max are used to define the maximum and minimum values an element may have

percentages means the this much percentage of the parent container.

rem: means to change from the root element, root element is the element called html because it is at the root of everything in html. so usign rem would change the new child with respect to the property inherited from the root.
also you cannot apply width on span elements so span would look really bad, with these properties.