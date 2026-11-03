# PageRank Algorithm

import numpy as np  # Imports NumPy library for numerical calculations

# Each page contains the pages it links to

pages = {  # Creates a dictionary representing web pages and their outgoing links
    "A": ["B", "C"],  # Page A links to pages B and C
    "B": ["C"],  # Page B links to page C
    "C": ["A"],  # Page C links to page A
    "D": ["C"]  # Page D links to page C
}

page_names = list(pages.keys())  # Extracts all page names from the dictionary
n = len(page_names)  # Calculates the total number of web pages

# Initial PageRank value for every page
rank = {page: 1 / n for page in page_names}  # Assigns equal initial PageRank to every page

# Damping factor
d = 0.85  # Sets the probability of following links instead of randomly jumping

for iteration in range(100):  # Repeats the PageRank calculation 100 times

    new_rank = {}  # Creates an empty dictionary to store updated PageRank values

    for page in page_names:  # Loops through each web page

        # Random jump probability
        new_rank[page] = (1 - d) / n  # Calculates the probability of randomly jumping to a page

        # Find pages that link to the current page
        for source in page_names:  # Checks every page to find incoming links

            if page in pages[source]:  # Checks whether the source page links to the current page

                # Number of outgoing links from source page
                outgoing_links = len(pages[source])  # Counts the number of links from the source page

                if outgoing_links > 0:  # Checks whether the source page has at least one outgoing link
                    new_rank[page] += (
                        d * rank[source] / outgoing_links  # Adds the PageRank contribution from the source page
                    )

    rank = new_rank  # Updates the old PageRank values with the newly calculated values

print("PageRank Values")
print("----------------")

for page, value in sorted(  # Sorts web pages according to their PageRank values
    rank.items(),  # Gets page names and their corresponding PageRank values
    key=lambda x: x[1],  # Uses the PageRank value for sorting
    reverse=True  # Displays pages in descending order (highest to lowest)
):
    print(page, ":", round(value, 6))  # Displays page name and PageRank rounded to 6 decimal places