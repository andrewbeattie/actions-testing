# tick

Python scripts to assist with filling out TickSpot using the request module. Information on the project, task and entries can be queried
through simple commands. Entries can also be created with this information. When creating an entry it can
also check to see if the date is a holiday making it easy to implement automation for TickSpot entries.

## Installation
Install directly from GitHub as follows:


```bash
pip install git+https://github.com/andrewbeattie/tick.git
```
You will need to add the following to your environment variables.
```
TICKSPOT_USERNAME
TICKERSPOT_PASSWORD
```
You will need to save this file and create the environment variable "TICKSPOT_CONFIG" pointing towards the config file.

## Usage

![](https://i.imgur.com/aapxUnH.png)

1. Use list project to get the project id
2. Use the project id to use list task to get the appropriate task id
3. Create an entry with a project id and task id.

## License
[MIT](https://choosealicense.com/licenses/mit)
