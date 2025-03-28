"""
 Example how to set up DAClient.
 DAClient is a singleton pattern for Client from ngsildclient package
 localhost:1026 are the default values for Client
 You can change them
"""
from sd_data_adapter.client import DAClient

from sd_data_adapter.api import is_alive_check

if __name__ == '__main__':
    HOST: str = "localhost"
    PORT: int = 1026
    DAClient.get_instance(HOST, PORT)

    print("Connection is alive:", is_alive_check())