# Lab 5

## 5-1: Egg Timer

Make a page with a text entry field and a button called 'Set Timer'. When a user
puts a number in the field and clicks the button, wait that many seconds then
log "Ding!" to the console. Make sure you let users set multiple timers at once,
giving them unique IDs. So:

```javascript
console.log(`Timer ${id}: Ding!`)
```

## 5-2: Sequential Asynchronous Functions:

Condsider 3 functions, `fnA`, `fnB`, and `fnC`. Each takes between 1 and 5 
seconds to run. Write code that will run them in sequence in the shortest 
possible time.

## 5-3: Random Concept Walk

Write a page with a text entry field and a search button. Run the query through 
our related searches API. Pick a random response and run that through the API. 
Repeat three more times, for a related searches chain that's five items long, 
including the original query. Log the results to the console. Hint: You may want 
to use javascript's Fetch method, which sends AJAX requests and returns Promises 
natively.

## 5-4 Random Concept Walk with Async

Repeat 5-3, this time with the `async` keyword. Can we update it to take a 
variable number of steps on our walk?