import requests

class gen():
    def __str__(self) -> dict:
        response = requests.post('https://api.internal.temp-mail.io/api/v3/email/new')
        return {"data":{"email":response.json()["email"],"token":response.json()["token"]},"message":"success"}
# print(gen().__str__())
