# ut2j_toulouse_bikes

## Setup
Create **api_key.py** in root folder with the following line:
* KEY = "*your_api_key*"

**environment.py** in root folder with the following lines:
* SCRIPT_PATH_FOLDER = "*full_path_of_the_folder_of_the_script*"
* LOG_PATH_FOLDER = "*full_path_of_the_folder_to_use_to_store_the_logs*"

and **data.json** in root folder with an empty array:
* [ ]

## How to use it
In order to request data once:
`python3 main.py`

In order to launch the cron job:
`python3 launcher.py`

## Read data
Data get stored in **data.json** and logs under your log folder in **main.log**
