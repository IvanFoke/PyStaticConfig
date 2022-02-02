from pystaticconfig import BaseConfig


class Config(BaseConfig):
    _config_location = 'app_config.json'

    login = ""
    password = ""

    params = {"lang": "eng"}


if __name__ == "__main__":
    Config.load()
    
    # use config
    print(Config.params)
    
    # change config
    Config.login = input("Enter login: ")
    Config.password = input("Enter password: ")
    
    # save config
    Config.save()
