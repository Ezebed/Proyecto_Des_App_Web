// npx tailwindcss -i ./recursos/CSS/input.css -o ./recursos/CSS/output.css --watch

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

