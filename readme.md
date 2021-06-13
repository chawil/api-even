[![codecov](https://codecov.io/gh/chawil/api-even/branch/master/graph/badge.svg?token=CSHFDGGO8A)](https://codecov.io/gh/chawil/api-even)

# api-even

API to know if a number is odd or even

## Docker

```bash
# to run container
docker run -p 5000:5000 --rm -d api-even/latest
```

## dev

```bash
# to install nodemon
npm install --global nodemon

# command to "hotreload" the web page when the code changes
nodemon -e py -x python main.py

# -e for extensions
# -x for the command

# to run server
python main.py

# to test
python tests.py

```

## performances notes

- When testing in local, calling http://localhost:5000/ is 300x slower than http://127.0.0.1:5000/ for some DNS resolution problem, not sure why it happens only with flask (no problem with the go front)
