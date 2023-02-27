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


## 3.c.

### 3.c.i.

![]({{site.baseurl}}/images/cpt3.png)

### 3.c.ii.

![]({{site.baseurl}}/images/cpt4.png)

### 3.c.iii.

The procedure here is `loadInventories`. First, it retrieves the DOM element with class teams and deletes all but the first row from its rows collection, effectively clearing its contents. Next, it retrieves the value of an input element with ID user, and if it is an empty string, the function displays an alert and returns. Otherwise, the function makes a fetch request to a local server, passing in the retrieved user value as a query parameter. When the response is received, it is parsed as JSON, and if the resulting array has length greater than zero, the function populates the teams element with a new set of rows, one for each item in the array. This procedure is called in `maybeUser`, which then checks if a user has been previously saved in the local storage and if so, it populates the "user" input field with that value and calls a function to load inventory data associated with that user.

### 3.c.iv.

![]({{site.baseurl}}/images/cpt5.png)

The code defines a function addInventory which starts by collecting input data from a web form using document.getElementById. The function then proceeds to use selection to check if the username field is empty, and if it is, it displays an alert to the user and returns from the function. If the username field is not empty, the function constructs a data object using sequencing, which contains the input values collected earlier. The function then constructs a requestOptions object also using sequencing which includes the data object, and specifies the HTTP method and content type headers for a POST request. The function then uses iteration, in the form of a try-catch block, to handle errors that may occur during the fetch request. Finally, the function uses fetch to send a POST request to a specified URL and logs the success response to the console, as well as displaying an alert to the user.


## 3.d

### 3.d.i.

#### Call One
The user inputs the attributes of their desired inventory and clicks on the "Add Inventory" button. The first call to addInventory procedure passes a non-empty username and all other required arguments to add a new inventory item to the system. This call will execute the entire algorithm, constructing the data object, constructing the requestOptions object, and sending a POST request to the specified URL with the data object as the request body. If the request is successful, a success message will be logged to the console and an alert will be shown to the user indicating that the inventory has been added.


#### Call Two
The second call to addInventory procedure passes an empty string as the username argument. This call will execute only the selection code segment that checks if the username is empty. Since the passed argument is an empty string, the condition in the if statement will evaluate to true, causing an alert to be shown to the user indicating that the entered company is invalid. The rest of the code segments will not execute, and no request will be sent to the server.



### 3.d.ii.

#### Condition(s) tested by Call One
The given procedure, addInventory(), includes two conditional statements to test certain conditions. The first conditional statement tests whether the username variable is empty, which is checked using the if statement if (user === ""). 


#### Condition(s) tested by Call Two
The second conditional statement is not explicitly shown in the code block, but is present in the .catch() block of the fetch() method call. This is a catch-all statement that executes if there are any errors during the HTTP request or response, such as a network error or a server-side error. 


### 3.d.iii.

#### Results of Call One
If the username is indeed empty, then an alert is displayed with the message "Invalid company!" and the procedure exits using the return statement.


#### Results of Call Two
If such an error occurs, then the catch block logs the error to the console using console.error(error).
