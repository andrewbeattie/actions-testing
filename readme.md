# tick

Allow for interactions with TickSpot through Python currently the goals are to be able to automatically create entries in TickSpot via a cronjob.

## Installation
Install directly from GitHub as follows:


```bash
pip install git+https://github.com/andrewbeattie/tick.git
```
You will also need to have a config.yaml file with the following information:
```
tickspot:
  username:
  password:
date:
  country:
  province:
  state:
```
You will need to save this file and create the environment variable "TICKSPOT_CONFIG" pointing towards the config file.

## Usage

![](https://i.imgur.com/aapxUnH.png)

1. Use list project to get the project id
2. Use the project id to use list task to get the appropriate task id
3. Create an entry with a project id and task id.

## License
[MIT](https://choosealicense.com/licenses/mit)