from mocker import Mocker
from mocker import ANY

mocker = Mocker()
postmonkey = mocker.replace("postmonkey")
pm = postmonkey.PostMonkey(ANY)

pm.ping()
mocker.result(u"Everything's Chimpy!")

mocker.replay()

from postmonkey import PostMonkey
mailchimp = PostMonkey('123')
print(mailchimp.ping())
