---
toc: true
layout: post
description: CPT Submissions (Trimester 2)
categories: [Trimester 2]
title: Tri 2 CPT Write-Up
---

# Video

My video demonstration of my feature can be found here. 

# Write-Up (Inventory Management System)

## 3a. 

### 3.a.i.

This program is meant to provide a more streamline system for business managers to organize and locate their company's inventory. 

### 3.a.ii.

This program allows a user to not only input entries regarding various attributes of their company's inventory, such as the price of the product, how much it costs to produce, how long it takes to deliver, the quantity, and any other extra notes. The user does this by first defining under what company name this inventory goes under. This is useful because the feature also allows a search feature, where a user may type in the name of a specific company, and any entries made under that name will appear in a neat, organized table that displays each attribute. These entries are all persistent as well, so even if the page is closed and reopened, the entries remain. 


### 3.a.iii.

The inputs of the program are the user's typed entries into the form for which entries are made. The program collects this data and returns an input stating whether or not the inventory was successfully added - depending on if the user's entries met the requirements such as filling out all fields - and then may be called upon to displays its entries within the search feature that neatly formats the attributes in a table. 

## 3b.

### 3.b.i.

![]({{site.baseurl}}/images/cpt1.png)

### 3.b.ii.

![]({{site.baseurl}}/images/cpt2.png)

### 3.b.iii.

The name of the variable representing the collection type is "data", and "teams" is what populates the collection type through an SQLite Database. 

### 3.b.iv.

The data that my list contains is extremely vital to my program since it contains every single unique attribute about the product for the inventory entry. This is absolutely vital to the program as it is able to fetch and store the recieved data in order to populate the tables for when the user searches up the logged inventories of a specific company. 

### 3.b.v.

Without the variable "data", everything will become inefficient as the program would then require some sort of individual variable for each and every unique attribute. This would unneedingly lengthen my code and make it much too bulky and complex. 


