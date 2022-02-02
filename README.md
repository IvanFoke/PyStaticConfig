# PyStaticConfig
 Static python class for storing a JSON config file. 
 
 -----
## Description
 `BaseConfig` from `pystaticconfig` is a base class for your config. It creates file with path stored in attribute `_config_location`. Class is static so it doesn't need to be instantiated.   
 Private fields starting with underscore (like `_config_location`) won't be saved in JSON file. Other public attributes will be stored in it. 

## Installation
 Package is uploaded to PyPI. Install it with  
 ```bash
 pip install pystaticconfig
 ```

## Usage
 Inherit from `BaseConfig` for creating your own config. Like this:  
 **config.py**  
 ```python
 from pystaticconfig import BaseConfig
 
 class Config(BaseConfig):
     _config_location = '/path/to/app/config.json'
     attr1 = 'value1'
     attr2 = {'1': 1, '2': 2}
 ```
 **app.py**  
 ```python
 from config import Config
 
 # load from file config.json
 Config.load()
    
 # change values
 Config.attr1 = 'new_value'
    
 # save
 Config.save()
 ```
