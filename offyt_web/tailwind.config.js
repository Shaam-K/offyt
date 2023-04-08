/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: [
    "./offyt_app/**/*.{html,js}",
  ],
  
  theme: {
    debugScreens: {
      position: ['bottom', 'left'],
    },
    extend: {
      fontFamily : {
        kanit: "'Kanit', sans-serif",
        merriwe: "'Merriweather Sans', sans-serif",
        roboto: "'Roboto Mono', monospace"
      }
    },
  },
  plugins: [
    require('tailwindcss-debug-screens'),
  ]
}

