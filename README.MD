# Pre-requisites
To deploy the application we need next things to be installed:
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)

# Installation
## Build Docker Container
Inside _Project Root_ folder run in the _Terminal_:

```shell
docker compose build
```

## Start Docker Container
Inside _Project Root_ folder run in the _Terminal_:

```shell
docker compose up -d
```

# Create the test data
## Access the UI
In _Web Browser_ navigate to the address: [http://localhost:8501](http://localhost:8501)

## Personalize Test Data Generation
After command is started you should see in ghe browser _Web UI_ like this:

![Test Data Inserter Web UI](img/web_ui.png "Test Data Inserter Web UI")

### Fields meaning
- *MS SQL Backend host* - Database host
- *Host for REST API Service* - *OLX Faked Backend* *REST API* host
- *MS SQL Backend port* - *MS SQL Server* user name
- *REST API service HTTPS port* - *OLX Faked Backend* *REST API* host port
- *Database Name* - *MS SQL Server* user password
- *Database username* - Database to use
- *Database password* - How many users to create
- *How many users to create?* - How mny users to create?
- *How many items per user to create?* - How many *OLX items* create for each *user*
- *Set the defaule user password* - User password set to all created users.
- *Delete all previous inserted test data from the Database?* - Delete all previous data in the *DB*? Available options: *Yes*, *No*. Option is optional. If not set, all previous data will be deleted.

### Start Test Data Insertion

To start the operation, click button *Insert Test Data >>*.
