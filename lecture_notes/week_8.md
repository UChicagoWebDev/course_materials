class: center, middle
# MPCS 52553: Web Development
## Week 8: Node, Modules, Typescript, and CORS
---

class: agenda
# Agenda
- ## Node
- ## Javascript Modules
- ## Typescript
- ## CORS
---

# Node.js

For over a decade, Javascript was a kind of ugly duckling of programming languages. 
Global scope and dynamic, weak typing made large applications very frustrating to build,
but you used it because it was the only thing that ran in the browser.

![Giant yellow rubber duck floating in a marina](images/wat-rubber-duck.jpg)
---

# Node.js

If you have ever seen a movie about an ugly duckling, you know that the characters and the audience
fall in love with them. 

.half[![Shrek rubber duck](images/shrek-rubber-duck.avif)]

People who fell in love with Javascript created [Node](https://nodejs.org/), 
which let them run it _outside_ the browser, on their servers from the command line.
---

# Node.js

Why then? Node is made possible by Google's open-source 
[V8](https://en.wikipedia.org/wiki/V8_%28JavaScript_engine%29) open-source Javascript engine. 
Both come out in 2008. It also benefits from 
[ES5](https://en.wikipedia.org/wiki/ECMAScript_version_history) being finalized in 2009.

V8 uses just-in-time compiling to translate Javascript code into native machine operations.
Having a compilation step gives a place to hook in a lot of  tooling that makes development
easier. 

And Javascript running in V8 is _fast_. Node is initially proposed as an alternative
to the Apache web server, which is written in C.
---

# Node.js

Let's jump in and install:
- https://nodejs.org/
- https://en.wikipedia.org/wiki/Node.js
---

# Lab 8-1
https://github.com/UChicagoWebDev/lab-8

Make a file called lookma.js:

```javscript
console.log("Look ma, no broswer")
```

Then let's run it with Node:

`node lookma.js`
---

# Javascript Modules
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules

> JavaScript programs started off pretty small — most of its usage in the early days was to do isolated scripting tasks, providing a bit of interactivity to your web pages where needed, so large scripts were generally not needed. Fast forward a few years and we now have complete applications being run in browsers with a lot of JavaScript, as well as JavaScript being used in other contexts (Node.js, for example). 

...

> Complex projects necessitate a mechanism for splitting JavaScript programs into separate modules that can be imported when needed. Node.js has had this ability for a long time, and there are a number of JavaScript libraries and frameworks that enable module usage (for example, other CommonJS and AMD-based module systems like RequireJS, webpack, and Babel).

Today, all modern browsers have native support for JavaScript modules without requiring them to be transpiled.
---

# Lab 8-2: Modules
https://github.com/UChicagoWebDev/lab-8
---

# Type Checking
https://www.typescriptlang.org/docs/handbook/2/basic-types.html

https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html
---

# Lab 8-3
https://github.com/UChicagoWebDev/lab-8
---

# Exercise 8

## Watch Party 4: Just My Type
https://github.com/UChicagoWebDev/exercise-8
---

# CORS
https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS
---

# CORS in Flask
https://github.com/corydolphin/flask-cors