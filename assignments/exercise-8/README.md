# Exercise #8: Watch Party 4: Just My Type

10 points

**DUE: Friday, December 4 by 5:00pm**

### Instructions

Re-implement the Watch Party single page application from Exercises 6 and 7, this time moving your React application and any static assets into `web-ui`.  We're going to break the React componenets for each of our pages into [modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules) and convert each one to [Typescript](https://www.typescriptlang.org/). Copy your Flask application into `/api` update it to only serve API routes.

Install [Node.js](https://nodejs.org/en) if you haven't already. Following the recommendation of the React docs, we are going to use [Vite](https://vite.dev/guide/) as our build tool when adding React to an existing site. We created `/web-ui` with the command `npm create vite@latest web-ui --template react-swc-ts`.

Start the api from inside `/api` with `flask run`, and start the ui dev server from inside `/web-ui` with `npm run dev`

### Rubric
- Implement all the behaviors of Exercise 6
- Update your Flask API to accept Cross-Origin Requests from your web-ui dev server
- Implement top-level routing in App.tsx
- Put styles that apply to the whole app in App.css
- Implement the splash page as Splash.tsx and Splash.css
- Implement the profile page as Profile.tsx and Profile.css
- Implement the login page as Login.tsx and Login.css
- Implement the room page as Room.tsx and Room.css
- Create a Room type that your Room and Splash components expect and convert API responses into instances of that type
- Create a Message type that your Room component expects and convert API responses into instances of that type
