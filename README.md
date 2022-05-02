# API Sender

Sends messages to various APIs for email or discord

[![Pypi](https://github.com/Sumiza/apisender/actions/workflows/python-publish.yml/badge.svg)](https://github.com/Sumiza/apisender/actions/workflows/python-publish.yml)
[![Pylint](https://github.com/Sumiza/apisender/actions/workflows/pylint.yml/badge.svg)](https://github.com/Sumiza/apisender/actions/workflows/pylint.yml)
[![pytest](https://github.com/Sumiza/apisender/actions/workflows/python-package.yml/badge.svg)](https://github.com/Sumiza/apisender/actions/workflows/python-package.yml)
![PyPI](https://img.shields.io/pypi/v/apisender)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/apisender)


``` python
from apisender import Apisender
```
```
Supported APIs:

- Discord
- Mailjet
- SMTP2GO

Todo:
- Mailgun
- Twillo (sms)
- Telnyx (sms)
```
``` python
Examples:

    fromname = "fromname"
    fromid = "from@test.com"
    subject = "test subject"
    toid = "to@test.com"
    toname = "toname"
    bodytext = "test text"
    bodyhtml = "<h1>test html</h1>"

    print(Apisender(fromname=fromname,
                    bodytext=bodytext).discord().text)

    print(Apisender(fromname=fromname,
                    fromid=fromid,
                    toname=toname,
                    toid=toid,
                    subject=subject,
                    bodytext=bodytext,
                    bodyhtml=bodyhtml).mailjet().text)

    print(Apisender(fromid=fromid,
                    toid=toid,
                    subject=subject,
                    bodytext=bodytext).smtp2go().text)
```

```
Notes:
    - No except checks are done for failed sending.
    - Check is done if password file is missing.
    - Requires requests to work.
    - Returns requests responses.
    - apisender.json is where you keep your passwords
```

