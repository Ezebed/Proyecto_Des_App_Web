// npx tailwindcss -i ./static/CSS/input.css -o ./static/CSS/output.css --watch

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/**/*.js",
],
  theme: {
    extend: {},
  },
  plugins: [],
}

