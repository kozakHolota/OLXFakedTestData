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
streamlit run ./main_ui.py
```

## Personalize Test Data Generation
After command is started you should see in ghe browser _Web UI_ like this:

![Test Data Inserter Web UI](img/web_ui.png "Test Data Inserter Web UI")

### Fields meaning
- *MS SQL Backend host* - Database host (in most cases *localhost*)
- *MS SQL Backend port* - *MS SQL Server* user name
- *Database Name* - *MS SQL Server* user password
- *Database username* - Database to use
- *Database password* - How many users to create
- *How many users to create?* - How mny users to create?
- *How many items per user to create?* - How many *OLX items* create for each *user*
- *Set the defaule user password* - User password set to all created users.
- *Delete all previous inserted test data from the Database?* - Delete all previous data in the *DB*? Available options: *Yes*, *No*. Option is optional. If not set, all previous data will be deleted.

### Start Test Data Insertion

To start the operation, click button *Insert Test Data >>*.
