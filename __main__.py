import bottle
from pymorphy2 import MorphAnalyzer

from pymorphy2.analyzer import Parse
from pymorphy2.tagset import OpencorporaTag

morph = MorphAnalyzer()


def _tag_to_dict(tag: OpencorporaTag) -> dict:
    return {
        'grammemes': tuple(tag.grammemes)
    }


def _parsed_to_dict(parsed: Parse) -> dict:
    return {
        'normal-form': parsed.normal_form,
        'tag': _tag_to_dict(parsed.tag),
        'score': parsed.score
    }


@bottle.route('/parse/<word>')
def index(word: str) -> dict:
    return {
        'status': 'ok',
        'word': word,
        'result': [
            _parsed_to_dict(form) for form in morph.parse(word)
        ]
    }


bottle.run(host='localhost', port=8080)
