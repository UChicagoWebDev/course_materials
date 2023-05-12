## Sample Configuration for React Modules with babel-standalone

This sample project shows how you can divide your React code into multiple
[javascript Modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
without installing the React transpilation toolchain on your development environment.

You'll need to update the `<script>` tag you're using to include babel-standalone,
the library that transforms JSX on the fly for us. Notice that the one in this
updated `index.html` uses the latest build of babel-standalone, instead of being
pegged to version 6 like earlier examples from class:

`<script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>`

Then you'll need to include each script that contains a module in your code as
a `<script>` tag in your `index.html`, and you'll need to put script tags for
dependencies before the scripts that import them. Including `type="text/babel"`,
`data-plugins="transform-modules-umd"`, and ` data-presets="react"` attributes
on your scripts will tell babel-standalone how to decode them, but unfortunately
it can't walk the dependency tree for you and apply the babel transformations to
files at the time they're imported.

So in this example, ModuleDemo is defined in `script.js` and is our root
component that we pass to `React.createElement`. That means it has to be the
last `<script>` tag in our `index.html`. ModuleDemo imports MyModule, defined in
`modile.js`. So the script tag for `module.js` has to appear above the one for
`script.js`. MyModule imports MyChildDependency, defined in `childDependency.js`.
So the `<script>` tag for `childDependency.js` has to appear above both of them
in `index.html`.

If we were building these modules on our development machines with a tool like
webpack, we could let the tool do all the dependency management for us, but here
we're limited to what we can accomplish in the browser. But this does let you
write idiomatic javascript modules, they just have to be included in `index.html`
in a strange way.
