import asyncio
import streamlit as st

from api.item_api_client import ItemApiClient
from api.user_api_client import UserApiClient

class asyncrange:
    class __asyncrange:
        def __init__(self, *args):
            self.__iter_range = iter(range(*args))

        async def __anext__(self):
            try:
                return next(self.__iter_range)
            except StopIteration as e:
                raise StopAsyncIteration(str(e))

    def __init__(self, *args):
        self.__args = args

    def __aiter__(self):
        return self.__asyncrange(*self.__args)


async def process_data(hostname: str, port: int, user_password: str, how_many_users: int, items_per_user: int, openai_key: str):
    user_client = UserApiClient(hostname, port, openai_key, user_password)
    progress_text = "Test data creation progress. Please wait."
    step = 100 / how_many_users
    users_registered = 0
    items_registered = 0
    errors = 0
    percents = 0
    with st.spinner("Creating the test data. Please wait"):
        async for _ in asyncrange(how_many_users):
            try:
                new_user = await user_client.register()
                users_registered += 1
                st.markdown(f"Registered new user: {new_user['username']}")
                auth_token = await user_client.login(new_user["username"], new_user["password"])
                item_api = ItemApiClient(hostname, port, openai_key, auth_token)

                async for _ in asyncrange(items_per_user):
                    await item_api.add_task(item_api.add_item())
                    items_registered += 1

                await item_api.perform()
            except Exception as ex:
                st.error(str(ex), icon="🚨")
                errors += 1

    st.caption(f':blue[Users registered: {users_registered}] :sunglasses:')
    st.caption(f':blue[Items registered: {items_registered}] :sunglasses:')
    st.caption(f':red[Errors: {errors}]')


def main():
    st.title("Fake OLX test data creation")
    with st.container():
        st.header("Test Data Parameters")
        user_password = st.text_input("Common password for all created users", "")
        how_many_users = st.number_input("How many users to create?", 1)
        items_per_user = st.number_input("How many items per user to create?", 1)

    with st.container():
        st.header("API server data")
        hostname = st.text_input("API Hostname", "olxfakedbackend")
        port = st.number_input("API port", 443)
        openapi_key = st.text_input("Open AI API key", "")

    run_button = st.button("Start generate data")

    if run_button:
        asyncio.run(process_data(hostname, port, user_password, how_many_users, items_per_user, openapi_key))


if __name__ == "__main__":
    main()
