/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        background: '#1a1a1a',
        primary: '#fc4c02',
        'primary-dark': '#e44400',
      },
    },
  },
  plugins: [],
} 