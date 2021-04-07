#!/usr/bin/python
# -*- coding: utf-8 -*-

# import things
from flask_table import Table, Col

# Declare your table
class ItemTable(Table):
    name = Col("Name")
    description = Col("Description")

# Get some objects
class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
items = [Item(u"小李", u"Description1"),
         Item(u"小王", u"Description2"),
         Item(u"小张", u"Description3")]
# Or, equivalently, some dicts
items = [dict(name="Name1", description="Description1"),
         dict(name="Name2", description="Description2"),
         dict(name="Name3", description="Description3")]

if __name__ == "__main__":
    # Or, more likely, load items from your database with something like

    # Populate the table
    table = ItemTable(items)

    # Print the html
    print(table.__html__())
    # or just {{ table }} from within a Jinja template

