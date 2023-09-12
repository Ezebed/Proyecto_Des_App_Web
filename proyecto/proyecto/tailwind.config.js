// npx tailwindcss -i ./static/CSS/input.css -o ./static/CSS/output.css --watch

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./recursos/**/*.js",
],
  theme: {
    extend: {},
  },
  plugins: [],
}

