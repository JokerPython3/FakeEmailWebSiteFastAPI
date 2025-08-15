import requests

class inboxs():
    def __str__(self,email) -> dict:
        response = requests.get(
            'https://api.internal.temp-mail.io/api/v3/email/{}/messages'.format(email),
        )
        return{"data":{"inbox":response.json()},"message":"success"}
# print(inboxs().__str__("80a9aj8ng@jxpomup.com"))