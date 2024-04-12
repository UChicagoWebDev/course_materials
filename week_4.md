uchicagowebdevclass: center, middle

# MPCS 52553: Web Development
## Week 4: Javascript and REST APIs
---

class: agenda

# Why We Javascript

# Classical Javascript
- `<script>` tags
- `console.log`, `alert`, event handlers

# DOM Manipulation
- selectors, modifying attributes
- adding and removing nodes

# ES6
- "wats"
- `const` and `let`

# AJAX and REST APIs
---

# Why We Javascript

## "Competition is a click away."
[Google Response to Antitrust Concerns, 2009 (NYT)](https://www.nytimes.com/2009/06/29/technology/companies/29google.html)


---
# Why We Javascript

> The basic advice regarding response times has been about the same for [fifty]
years
<footer><cite>Miller 1968; Card et al. 1991<cite></footer>

.big[**0.1 second**] is about the limit for having the user feel that the system is
**reacting instantaneously**, meaning that no special feedback is necessary
except to display the result.

.big[**1.0 second**] is about the limit for the **user's flow of thought** to stay
uninterrupted, even though the user will notice the delay. Normally, no special
feedback is necessary during delays of more than 0.1 but less than 1.0 second,
but the user does lose the feeling of operating directly on the data.

.big[**10 seconds**] is about the limit for **keeping the user's attention** focused
on the dialogue. For longer delays, users will want to perform other tasks while
waiting for the computer to finish, so they should be given feedback indicating
when the computer expects to be done. Feedback during the delay is especially
important if the response time is likely to be highly variable, since users will
then not know what to expect.

[Response Times: The 3 Important Limits (Nielsen Norman Group)](https://www.nngroup.com/articles/response-times-3-important-limits/)

---

# Why We Javascript

###It is very hard to get HTTP responses back in less than 100 ms.

So if you're doing everything right, you get 1 request that you can send out and
back without interrupting the user's flow. And if you have to reload the whole
page, with all its HTML, CSS, and images, forget about it. You'll easily be
spending hundreds or thousands of milliseconds.
---

# Why We Javascript

> Netscape quickly realized that the Web needed to become more dynamic. Even if
you simply wanted to check that users entered correct values in a form, you
needed to send the data to the server in order to give feedback.
<footer>Speaking JS <cite>O'Reilly Media, http://speakingjs.com/es5/ch04.html</cite></footer>

---

# Classical Javascript

## [Script Elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script#Examples)
- External file or inline
- Can go in head or body
- Evaluated immediately
- Global scope
---

# Classical Javascript

## [HTML Event Handlers](https://developer.mozilla.org/en-US/docs/Web/Guide/Events/Event_handlers#HTML_onevent_attributes)
- onclick
- onkeypress
- onfocus

## Examples
- [Alert Example](http://uchicagowebdev.com/examples/week_4/alert.html)
- [Console Log Example](http://uchicagowebdev.com/examples/week_4/console.html)
---

# Lab: Logging events to the Console

```
<script>
var i =0;

function increment() {
  i = i+1;
  console.log(i);
}
</script>
```
---

# DOM Manipulation

### [DOM Element API](https://developer.mozilla.org/en-US/docs/Web/API/Element)
- [querySelector](https://developer.mozilla.org/en-US/docs/Web/API/Element/querySelector)
- [addEventListener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener)
- [setAttribute](https://developer.mozilla.org/en-US/docs/Web/API/Element/setAttribute)
---

# Lab: Buttons to change the styling of a `<div>`

[dommanipulation.html](https://uchicagowebdev.com/examples/week_4/dommanipulation.html)
```
<div id="testing_ground">Watch me change colors!</div>

<input type="button" onclick="recolor('testing_ground')" value="Colorize!"></input>

<script>
function recolor(id) {
  var e = document.body.querySelector("#"+id);
  e.setAttribute("style","color: red");
}
</script>
```
---

# DOM Manipulation

### [DOM Element API](https://developer.mozilla.org/en-US/docs/Web/API/Element)
- [children](https://developer.mozilla.org/en-US/docs/Web/API/ParentNode/children)
  - [prepend](https://developer.mozilla.org/en-US/docs/Web/API/ParentNode/prepend)
  - [append](https://developer.mozilla.org/en-US/docs/Web/API/ParentNode/append)
  - [replaceWith](https://developer.mozilla.org/en-US/docs/Web/API/ChildNode/replaceWith)
- [cloneNode](https://developer.mozilla.org/en-US/docs/Web/API/Node/cloneNode)
- [document.createElement](https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement)
---

# Lab: Buttons to add new `<li>`s to a List
[dommanipulation.html](https://uchicagowebdev.com/examples/week_4/dommanipulation.html)
---

# ES6

### [Wat - A lightning talk by Gary Bernhardt from CodeMash 2012](https://www.destroyallsoftware.com/talks/wat)
(start at 1:20)

### [The WATs of Javascript](https://loomcom.com/blog/0097_the_wats_of_javascript.html)
Good explanation why the above weird behaviors happen.

### [Javascript Quirks and Elegant Features](http://speakingjs.com/es5/ch03.html)
---

# ES6

### ECMAScript Versions
1. June 1997
2. June 1998
3. December 1999
4. *Abandoned*
5. December **2009**
6. June **2015**

[ECMAScript Versions (Wikipedia)](https://en.wikipedia.org/wiki/ECMAScript#Versions)
---

# ES6 New Features

- [`let` and `const`](https://hacks.mozilla.org/2015/07/es6-in-depth-let-and-const/)
- [arrow functions](https://hacks.mozilla.org/2015/06/es6-in-depth-arrow-functions/)
- New methods on [Arrays](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
- [Maps](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
  and [Sets](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)
- Promises (for next week)

---

# AJAX and REST APIs

### [Using XMLHttpRequest](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/Using_XMLHttpRequest)

### [JSON](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)

---

# Lab: Exercise 4

https://uchicagowebdev.com/examples/exercise_4/

[Exercise 4 on Canvas](https://canvas.uchicago.edu/courses/57047/assignments/657292)

[Exercise 4 on GitHub Classroom](https://classroom.github.com/a/qmUxZhJ3)
