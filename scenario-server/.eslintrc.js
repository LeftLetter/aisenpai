module.exports = {
  env: {
    commonjs: true,
    es6: true,
    node: true,
  },
  extends: ['standard', 'plugin:prettier/recommended'],
  globals: {
    Atomics: 'readonly',
    SharedArrayBuffer: 'readonly',
  },
  parserOptions: {
    ecmaVersion: 2018,
  },
  plugins: ['prettier'],
  rules: {
    'prettier/prettier': [
      'error',
      {
        singleQuote: true,
        semi: false,
        arrowParens: 'avoid',
      },
    ],
  },
}
