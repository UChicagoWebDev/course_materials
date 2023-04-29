class: center, middle

# MPCS 52553: Web Development

## Week 6: Storage, Arguments, and Single Page Applications

---

class: agenda

# What is a Single Page Application (SPA)?

- Static assets in Flask
- Path, Routing and history
- Review: Query Variables
- Review: Fragments
- Cookies
- SessionStorage and LocalStorage
- Lab: Who is Best? A toy single-page application

---

# Watch Party 2: The Single Page Experience

---

# Single Page Applications (SPAs)

> A single-page application (SPA) is a web application or website that interacts
> with the user by dynamically rewriting the current web page with new data from
> the web server, instead of the default method of a web browser loading entire
> new pages. The goal is faster transitions that make the website feel more like
> a native app.
>
> In a SPA, a page refresh never occurs; instead, all necessary HTML,
> JavaScript, and CSS code is either retrieved by the browser with a single page
> load,[1] or the appropriate resources are dynamically loaded and added to the
> page as necessary, usually in response to user actions.

https://en.wikipedia.org/wiki/Single-page_application

## https://flask.palletsprojects.com/en/2.0.x/tutorial/static/

---

# Static Assets in Flask

### From Exercise 5

- [create_room.html](https://github.com/UChicagoWebDev/exercise-5/blob/main/app.py#L80-L91)
- [script.js](https://github.com/UChicagoWebDev/exercise-5/blob/main/templates/index.html#L14)
- [tv.jpeg](https://github.com/UChicagoWebDev/exercise-5/blob/main/templates/index.html#L29)

## https://flask.palletsprojects.com/en/2.2.x/api/#flask.Flask.send_static_file

---

# Path

## https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/What_is_a_URL#path_to_resource

---

# Path, Routing, and History

Look at our example application in `mpa`: 
https://github.com/UChicagoWebDev/course_lectures/tree/main/examples/week_6/mpa

## We have modified it to simulate it being very slow to load:
https://github.com/UChicagoWebDev/course_lectures/blob/main/examples/week_6/mpa/app.py#L10

![](images/mpa_sleep.png)
---

# Path, Routing, and History

`spa` only loads once, then switches between animals instantly with javascript.

But what if we want to be able to link to `/cat`? What if we want `/bear` in our
browser history?

Modify the example app in `spa/` so that the animal we pick as best goes into
our browser history. Make sure that if we load the page with that URL, the
correct animal is identified as best.

---

# Lab: Who is Best?

![](examples/week_6/spa/static/happy_cat.jpeg)
## https://developer.mozilla.org/en-US/docs/Web/API/History_API

---

# Review: Query Parameters
![](images/mdn-url-parameters%40x2.png)
## https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/What_is_a_URL#parameters

---

# Review: Fragments
![](images/mdn-url-anchor%40x2.png)
## https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/What_is_a_URL#anchor

---

# Cookies

A cookie is a small piece of information left on a visitor's computer by a website, via a web browser.

Cookies are used to personalize a user's web experience with a website. It may contain the user's preferences or inputs when accessing that website. A user can customize their web browser to accept, reject, or delete cookies.

Cookies can be set and modified at the server level using the Set-Cookie HTTP header, or with JavaScript using document.cookie.
## https://developer.mozilla.org/en-US/docs/Glossary/Cookie

---

# SessionStorage and LocalStorage

`sessionStorage` maintains a separate storage area for each given origin that's available for the duration of the page session (as long as the browser is open, including page reloads and restores).
- Stores data only for a session, meaning that the data is stored until the browser (or tab) is closed.
- Data is never transferred to the server.
- Storage limit is larger than a cookie (at most 5MB).
`localStorage` does the same thing, but persists even when the browser is closed and reopened.
- Stores data with no expiration date, and gets cleared only through JavaScript, or clearing the Browser cache / Locally Stored Data.
- Storage limit is the maximum amongst the two.

## https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API

---

# Watch Party 2

## The Single Page Experience

https://github.com/UChicagoWebDev/exercise_6