import json
from dataclasses import asdict

import requests

from api_objects.user import User
from utils.util import email, name, phone, zip_code, bool_rand


def create_users(meth):
    user_ids = []
    def wrapper(self, count):
        with requests.Session() as req:
            req.headers["accept"] = "*/*"
            req.headers["Content-Type"] = "application/json"
            req.verify = False
            for _ in range(int(count)):
                email_ = email(self)
                name_ = name(self)
                user_req =  User(
                    userId = email_,
                    password = self.default_user_password,
                    contactPersonName = name_,
                    email=email_,
                    phoneNumber=phone(self),
                    contactCity=self.city_ds.random_choice(),
                    imagePath=f"/var/tmp/{name(self)}.jpg",
                    lowName=name(self),
                    lowAddress=self.address_ds.random_choice(),
                    zipCode=zip_code(),
                    requisitesCity=self.city_ds.random_choice(),
                    singleRegId=zip_code(),
                    isTaxesPayer=bool_rand(),
                    taxationId=zip_code(),
                    requisitesContactPersonName=name_
                )

                res = req.post(url=f"https://localhost:8443/api/users/register", json=asdict(user_req))

                if not res.ok:
                    raise RuntimeError(f"User register operation finished with wrong status code: {res.status_code}. Error text: {res.text}\nPayload:{res.request.body}")

                auth_hrader = f"Bearer {res.json()['token']}"

                user_res = req.post("https://localhost:8443/api/users/current_user", headers={"Authorization": auth_hrader})

                if not user_res.ok:
                    raise RuntimeError(f"Current user get operation finished with wrong status code: {user_res.status_code}. Error text: {user_res.text}.\nReq Headers: {user_res.headers}")

                user_ids.append(user_res.json()["userId"])
        if hasattr(self, "user_ids"):
            self.user_ids.clear()

        self.user_ids = user_ids

        return meth(self, count)

    return wrapper