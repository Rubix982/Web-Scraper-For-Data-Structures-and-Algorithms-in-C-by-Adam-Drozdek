from requests_html import HTMLSession
import requests

# Printing decoration
# name is a list, index is an int, returns nothing
def printDecor(name : list, index: int) -> None:

    '''
        Function takes two arguments
        printDecor(name_of_the_list_to_access, index_to_access)

        name_of_list_to_access is 'list' type, index_to_access is an 'int'

        return nothing

        Simple function to print a line to show a progress bar for the download
    '''

    to_format = "".join(name[index])

    print(" File \"%-32s\" downloaded:  " % to_format, end="")
    
    for i in range(index):
        print(bytes((219,)).decode('cp437'), end="")

    for i in range(len(name)-index):
        print(" ", end="")

    print(f" : [{index}:{len(name) - 1}]")

    return None

def main():
    main_html_page = "http://www.mathcs.duq.edu/drozdek/DSinCpp/"

    session = HTMLSession()
    r = session.get(main_html_page)

    contents = r.html.find('ul li a')

    link_name = []                                  # List of the names of the files
    file_links = []                                 # Absolute links of the files
    
    for link in contents:
        link_name.append(link.links)                # Put all the names in a single list
        file_links.append(link.absolute_links)      # Put all the absolute links in another list 

    # Go through each element stored in the list of 
    # absolute links  
    for link_index, link in enumerate(file_links):  

        try:
            # Send a request to 'get' the data from the link, 
            # return the data to download_link
            download_link = requests.get("".join(link))      
        except Exception as e:
            print("Sorry, this file does not exist, {0} {1}\n ".format(link_index, e))

        # Logic to write files locally
        with open("".join(link_name[link_index]), "wb") as html_file:
            html_file.write(download_link.content)

        printDecor(link_name, link_index)
        
        print()

if __name__ == "__main__":
    main()