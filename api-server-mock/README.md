# docker-json-server

[JSON Server](https://github.com/typicode/json-server) provides REST API mocking based on plain JSON.
This is a [docker](https://www.docker.io) image that eases setup.

## Requirement
Docker
Docker-compose(optional)


## Usage
Run just following command.

```bash
$ docker run -d -p 3000:3000 -v your_db.json:/data/db.json iaoiui/json-server
```

By Putting your_db.json in the directory which is same as the root directory of this repository,
You can get same result with docker-compose.

```bash
$ docker-compose up -d
```


The above example exposes the JSON Server REST API on port 3000, so that you can now browse to:

```
http://localhost:3000
```

### JSON source

If you mount a file to `/data/db.json` (as in the above example),
it will automatically be used as the plain JSON data source file.

A sample file could look like this:

```json
{
  "posts": [
    { "id": 1, "body": "foo" },
    { "id": 2, "body": "bar" }
  ],
  "comments": [
    { "id": 1, "body": "baz", "postId": 1 },
    { "id": 2, "body": "qux", "postId": 2 }
  ]
}
```
