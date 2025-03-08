Specifity is something like this
inline > ID > class and attribute > element > universal

then we can use important to overwrite everything

and also the origin of the css matters, if it comes from the browser vs there is one that came from the author then the the one written by the author will ahve precedence.

Because of complex selector structure, it is a good practice to give these values to the specifity according to the order defined at the top of document
1000 > 100 > 10 > 1 > 0

pseudo classes also have a specifity of 10
Important has a specifity of 10,000