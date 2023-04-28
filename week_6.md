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

# Watch Party 2: The Single Page Experience

---

# Single Page Applications (SPAs)

> A single-page application (SPA) is a web application or website that interacts with the user by dynamically rewriting the current web page with new data from the web server, instead of the default method of a web browser loading entire new pages. The goal is faster transitions that make the website feel more like a native app.
>
> In a SPA, a page refresh never occurs; instead, all necessary HTML, JavaScript, and CSS code is either retrieved by the browser with a single page load,[1] or the appropriate resources are dynamically loaded and added to the page as necessary, usually in response to user actions.

https://en.wikipedia.org/wiki/Single-page_application

## https://flask.palletsprojects.com/en/2.0.x/tutorial/static/

# Static Assets in Flask

### From Exercise 5

- [create_room.html](https://github.com/UChicagoWebDev/exercise-5/blob/main/app.py#L80-L91)
- [script.js](https://github.com/UChicagoWebDev/exercise-5/blob/main/templates/index.html#L14)
- [tv.jpeg](https://github.com/UChicagoWebDev/exercise-5/blob/main/templates/index.html#L29)

## https://flask.palletsprojects.com/en/2.2.x/api/#flask.Flask.send_static_file

# Path

## https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/What_is_a_URL#path_to_resource

# Path, Routing, and History

Look at our example application in `mpa`.

## We're going to modify it to simulate it being very slow to load.

# Path, Routing, and History

`spa` only loads once, then switches between animals instantly with javascript.

But what if we want to be able to link to `/cat`? What if we want `/bear` in
our browser history?

Modify the example app in `spa/` so that the animal we pick as best goes into
our browser history. Make sure that if we load the page with that URL, the
correct animal is identified as best.

# Lab: Who is Best?

## https://developer.mozilla.org/en-US/docs/Web/API/History_API

# Review: Query Parameters

## https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/What_is_a_URL#parameters

# Review: Fragments

## https://developer.mozilla.org/en-US/docs/Learn/Common_questions/Web_mechanics/What_is_a_URL#anchor

# Cookies

## https://developer.mozilla.org/en-US/docs/Glossary/Cookie

# SessionStorage and LocalStorage

## https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API

# Watch Party 2

## The Single Page Experience

https://mit.cs.uchicago.edu/mpcs52553-sum-21/course/tree/master/week_6/exercise_6
