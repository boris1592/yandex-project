from json import loads

from django.core.exceptions import ValidationError

from .models import Tag


def tag_is_default(tag_name):
    tags = Tag.objects.filter(name=tag_name)
    return tags.exists() and tags.first().is_default


def tags_validator(value):
    tags = map(lambda t: t['value'].lower(), loads(value))
    default_tags = list(filter(tag_is_default, tags))

    if len(default_tags) > 0:
        return

    should_contain = Tag.objects.filter(is_default=True)
    shuld_contain_string = ', '.join(map(lambda t: t.name, should_contain))
    raise ValidationError(
        f'Tags should contain at least one of these: {shuld_contain_string}'
    )
