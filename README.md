# Indent [![Build Status](https://travis-ci.org/okkays/indent.svg?branch=master)](https://travis-ci.org/okkays/indent) [![codecov](https://codecov.io/gh/okkays/indent/branch/master/graph/badge.svg)](https://codecov.io/gh/okkays/indent)

Takes a line of arbitrary text, and greedily applies line breaks and indentation
to it.

For example,

```
curl -s https://dog.ceo/api/breeds/image/random 2>&1 | indent.py
{"message":"https:\/\/images.dog.ceo\/breeds\/boxer\/n02108089_1031.jpg","status":"success"}
```

Becomes:

```
curl -s https://dog.ceo/api/breeds/image/random 2>&1 | indent.py
{
  "message":"https:\/\/images.dog.ceo\/breeds\/entlebucher\/n02108000_2739.jpg",
  "status":"success"
}
```

Braces don't line up, or the formatting's weird?  Not my problem!

```
└─ $ echo "([{,,,)]" | indent.py
(
  [
    {
      ,
      ,
      ,
    )
  ]
```

# Testing

1. Get the deps: `pip install -r requirements-dev.txt`
2. Run the tests, with something like:

```bash
ls | entr -s 'coverage run -m pytest indent_test && coverage report'
```

