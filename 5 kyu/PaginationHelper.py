"""5 kyu
PaginationHelper

For this exercise you will be strengthening your page-fu mastery. You will complete the PaginationHelper class, which is
 a utility class helpful for querying paging information related to an array.

The class is designed to take in an array of values and an integer indicating how many items will be allowed per each
page. The types of values contained within the collection/array are not relevant.

The following are some examples of how this class is used:

helper = PaginationHelper(['a','b','c','d','e','f'], 4)
helper.page_count() # should == 2
helper.item_count() # should == 6
helper.page_item_count(0)  # should == 4
helper.page_item_count(1) # last page - should == 2
helper.page_item_count(2) # should == -1 since the page is invalid

# page_index takes an item index and returns the page that it belongs on
helper.page_index(5) # should == 1 (zero based index)
helper.page_index(2) # should == 0
helper.page_index(20) # should == -1
helper.page_index(-10) # should == -1 because negative indexes are invalid

Algorithms
Object-oriented Programming
Classes
Basic Language Features
Fundamentals
Utilities
Arrays
Collections
Lists
Data Structuress
"""


# How this works
class PaginationHelper:

    def __init__(self, collection, items_per_page):
        """
        The constructor takes in an list of items and a integer indicating how many items fit within a single page
        """
        self._items_per_page = items_per_page
        self._pages = tuple(len(collection[i:i + items_per_page]) for i in range(0, len(collection), items_per_page))

    def item_count(self):
        """Returns the number of items within the entire collection"""
        return sum(self._pages)

    def page_count(self):
        """Returns the number of pages"""
        return len(self._pages)

    def page_item_count(self, page_index):
        """
        Returns the number of items on the current page. page_index is zero based
        This method should return -1 for page_index values that are out of range
        """
        try:
            return self._pages[page_index]
        except IndexError:
            return -1

    def page_index(self, item_index):
        """
        Determines what page an item is on. Zero based indexes.
        This method should return -1 for item_index values that are out of range
        """
        return item_index // self._items_per_page if 0 <= item_index < self.item_count() else -1