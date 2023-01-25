import click

from db_objects.item_db_object import ItemDbObject
from db_objects.user_db_object import UserDbObject
from utils.db_utils import delete_all
from utils.mssql_connector import MSSQLConnector


@click.command()
@click.option('--host', help='Host of MS SQL instance on which OLX Faked Backend depends')
@click.option('--username', help='User to log into MS SQL instance on which OLX Faked Backend depends')
@click.option('--password', help='User password to log into MS SQL instance on which OLX Faked Backend depends')
@click.option('--database', help='OLX Faked Backend database')
@click.option('--users', type=click.types.INT, help='users to register')
@click.option('--items_per_user', type=click.types.INT, help='Items per user to register')
@click.option('--delete_previous_data', type=click.Choice(["Yes", "No"], case_sensitive=False), default="Yes",
              help='Delete all previous data in DB? Values available: Yes, No')
def main(host: str, username: str, password: str, database: str, users: int, items_per_user: int,
         delete_previous_data: str):
    mssql_obj = MSSQLConnector(host, username, password, database)
    if delete_previous_data.lower() == "yes":
        delete_all(mssql_obj)

    user_dbo = UserDbObject(mssql_obj)
    items_dbo = ItemDbObject(mssql_obj, users)

    user_dbo.insert_data(users)
    items_dbo.insert_data(items_per_user)


if __name__ == "__main__":
    main()
