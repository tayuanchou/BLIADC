/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./homepage/templates/**/*.html", "./static/**/*.js"],
  theme: {
    extend: {
      colors: {
        blanchedalmond: "#FFEBCD",
        customRed: "#781f2c",
        textPink: "#c43147",
      },
    },
  },
  plugins: [],
};
