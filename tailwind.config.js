module.exports = {
  purge: [
      './assets/js/*.js',
      './assets/js/**/*.js',
      './templates/*.html',
      './templates/**/*.html',
  ],
  theme: {
    extend: {
      maxWidth: {
        '1/3': '33.333333%'
      }
    },
  },
  variants: {},
  plugins: [],
}
