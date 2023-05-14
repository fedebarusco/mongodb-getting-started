# MongoDB Getting Started

**Project Name**: *Bookstore Inventory Management System*

This repository is an example project that combines MongoDB and Python to build a bookstore inventory management system using MongoDB as the database and Python for the backend. The system will allow users to add, update, and delete books from the inventory, as well as search for books based on different criteria.

This is just a high-level overview of a project combining MongoDB and Python. It can be expanded on this foundation or customized it to fit the specific requirements.

## Table of Contents
* [General Information](#general-information)
* [Technologies Used](#technologies-used)
* [Project Overview](#project-overview)
* [Functions](#functions)
    * [min_max_dates(date_list)](#min_max_datesdate_list)
    * [check_missing_dates(df)](#check_missing_datesdf)
    * [check_null_countries(df)](#check_null_countriesdf)
    * [main](#main)
* [Tests](#tests)
    * [test_min_max_dates](#test_min_max_dates)
    * [test_check_missing_dates](#test_check_missing_dates)
    * [test_check_null_countries](#test_check_null_countries)
* [Usage](#usage)


## General Information

The repository is organized as follows:

    .
    ├── data                                                      # Input data
    |   ├── ...                                                   # Original input data
    |   └── ...                                                   # Test data for unit tests
    ├── .gitignore                                                # Git ignored files
    ├── app.py                                                    # Main script
    ├── bootstrap.sh                                              # Bootstrap script
    ├── config.toml                                               # Configuration file
    ├── Inventory_Management_System.postman_collection.json       # Postman collection
    ├── README.md                                                 # README
    ├── requirements.txt                                          # Requirements for pip
    ├── test.py                                                   # Unit tests
    └── utils.py                                                  # Utils


## Technologies Used

* MongoDB - version 6.0.5 - NoSQL database that will store the book inventory data
* Python - version 3.10.6 - Programming language used for the backend development and interaction with the MongoDB database
* Flask - version 2.3.2 - Lightweight web framework for Python that will handle the HTTP requests and responses
* pymongo - version 4.3.3 - Python library that provides a convenient interface for interacting with MongoDB from Python

## Features

* Add Book: Users can add new books to the inventory by providing details such as title, author, genre, and quantity.
* Update Book: Users can update the details of existing books, including title, author, genre, and quantity.
* Delete Book: Users can remove books from the inventory based on the book ID.
* Search Books by ID: Users can search for books in the inventory based on the book ID.
* [TODO] Search Books: Users can search for books based on criteria such as title, author, or genre, and retrieve a list of matching books.
* Display Inventory: Users can view the complete inventory of books, including all details.

## Implementation Steps

1. Set up MongoDB: Install MongoDB and start the MongoDB server.
2. Create a new MongoDB database and collection to store the book inventory data.
3. Set up a Python virtual environment and install the necessary dependencies (Flask and pymongo).
4. Create a Flask application with routes to handle the different functionalities of the bookstore management system (add, update, delete, search, display).
5. Implement the necessary Python functions to interact with the MongoDB database using pymongo. This includes connecting to the database, performing CRUD operations, and handling search queries.
7. Test the application by running the Flask development server and interacting with the different functionalities.

## MongoDB 

### Installation

This guide is based on Ubuntu 22.04.2 LTS ("Jammy") running through WSL2. To check the version of Ubuntu installed on your system you can use the ``lsb_release`` command: 
```console
lsb_release -a
```

In order to install MongoDB Community Edition using the ``apt`` package manager, replicate the following steps: 
1. From a terminal, install ``gnupg`` if it is not already installed:
    ```console
    sudo apt-get update
    sudo apt-get install gnupg
    ```
    Then, import the MongoDB public GPG Key from https://pgp.mongodb.com/server-6.0.asc:
    ```console
    curl -fsSL https://pgp.mongodb.com/server-6.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg --dearmor
   ```
2. Create the list file /etc/apt/sources.list.d/mongodb-org-6.0.list: 
    ```console
    echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
    ```
3. Reload the local package database: 
    ```console
    sudo apt-get update
    ```
4. Install the latest stable version of MongoDB: 
    ```console
    sudo apt-get install -y mongodb-org
    ```
    **Note:** remember that ``apt-get`` will upgrade the packages when a newer version becomes available. 

By installing MongoDB by using the package manager, the data directory ``/var/lib/mongodb`` and the log directory ``/var/log/mongodb`` are created during the installation.

By default, MongoDB runs using the ``mongodb`` user account. If you change the user that runs the MongoDB process, you must also modify the permission to the data and log directories to give this user access to these directories.

The official MongoDB package includes a configuration file (``/etc/mongod.conf``). These settings (such as the data directory and log directory specifications) take effect upon startup. That is, if you change the configuration file while the MongoDB instance is running, you must restart the instance in order to apply the changes.


### Running MongoDB

To check which init system (``systemd`` or ``service``) your platform uses in order to run mongod, run the following command:
```console
ps --no-headers -o comm 1
```

Run and manage the ``mongod`` process by using the operating system's built-in init system (e.g. ``systemd``).
1. Start the mongod process by running the following command: 
    ```console
    sudo systemctl start mongod
    ```
2. Verify that MongoDB has started successfully: 
    ```console
    sudo systemctl status mongod
    ```
3. Begin using MongoDB by starting a mongosh session on the same host machine as the mongod: 
    ```console
    mongosh
    ```

### Basic Terms

#### Database
Database is a physical container for collections. Each database gets its own set of files on the file system. A single MongoDB server typically has multiple databases.

#### Collection
Collection is a group of documents and is similar to an RDBMS table. A collection exists within a single database. Collections do not enforce a schema. Documents within a collection can have different fields.

#### Document
A document is a set of key-value pairs. Documents have dynamic schema. Dynamic schema means that documents in the same collection do not need to have the same set of fields or structure, and common fields in a collection’s documents may hold different types of data.

### Useful commands

Some of the basic commands are the following ones: 
- Finding the current database you’re in: ``test`` is the initial database that comes by default.
    ```console
    db
    ```
- Listing databases:
    ```console
    show databases
    ```
- Change database (and create a new one if it doesn't exists):
    ```console
    use <your_db_name>
    ```
- Deleting database:
    ```console
    db.dropDatabase()
    ```
- Create a collection: 
    ```console
    db.createCollection("testCollection")
    ```
- Insert data into a collection (and create a collection if it doesn't exists) can be done in several ways: 
    - insertOne() to insert a single document only: 
        ```console
        db.testCollection.insertOne({"title": "The Da Vinci Code", "author":"Dan Brown", "genre":"Thriller"})
        ```
    - insertMany() to insert more than one document: 
        ```console
        db.testCollection.insertMany(
            [
                {
                    "title":"The Great Gatsby",
                    "author":"F. Scott Fitzgerald",
                    "genre":"Classic",
                    "publisher":"Scribner",
                    "publication_date":new Date("1925-04-10"),
                    "ISBN":"9780743273565",
                    "quantity":100,
                    "price":9.99
                },
                {
                    "title":"To Kill a Mockingbird",
                    "author":"Harper Lee",
                    "genre":"Classic",
                    "publisher":"J. B. Lippincott & Co.",
                    "publication_date":new Date("1960-07-11"),
                    "ISBN":"9780061120084",
                    "quantity":75,
                    "price":8.99
                },
                {
                    "title":"1984",
                    "author":"George Orwell",
                    "genre":"Classic",
                    "publisher":"Secker & Warburg",
                    "publication_date":new Date("1949-06-08"),
                    "ISBN":"9780451524935",
                    "quantity":50,
                    "price":7.99
                },
                {
                    "title":"The Lord of the Rings",
                    "author":"J. R. R. Tolkien",
                    "genre":"Fantasy",
                    "publisher":"George Allen & Unwin",
                    "publication_date":new Date("1954-07-29"),
                    "ISBN":"9780547928203",
                    "quantity":120,
                    "price":12.99
                },
                {
                    "title":"Harry Potter and the Philosopher's Stone",
                    "author":"J. K. Rowling",
                    "genre":"Fantasy",
                    "publisher":"Bloomsbury",
                    "publication_date":new Date("1997-06-26"),
                    "ISBN":"9781408855652",
                    "quantity":200,
                    "price":10.99
                },
                {
                    "title":"The Hunger Games",
                    "author":"Suzanne Collins",
                    "genre":"Science Fiction",
                    "publisher":"Scholastic",
                    "publication_date":new Date("2008-09-14"),
                    "ISBN":"9780439023481",
                    "quantity":150,
                    "price":11.99
                },
                {
                    "title":"The Catcher in the Rye",
                    "author":"J. D. Salinger",
                    "genre":"Classic",
                    "publisher":"Little, Brown and Company",
                    "publication_date":new Date("1951-07-16"),
                    "ISBN":"9780316769174",
                    "quantity":80,
                    "price":9.99
                }
            ]
        )
        ```
    **Note**: Whenever you insert a document, MongoDB automatically adds an ``_id`` field which uniquely identifies each document.
- Query all data from a collection:
    ```console
    db.testCollection.find().pretty()
    ```
- Display some specific document:
    ```console
    db.testCollection.find(
        {
        title: "The Catcher in the Rye"
        }
    )
    ```
    It is also possible to use operators like ``$lt``, ``$lte``, ``$gt``, ``$gte``, ``$ne`` to filter out the documents according to the condition:
    ```console
    db.testCollection.find(         
        {
            quantity : {$lt : 100}         
        }
    )
    ```
- Updating documents (the first argument is the field of which document you want to update):
    ```console
    db.testCollection.update({price : 9.99}, {$set: {price: 8.99}})
    ```
    If you need to remove a property from a single document: 
    ```console
    db.testCollection.update({title: "The Hunger Games"}, {$unset: {quantity:""}});
    ```
- Limit method:
    ```console
    db.testCollection.find().limit(2)
    ```
- Sort method (accepts a document containing a list of fields along with their sorting order, 1 for ascending order, -1 for descending order):
    ```console
    db.testCollection.find().sort({title: 1})
    ```
- Removing a document:
    ```console
    db.testCollection.remove({title: "The Catcher in the Rye"});
    ```
- Removing a collection (delete all the documents along with the collection itself):
    ```console
    db.testCollection.remove({});
    ```
- Dropping a collection (remove all the documents inside a collection):
    ```console
    db.testCollection.drop()
    ```

### Indexing

Indexes in MongoDB are essential for efficient query resolution. When a collection lacks indexes, MongoDB has to scan every document in the collection to find the ones that match a query. This scan is highly inefficient and results in processing a large volume of data.
To optimize query performance, MongoDB employs indexes, which are special data structures that store a subset of the data in a format that is easy to traverse. Indexes store the values of specific fields or sets of fields and organize them based on the specified field values.
MongoDB offers a diverse set of index types and features, including support for language-specific sort orders, enabling efficient access to data with complex query patterns. Indexes can be created and dropped as needed, allowing for adaptability to evolving application requirements and query patterns. Furthermore, indexes can be declared on any field within your documents, including fields nested within arrays.
By utilizing MongoDB's index functionality effectively, you can significantly improve the speed and efficiency of your queries, reducing the need for full collection scans and enhancing overall performance.

In order to make the best use of indexes in MongoDB, there are some best practices: 
- **Compound indexes** in MongoDB are indexes that encompass multiple fields. Instead of creating separate indexes for individual fields like "last_name" and "first_name" in a collection, it is generally more efficient to create a compound index that includes both fields if queries involve both names. It's worth noting that a compound index can still be utilized to filter queries that only specify one of the fields included in the index. By leveraging compound indexes, you can optimize query performance by providing efficient access to data based on multiple fields simultaneously. 
- **Follow the ESR rule** to establish the order of fields in the compound index: 
    - First, add those fields against which **Equality** queries are run.
    - Then, fields that should reflect the **Sort** order of the query.
    - The last fields represent the **Range** of data to be accessed.  
- **[Covered queries](https://www.mongodb.com/docs/manual/core/query-optimization/#covered-query)** in MongoDB are beneficial because they retrieve results directly from an index without the need to access the source documents. It is important to note that by default, the `_id` field is always returned, so if you want to achieve covered queries, you must explicitly exclude it from the query results or include it in the index.
In the case of sharded clusters, MongoDB internally requires access to the fields of the shard key. Therefore, covered queries are only possible when the shard key is included in the index. Including the shard key in the index is generally recommended as a best practice.
By utilizing covered queries, you can enhance query performance by reducing the amount of data retrieval and minimizing disk I/O, resulting in more efficient operations.
Tip: To determine whether a query is a covered query, use the ``explain()`` method. 
- **Pay attention on fields cardinality**, because queries on fields with a small number of unique values (low cardinality) can return large result sets. 
- **Eliminate Unnecessary Indexes**, because indexes are resources-intensive. Tip: MongoDB provides tooling to help you understand index usage. 
- **Wildcard Indexes Are Not a Replacement for Workload-Based Index Planning**: For workloads with many ad-hoc query patterns or that handle highly polymorphic document structures, [wildcard indexes](https://www.mongodb.com/docs/manual/core/index-wildcard/) give you a lot of extra flexibility. You can define a filter that automatically indexes all matching fields, subdocuments, and arrays in a collection.
- **Use text search to match words inside a field**: Regular indexes are useful for matching the entire value of a field, instead, if you only want to match on a specific word in a field with a lot of text, then use a [text index](https://www.mongodb.com/docs/manual/core/index-text/#std-label-index-feature-text).
- **Use Partial Indexes** to reduce the size and performance overhead of indexes by only including documents that will be accessed through the index. For example, create a partial index on the ``orderID`` field that only includes order documents with an ``orderStatus`` of "In progress", or only indexes the ``emailAddress`` field for documents where it exists.
- **Use a multi-key index** if your query patterns require accessing individual array elements. 
- **Avoid Regular Expressions That Are Not Left Anchored or Rooted**, leading wildcards are inefficient and may result in full index scans, while trailing wildcards can be efficient if there are sufficient case-sensitive leading characters in the expression.
- **Avoid Case Insensitive Regular Expressions**, otherwise use a case insensitive index instead. 
- **Use Index Optimizations Available in the WiredTiger Storage Engine** to place indexes on their own separate volume, allowing for faster disk paging and lower contention. 
- **Use the MongoDB Explain Plan** to check on index coverage for invidivual queries. MongoDB provides visualization tools to help further improve understanding of your indexes, and which provides intelligent and automatic recommendations on which indexes to add. 
- **Visualize Index Coverage With MongoDB Compass**, the free GUI for MongoDB which provides many features to help optimize query performance. The "indexes" tab displays a list of indexes for a collection, providing information such as the index name, keys, type, size, and any special properties. An important aspect is the index usage feature, which indicates how frequently an index has been utilized. This information can be valuable in understanding the effectiveness of indexes and identifying opportunities for further optimization. MongoDB Compass serves as a helpful tool for exploring the database schema, analyzing query explain plans, and gaining insights into index performance.

#### Indexing methods

MongoDB provides a set of methods about indexing: 
- createIndex() (the key is the name of the field on which you want to create index and the values is the order):
    ```console
    db.testCollection.createIndex({"title":1})
    ```
- dropIndex():
    ```console
    db.testCollection.dropIndex({"title":1})
    ```
- dropIndexes() (deletes multiple (specified) indexes on a collection):
    ```console
    db.testCollection.dropIndexes()
    ```
- getIndexes() (returns the description of all the indexes int the collection):
    ```console
    db.testCollection.getIndexes()
    ```

### Logical Operators

MongoDB provide logical operators that can be used to construct complex queries by combining multiple conditions. These operators allow you to perform logical operations, such as logical AND, OR, and NOT, on the query criteria.
- The ``$and`` operator combines multiple query expressions, specifying that all conditions must be met for a document to match the query. This is equivalent to the logical AND operation.
- The ``$or`` operator combines multiple query expressions, indicating that at least one condition must be met for a document to match the query. This is similar to the logical OR operation.
- The ``$not`` operator performs a logical NOT operation on the specified query expression, excluding documents that match the condition.
These logical operators provide flexibility in constructing complex queries and enable you to retrieve documents based on multiple conditions. By utilizing these operators effectively, you can build powerful and precise queries in MongoDB.

An example of query that uses the logical operator ``$and`` to display books whose price is less than 10, and also whose genre is Classic: 
```console
db.testCollection.find({$and:[{price : {$lt : 10}}, {city: "Classic"}]});
```

### Advantages of MongoDB over RDBMS

- Schema less − MongoDB is a document database in which one collection holds different documents. Number of fields, content and size of the document can differ from one document to another.
- Structure of a single object is clear.
- No complex joins.
- Deep query-ability. MongoDB supports dynamic queries on documents using a document-based query language that’s nearly as powerful as SQL.
- Tuning.
- Ease of scale-out − MongoDB is easy to scale.
- Conversion/mapping of application objects to database objects not needed.
- Uses internal memory for storing the (windowed) working set, enabling faster access of data.

## Project Overview

### Data Model

In a Bookstore Inventory Management System, you could have several collections within the MongoDB database to organize and store the data effectively. Here are some possible collections:
- **Books**: This collection would store information about each book in the inventory, such as title, author, genre, publisher, publication date, ISBN, quantity, price, and any other relevant details.
- **Authors**: This collection keep track of information specific to authors, such as their names, biographies, and other metadata. This collection would have a relationship with the "Books" collection, where each book document would reference the corresponding author(s).
- **Publishers**: Similar to the "Authors" collection, a "Publishers" collection can store information about book publishers. This collection could include publisher names, contact information, and other relevant details. Again, there would be a relationship between the "Books" collection and the "Publishers" collection, with each book document referencing the publisher.
- **Genres**: To categorize books by genres, you could create a "Genres" collection to store different genres. Each genre document would contain information such as the genre name and possibly a description. The "Books" collection would then reference the corresponding genre for each book.

These are just a few examples of collections that could be included in a Bookstore Inventory Management System. The specific collections you choose would depend on the system's requirements and the level of detail to track for books, authors, publishers, and other related entities.

For this specific example, we will create only the books collection to store the following informations about each book: title, author, genre, publisher, publication date, ISBN, quantity, price.  

### Setup MongoDB

1. Start the mongod process by running the following command: 
    ```console
    sudo systemctl start mongod
    ```
2. Start a mongosh session on the same host machine as the mongod: 
    ```console
    mongosh
    ```
3. Create a new database: 
    ```console
    use bookstore_inventory
    ```
4. Create a new collection: 
    ```console
    db.createCollection("books")
    ```
5. Insert some rows:
    ```console
    db.books.insertMany([ { "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Classic", "publisher": "Scribner", "publication_date": new Date("1925-04-10"), "ISBN": "9780743273565", "quantity": 100, "price": 9.99 }, { "title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Classic", "publisher": "J. B. Lippincott & Co.", "publication_date": new Date("1960-07-11"), "ISBN": "9780061120084", "quantity": 75, "price": 8.99 }, { "title": "1984", "author": "George Orwell", "genre": "Classic", "publisher": "Secker & Warburg", "publication_date": new Date("1949-06-08"), "ISBN": "9780451524935", "quantity": 50, "price": 7.99 }, { "title": "The Lord of the Rings", "author": "J. R. R. Tolkien", "genre": "Fantasy", "publisher": "George Allen & Unwin", "publication_date": new Date("1954-07-29"), "ISBN": "9780547928203", "quantity": 120, "price": 12.99 }, { "title": "Harry Potter and the Philosopher's Stone", "author": "J. K. Rowling", "genre": "Fantasy", "publisher": "Bloomsbury", "publication_date": new Date("1997-06-26"), "ISBN": "9781408855652", "quantity": 200, "price": 10.99 }, { "title": "The Hunger Games", "author": "Suzanne Collins", "genre": "Science Fiction", "publisher": "Scholastic", "publication_date": new Date("2008-09-14"), "ISBN": "9780439023481", "quantity": 150, "price": 11.99 }, { "title": "The Catcher in the Rye", "author": "J. D. Salinger", "genre": "Classic", "publisher": "Little, Brown and Company", "publication_date": new Date("1951-07-16"), "ISBN": "9780316769174", "quantity": 80, "price": 9.99 }, { "title": "The Da Vinci Code", "author": "Dan Brown", "genre": "Thriller", "publisher": "Doubleday", "publication_date": new Date("2003-03-18"), "ISBN": "9780385504201", "quantity": 60, "price": 8.99 }])
    ```

## Usage

1. Clone/Download the repository.
2. Move to the cloned/downloaded directory, create a virtual environment (e.g. ``python3 -m venv venv``) and activate it (e.g. ``. venv/bin/activate``)
3. Install packages from requirements (e.g. ``pip3 install -r requirements.txt``)
4. Run the script using the following command
    ```console
    python3 app.py
    ```
5. Import the postman collection available in the repository and use the requests

### Endpoints

- GET /: Returns a welcome message as the homepage of the bookstore inventory management system.
- GET /items: Retrieves all items from the inventory collection.
- GET /items/<item_id>: Retrieves a specific item from the inventory by its ID.
- POST /items: Adds a new item to the inventory collection.
- PUT /items/<item_id>: Updates an existing item in the inventory by its ID.
- DELETE /items/<item_id>: Deletes an item from the inventory by its ID.

## Tests

To check that the functions output the expected value, the following unit tests were implemented: 
- ``test_connect_to_collection``: Tests the connection to the MongoDB collection and verifies the connection details.
- ``test_homepage``: Tests the homepage route and checks if the response message is correct.
- ``test_get_all_items``: Tests the route to retrieve all items from the inventory and checks if the response is a list.
- ``test_get_one_item``: Tests the route to retrieve a specific item from the inventory and verifies the item ID in the response.
- ``test_add_item``: Tests the route to add a new item to the inventory and checks if the response contains the ID of the inserted item.
- ``test_update_item``: Tests the route to update an existing item in the inventory and verifies the success message in the response.
- ``test_delete_item``: Tests the route to delete an item from the inventory and verifies the success message in the response.

The tests are only run when the script is executed directly, so, to run all the tests defined in the ``TestBookstoreInventory`` class, once performed the setup steps described in the [Setup MongoDB](#setup-mongodb) section, simply execute the script:
```console
python3 test.py
```

# Credits

- [Install MongoDB Community Edition on Ubuntu](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/)
- [All Basics of MongoDB in 10 Minutes](https://medium.com/nerd-for-tech/all-basics-of-mongodb-in-10-minutes-baddaf6b6625)
- [MongoDB Performance Best Practices: Indexing](https://www.mongodb.com/blog/post/performance-best-practices-indexing)