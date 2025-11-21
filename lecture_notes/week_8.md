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

# Node.js

Make a file called lookma.js:

```javscript
console.log("Look ma, no broswer")
```

Then let's run it with Node:

`node lookma.js`
---

# Javascript Modules
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules
---

# Type Checking
https://www.typescriptlang.org/docs/handbook/2/basic-types.html
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