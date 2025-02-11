# Detoxify Rest API docekr image

HTTP API to classify the toxicity of text messages. This was inspired by [detoxify-flask-container](https://github.com/nedix/detoxify-flask-container) with a few changes

* Proper JSON response
* Three models loaded directly `multilingual` `original-small` `original`
* Build fixes I encountered

## Usage

### 1. Start the service

The following command starts the service on port `8080`.

```shell
docker run --pull always --rm --name lhc-detoxify \
    -p 8080:80 \
    remdex/lhc-detoxify:latest
```

### Build from scratch

```shell
docker build  --progress=plain -f Containerfile -t remdex/lhc-detoxify .
```

### 2. Request toxicity information

The following command sends a HTTP request that classifies the toxicity of a text message.

```shell
curl '127.0.0.1:8080?model=original-small&text=foobar'
```

Supported models out of the box

 * 'multilingual'
 * 'original-small'
 * 'original'

<hr>

## Attribution

- [Detoxify] ([License](https://raw.githubusercontent.com/unitaryai/detoxify/master/LICENSE))
- [Flask] ([License](https://raw.githubusercontent.com/pallets/flask/main/LICENSE.txt))

[Detoxify]: https://github.com/unitaryai/detoxify
[Flask]: https://github.com/pallets/flask
