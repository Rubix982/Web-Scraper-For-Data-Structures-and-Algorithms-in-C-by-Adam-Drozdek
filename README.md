# Data Structures and Algorithms in C++ 4th Edition, Adam Drozdek, Code
![Picture of the book](https://images-na.ssl-images-amazon.com/images/I/51q5Zu5XsNL._SX402_BO1,204,203,200_.jpg) 
with

![Hey, it's Python!](https://www.python.org/static/img/python-logo.png)

---
# Why?

Recently my semester started, and a course book from Data Structures had some code that I could not find the online repository for, but what I did manage to get was a list of links that the author had uploaded for the source code ( http://www.mathcs.duq.edu/drozdek/DSinCpp/ ).

Fun fact, the links in total are 53. So that is individually clicking, downloading and extracting files from a .zip file for each and every link.

So naturally, as anyone would ever do, I decided to web scrape it with Python.

~~Or simply because I was too lazy to download all 53 files.~~

---
# About

This project is simply a python file that uses the _**requests**_ and _**html-requests**_ library from Python to extract files from an html page. Very limited to just a special case, but did it anyways as a fun exercise.

---
# Tech
    
* [requests] - For sending requests to 'get' the html page 
* [requests-html] - To access the page and parse the HTML
* [pip3] - Your neighbor-hood friendly package manager for Python3

---
## 1): Use Python!

1): Remember to always update and upgrade first ( if you're in linux )!

```sh
> sudo apt-get update && apt-get upgrade
```
2): This script was written using Python 3.6.8 and Ubuntu 18.04 LTS, but the OS shouldn't matter. If your have Python 2.x, just remove the parenthesis( () ) of the print functions.

3): Clone the project from Github
```sh
> git clone link_to_be_updated
```

3): Change into the directory, and activate the virtual environment. Make sure you have virtualenv setup on your machine. Don't have _**virtualenv**_, or want to learn how to set it up? Here is an excellent guide: https://realpython.com/python-virtual-environments-a-primer/

```sh
> cd new_folder
> source listing/bin/activate
```

Your hostname/username should change to something like this:

```sh
> (listing) saif:~/Desktop/new_folder
```

Where listing is the virtualenv activated, and new_folder is where it is stored in.

4): Now just install the dependencies:

```sh
> pip3 install -r requirements.txt
```
5): Finally, run the script to download the files:

```sh
> python3 list_files.py
```

6): To deactivate, just

```sh
> deactivate
```

Which changes your prompt back to:

```sh
saif:~/Desktop/new_folder
```

## 2): Or, just download the .zip that contains all the files

Looks like I forgot to upload the link to that here. Maybe come back soon... ? 
¯\\__(ツ)__/¯ Oops!

---
# License

MIT

---
# Special Thanks...

... to [Dillinger] for helping it out with the mark-down. I'm really, really, _**REALLY**_ bad at remember names and syntax for stuff, so naturally [Stack Overflow] and [Dillinger] helped me out with that.

---
# End
Thanks for checking this repo! I hope it was useful for you.

The [author] himself!
![Picture of author](http://www.mathcs.duq.edu/pics/drozdek2.jpg)

Just certain tags for Google SEO: #DataStructures #AdamDrozdek #C++ #Code #WebScraper

   [requests]: <https://2.python-requests.org/en/master/>
   [requests-html]: <https://html.python-requests.org/>
   [pip3]: <https://pip.pypa.io/en/stable/>
   [Dillinger]: <https://dillinger.io/>
   [Stack Overflow]: <https://stackoverflow.com/questions/50837798/how-create-md-file-with-python>
   [Picture of Author]: <http://www.mathcs.duq.edu/pics/drozdek2.jpg>
   [author]: <http://www.mathcs.duq.edu/drozdek/>
