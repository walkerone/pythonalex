# -*- coding:utf-8 -*-
import configparser
config=configparser.ConfigParser()

config["name"]={
    "one":"three",
    "two":"ls"
}
config["age"]={
    "age1":222,
    "age2":3333
}
with open("config_test.ini","w") as configfile:
    config.write(configfile)

config.read("config_test")
print(config.sections())
print(config["name"]["two"])