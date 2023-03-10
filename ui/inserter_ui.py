import streamlit as st

from db_objects.item_db_object import ItemDbObject
from db_objects.user_db_object import UserDbObject
from utils.db_utils import delete_all
from utils.mssql_connector import MSSQLConnector


class InserterUi:
    def __init__(self):
        st.set_page_config(
            page_title="OLX Faked Test Data Inserter",
            page_icon="🧊",
            layout="wide",
            initial_sidebar_state="expanded"
        )

        st.header("Insert test data for OLX Faked portal")
        with st.container():
            st.subheader("Database Related Data")
            self.host = st.text_input("MS SQL Backend host", value="localhost")
            self.port = st.number_input("MS SQL Backend port", value=1433)
            self.database = st.text_input("Database Name", value="ShopDb")
            self.user = st.text_input("Database username", value="sa")
            self.password = st.text_input("Database password", type="password")

        with st.container():
            st.subheader("Test Data")
            self.users_amount = st.number_input("How many users to create?")
            self.items_per_user = st.number_input("How many items per user to create?")
            self.default_password = st.text_input("Set the defaule user password")
            self.delete_data = st.radio("Delete all previous inserted test data from the Database?", ("Yes", "No"))

        self.insert_data_button = st.button("Insert Test Data >>", on_click=self.perform)
        self.mssql_connector: MSSQLConnector = None

    def validate_input(self):
        fields = {"host": self.host,
                  "port": self.port,
                  "user": self.user,
                  "database": self.database,
                  "password": self.password,
                  "users amount": self.users_amount,
                  "items per user": self.items_per_user}
        failings = []

        for field in fields:
            if not fields[field]:
                failings.append(field)

        if failings:
            st.error(f"""
            Next fields should be filled:
            {', '.join(failings)}
            """,
                     icon="🚨"
                     )

            return False
        return True

    def connect_db(self):
        self.mssql_connector = MSSQLConnector(self.host, self.user, self.password, self.database)

    def perform(self):
        user_ids = list()
        if self.validate_input():
            with st.spinner("Connecting to the Database ..."):
                self.connect_db()

            if self.delete_data:
                with st.spinner("Deleting all previous data"):
                    delete_all(self.mssql_connector)

            with st.spinner("Creating users"):
                try:
                    user_ids = UserDbObject(self.mssql_connector, self.default_password).insert_data(self.users_amount)
                except Exception as e:
                    st.error("User creation error: " + str(e), icon="🚨")
                    raise e

            with st.spinner("Creating items on the portal ..."):
                try:
                    ItemDbObject(self.mssql_connector, user_ids).insert_data(self.items_per_user)
                except Exception as e:
                    st.error("Items creation error: " + str(e), icon="🚨")
                    raise e

            st.info("Test Data inserted successfully!")