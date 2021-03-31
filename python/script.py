from core import TorClient

if __name__ == "__main__":
    #Init client
    client = TorClient()

    # Test ip rotation
    print("Public IP before rotate : ", client.get_public_ip())

    # Rotate client's ip
    client.rotate()

    # Test ip rotation
    print("Public IP after rotate : ", client.get_public_ip())
