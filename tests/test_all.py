"""
    Test all apisender
"""

from apisender import Apisender


def test_all():
    """
        Test all apisender
    """
    fromname = "fromname"
    fromid = "from@test.com"
    subject = "test subject"
    toid = "to@test.com"
    toname = "toname"
    bodytext = "test text"
    bodyhtml = "<h1>test html</h1>"
    subject = "test subject"

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
