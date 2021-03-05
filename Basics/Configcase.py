from configparser import ConfigParser

# Created object of config parser class
config = ConfigParser()

# TO read data from config file and Path of config file
# config.read("/Users/b0222643/Documents/PythonAutomationAPI/restApi/Basics/Config.cfg")

# # Now I have to make my config file dynamic path. (..) means current directory
config.read("../Inputfile/Config.cfg")

print(config.get("Section1", "username"))
print(config.get("Section1", "Password"))

# Another section

print(config.get("API", "firstapi"))
