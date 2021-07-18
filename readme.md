# tick

Allow for interactions with TickSpot through Python currently the goals are to be able to automatically create entries in TickSpot via a cronjob.

## Installation
To install you will need to clone the github repository. Currently it does not support pip.


```bash
git clone https://github.com/andrewbeattie/tick.git
```
You will need to add the folder to your system paths as well.

## Usage

![](https://i.imgur.com/aapxUnH.png)

1. Use list project to get the project id
2. Use the project id to use list task to get the appropriate task id
3. Create an entry with a project id and task id.

## License
[MIT](https://choosealicense.com/licenses/mit)