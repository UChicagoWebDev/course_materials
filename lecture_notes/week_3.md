class: center, middle
# MPCS 52553: Web Development
## Week 3: Server-Side Rendering with ~~the LAMP Stack~~ 
## a LAMP-ish Stack
---

class: agenda
# HTTP
- CRUD operations, URL parameters, forms and validation
- The Network tab

# Sever-Side Rendering with the LAMP Stack
- PHP scripting, environment variables

# Databases
- SELECT and INSERT
- JOIN

# Lab Exercises
- HTTP Requests with `curl`
- Server-side rendering with PHP
- Exercise 3: A Weblog
---

class: fancyStrong
# HTTP

For a long time, a popular interview question at Google was "What happens when
you type google.com into your browser and hit enter?" I got it myself during
onsite interviews there in 2013.

Much of the answer is about .big[**HTTP**].

![Google Interview Question](images/google_interview.png "Screenshot of Glassdoor.com")

---

# HTTP
> The **Hypertext Transfer Protocol** (**HTTP**) is an application protocol for
distributed, collaborative, hypermedia information systems.[1] HTTP is the
foundation of data communication for the World Wide Web, where hypertext
documents include hyperlinks to other resources that the user can easily access,
for example by a mouse click or by tapping the screen in a web browser.
([Wikipedia](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol))

[HTTP Overview (Mozilla Documentation)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)

[How Browsers Work](https://www.html5rocks.com/en/tutorials/internals/howbrowserswork/)
---

# HTTP: Requests

[HTTP Overview - Requests (Mozilla Documentation)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview#requests)

[HTTP Request Methods (Mozilla Documentation)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods)

![HTTP request diagram showing protocol version, status code, status message, and headers](images/http_request.png "HTTP request diagram")

---
# HTTP: Responses

[HTTP Overview - Responses (Mozilla Documentation)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview#responses)

[HTTP Response Status Codes (Mozilla Documentation)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

![HTTP response diagram showing protocol version, status code, status message, and headers](images/http_response.png "HTTP response diagram")
---

# Lab: HTTP Exercises

`curl` - [cURL (Wikipedia)](https://en.wikipedia.org/wiki/CURL)

`curl -i https://uchicagowebdev.com`

--

```
HTTP/1.1 200 OK
Date: Fri, 07 Apr 2023 20:23:49 GMT
Server: Apache/2.4.56 () OpenSSL/1.0.2k-fips PHP/8.0.27
Upgrade: h2,h2c
Connection: Upgrade
Last-Modified: Sun, 19 Mar 2023 21:27:37 GMT
ETag: "252-5f7477aba1131"
Accept-Ranges: bytes
Content-Length: 594
Content-Type: text/html; charset=UTF-8
<html>
    <head>
        <title>Web Development</title>
        <style>
            body: {width: 960px; margin: auto; padding-top: 2em;}
        </style>
    </head>
    <body>
        <titlebar>
            <h1>Web Development</h1>
            <h3>MPCS 52553 - Winter Quarter 2023</h3>
        </titlebar>
        <main>
            <ul>
                <li><a href="course_lectures/remark.html">Lecture Notes</a></li>
                <li><a href="examples">Labs &amp; In-Class Examples</a></li>
		<li><a href="students">Student Pages</a></li>
	    </ul>
        </main>
    </body>
</html>
```
---

# Web Servers: Apache
> The Apache HTTP Server ("httpd") was launched in 1995 and it has been the most
popular web server on the Internet since April 1996. It has celebrated its 20th
birthday as a project in February 2015. ([httpd.apache.org](https://httpd.apache.org/))

![httpd.pache.org](images/apache.png "Screenshot of httpd.apache.org")
---

# Web Servers: Apache
The web server running at https://uchicagowebdev.com/ is Apache. By default, when it
receives an HTTP request, it looks for files on the local filesystem that match
the URL path and returns them to the web browser.
---

# Web Servers: Python Built-In
We can get a similar effect (though not intended for production) with Python's built-in http module:

`python3 -m http.server`
---

# Serving Static Files
![Diagram: Serving Static HTML over HTTP](images/diagram_http_static.png "Serving Static HTML over HTTP")
---

# Serving Static Files
```
HTTP request comes in
Parse out the PATH
Does that path match a file on the local filesystem?
If yes, read that file and send its contents as the body of a new Response
If no, send a 404 Response
```

![Diagram: Serving Static HTML over HTTP](images/diagram_http_static.png "Serving Static HTML over HTTP")

---

# Server-Side Rendering
![Diagram: Serving Static HTML over HTTP](images/diagram_http_abstraction.png "Serving Static HTML over HTTP")

Importantly, HTTP is the interface between the browser and the server. The 
browser sends its HTTP Requests out, then it gets HTTP Responses back. It has no
insight into how those responses are generated.

---
# Server-Side Rendering
That means that HTTP Responses don't have to just be the contents of pre-existing HTML files.
They can just be the output of an application.

```
HTTP request comes in
Parse out the path, headers, query variables, body, etc
**DO LITERALLY ANYTHING YOU CAN PROGRAM**
Send a new Response
```
---
# Lab: Server-Side Rendering
Copy the `<yourname>.html` file you uploaded to `http://uchicagowebdev.com/students/`
in Week 1 and rename the copy `<yourname>.php`

Add some expressions to be evaluated server-side inside `<?php ?>` tags.
- Use `rand` ([https://www.php.net/rand](https://www.php.net/rand)) to generate
a random number. Refresh the page to see the number change.
- Use `getenv` ([https://www.php.net/getenv](https://www.php.net/getenv)) to get
the value of `HTTP_USER_AGENT` and tell you what browser is visiting the page.

Upload the result again with:
```bash
scp <yourname>.php student@uchicagowebdev.com:/var/www/html/students/
```

The password is pinned in Slack
---

# The LAMP Stack
One very popular thing you might want to do with your program that responds to
HTTP requests is have it interact with a database. And for a long time the most
popular such configuration of these pieces was the
[LAMP](https://en.wikipedia.org/wiki/LAMP_(software_bundle) stack.
![LAMP Stack diagram](images/lamp_architecture.png "LAMP Architecture Diagram")
---

# The LAMP Stack
> Originally popularized from the phrase "Linux, Apache, MySQL, and PHP", the acronym "LAMP" now refers to a generic software stack model. The modularity of a LAMP stack may vary, but this particular software combination has become popular because it is sufficient to host a wide variety of web site frameworks, such as WordPress. The components of the LAMP stack are present in the software repositories of most Linux distributions.

https://en.wikipedia.org/wiki/LAMP_(software_bundle)

![LAMP Stack diagram](images/lamp_architecture.png "LAMP Architecture Diagram")
---

# Act Break
---

# Lab: Working with Form Submissions
When the PHP script is run, it has access to information about the HTTP request that triggered it. See this page for an example:

[http://uchicagowebdev.com/examples/week_3/post_unsafe.php](http://uchicagowebdev.com/examples/week_3/post_unsafe.php)

[code on GitHub](https://github.com/UChicagoWebDev/course_materials/blob/main/examples/week_3/post_unsafe.php)

--

We have to be careful with user input though! Try POSTing:

`<div style="position: absolute;top: 0;left: 0;width: 500;background-color: red;height: 1000;">Hahahaha!</div>`
---

# Lab: Working with Form Submissions
If we are going to include user input in our response, we have to make sure any 
HTML is escaped and can't be interpreted by the browser as HTML. 

Let's try again:

[http://uchicagowebdev.com/examples/week_3/post_safely.php](http://uchicagowebdev.com/examples/week_3/post_safely.php)

`<div style="position: absolute;top: 0;left: 0;width: 500;background-color: red;height: 1000;">Hahahaha!</div>`

--

Line 12 here does the work: 

https://github.com/UChicagoWebDev/course_materials/blob/main/examples/week_3/post_safely.php#L12

---

# Databases

[MySQL (Wikipedia)](https://en.wikipedia.org/wiki/MySQL)

[Introduction to Relational Databases (MariaDB Documentation)](https://mariadb.com/kb/en/introduction-to-relational-databases/)

[A MariaDB Primer](https://mariadb.com/kb/en/a-mariadb-primer/)

![Database Tables](images/tables.png "Visualization of two Database Tables")
---

# Databases: SQLite
[SQLite (Wikipedia)](https://en.wikipedia.org/wiki/SQLite)

`sqlite3`

`.databases`

`.open example_db`

`.tables`

`.schema example_table;`
---

# Databases: Select and Insert
`select * from posts;`

`select * from comments;`

```
insert into books (Title, SeriesID, AuthorID)
VALUES ("Lair of Bones", 2, 2);
```
---

# Databases: JOIN
[SQL Joins](https://www.w3schools.com/sql/sql_join.asp)
---

# Accessing the Database with Python
[Connecting to the Database](https://docs.python.org/3/library/sqlite3.html)
---

# Sanitizing Database Inputs
![Bobby Tables Comic](https://imgs.xkcd.com/comics/exploits_of_a_mom.png "Comic strip of a mom who has named her son with a SQL injection")
.credit[https://xkcd.com/327/]
---

# Sanitizing Database Inputs
[Using Placeholders to construct queries](https://docs.python.org/3/library/sqlite3.html#how-to-use-placeholders-to-bind-values-in-sql-queries)
```python
con = sqlite3.connect("db/my_db.sqlite3")
cur = con.cursor()
cur.execute("CREATE TABLE birthdays(name, year)")
data = {"name": "Alice", "year": 1865}
cur.execute("INSERT INTO birthdays_table VALUES(:name, :year)", data)
```
---

# Lab: DIY SQL Injection
```
cd examples/week_3
python3 -i
```
```python
import sqlite3
con = sqlite3.connect("my_db.sqlite3")
cur = con.cursor()
cur.execute("CREATE TABLE students(name, grade)")
# THIS IS BAD
def unsafe_insert(name, grade):
    cur.execute("insert into students (name, grade) values" +
        "('" + name + "', '" + grade + "')")
    con.commit()
```
---

# Act Break
---

# Exercise 3

[A Web Journal](https://github.com/UChicagoWebDev/web-development-winter-2025-assignments-2-0-assignments/tree/main/3_take-home-weblog)


