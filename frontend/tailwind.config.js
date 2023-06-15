/** @type {import('tailwindcss').Config} */
export default {
  content: [
      "./src/**/*.{html,ts,svelte}",
      "../backend/templates/*.html",
      "../backend/templates/**/*.html"
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

