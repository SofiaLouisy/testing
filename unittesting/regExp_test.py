import re

EMAIL_REGEXP = r'[\S.]+@[\S.]+'

def test_email_regexp():
    assert re.match(EMAIL_REGEXP,'test@nowhere.com')

    assert not re.match(EMAIL_REGEXP, 'test@')