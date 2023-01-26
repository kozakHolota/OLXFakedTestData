# Pre-requisites
## Python installation
Install *Python* from the [official page](https://www.python.org/downloads/). Make sure that during the installation *Python* is added to the *PATH* system variable. That *Windows* users will be asked during the installation process.

## Virtual Environment installation
Use *Virtual Environment* only if you use *Python* for the regular development. Miss the instructions related to it otherwise.
In the *Terminal* (**Linux** or **MacOS X**) or *Powershell* (**Windoes OS**) type:

```shell
pip install virtualenv
```

## Install the dependencies

### Create Virtual Environment
If you use *Virtual Environment*, activate it in the *Terminal* (**Linux** or **MacOS X**) or *Powershell* (**Windoes OS**):

```shell
virtualenv my_virtual_environment
```
### Activate Virtual Environment

**Linux or Mac OS X**
```shell
. my_virtual_environment/bin/activate
```

**Windows OS**
```shell
my_virtual_environment\Scripts\activate.PS2
```

### Install the dependencies
Inside the project root type in the *Terminal*:
```shell
pip install -r requirements.txt
```

# Create the test data
## Command execution
To fill the *DB*, Database server must be running. How to activate is, see *README.MD* in [OLXFakedBackend](https://github.com/kozakHolota/OLXFakedBackend) project.

Inside the *Project Root* folder execute command:

```shell
python ./main.py --host=<mssql host> --username=<username> --password=<password> --database=<database> --users=<how many users create> --items_per_user=<how many items create per user> --delete_previous_data=<delete all dynamic data in DB>
```

## Command options
- *--host* - Database host (in most cases *localhost*)
- *--username* - *MS SQL Server* user name
- *--password* - *MS SQL Server* user password
- *--database* - Database to use
- *--users* - How many users to create
- *--items_per_user* - How many *OLX items* create for each *user*
- *--delete_previous_data* - Delete all previous data in the *DB*? Available options: *Yes*, *No*. Option is optional. If not set, all previous data will be deleted.
