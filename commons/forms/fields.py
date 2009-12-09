# vim:fileencoding=utf8
import re
from types import StringType, UnicodeType

from django.forms import RegexField, ValidationError
from django.utils.translation import ugettext_lazy as _

__all__ = (
    'StripRegexField',
    'EmailField',
    'AlphaNumField',
    'NumCharField',
    'FullWidthCharField',
)

RE_EMAIL = re.compile(
    r'^[\w\.\-]+' # account
    r'@(?:[A-Z0-9]+(?:-*[A-Z0-9]+)*\.)+[A-Z]{2,6}$' # domain
    , re.IGNORECASE
)
RE_ALPHA_NUM = re.compile(ur'^[a-zA-Z0-9\-_]*$')
RE_NUM = re.compile(ur'^[0-9]*$')
RE_FULL_WIDTH = re.compile(ur'[一-龠]+|[ぁ-ん]+|[ァ-ヴ]+|[０-９]+')

class StripRegexField(RegexField):
    """
    検証する前にstripする正規表現のフィールド
    """
    def clean(self, value):
        if type(value) in (StringType, UnicodeType):
            value = value.strip()
        return super(StripRegexField, self).clean(value)

class EmailField(StripRegexField):
    default_error_messages = {
        'invalid': _(u'Eメールアドレスの形式が不正です'),
    }

    def __init__(self, *args, **kwargs):
        super(EmailField, self).__init__(RE_EMAIL, *args, **kwargs)

class AlphaNumField(StripRegexField):
    """
    半角英数字と"_","-"のみ許容するフィールド
    """
    default_error_messages = {
        'invalid': _(u'半角英数字で入力してください'),
    }

    def __init__(self, *args, **kwargs):
        super(AlphaNumField, self).__init__(RE_ALPHA_NUM, *args, **kwargs)

class NumCharField(StripRegexField):
    """
    数字のみを許容するフィールド
    """
    default_error_messages = {
        'invalid': _(u'数字で入力してください'),
    }

    def __init__(self, *args, **kwargs):
        super(NumCharField, self).__init__(RE_NUM, *args, **kwargs)

class FullWidthCharField(StripRegexField):
    """
    全角文字のみを許容するフィールド
    """
    default_error_messages = {
        'invalid': _(u'全角文字を入力してください。'),
    }

    def __init__(self, *args, **kwargs):
        super(FullWidthCharField, self).__init__(RE_FULL_WIDTH, *args, **kwargs)
