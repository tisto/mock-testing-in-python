from mock import patch
from mock import MagicMock

@patch('postmonkey.PostMonkey')
def test_mailchimp_ping_method(mock_class):
    mock_class().ping = MagicMock(
        return_value=u"Everything's Chimpy!"
    )

    from postmonkey import PostMonkey
    pm = PostMonkey('123')
    assert pm.ping() == u"Everything's Chimpy!"

test_mailchimp_ping_method()
