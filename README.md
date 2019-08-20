# Morph analyzer for Russian language

Simple HTTP wrapper around [pymorphy2](https://github.com/kmike/pymorphy2).

Sample request: `http://localhost:8080/parse/мышь`

Sample response:
```
{
  "status": "ok",
  "word": "мышь",
  "result": [
    {
      "normal-form": "мышь",
      "tag": {
        "grammemes": [
          "sing",
          "anim",
          "NOUN",
          "accs",
          "femn"
        ]
      },
      "score": 0.666666
    },
    {
      "normal-form": "мышь",
      "tag": {
        "grammemes": [
          "sing",
          "nomn",
          "anim",
          "NOUN",
          "femn"
        ]
      },
      "score": 0.333333
    }
  ]
}
```
