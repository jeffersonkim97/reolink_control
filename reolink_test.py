from reolink_aio.api import Host
import asyncio

async def print_mac_address():
    # initialize the host
    host = Host('192.168.1.245', 'admin', 'tobeor!2b', port=554)
    # connect and obtain/cache device settings and capabilities
    await host.get_host_data()
    # check if it is a camera or an NVR
    print("It is an NVR: %s, number of channels: %s", host.is_nvr, host.num_channels)
    # print mac address
    print(host.mac_address)
    # close the device connection
    await host.logout()

if __name__ == "__main__":
    asyncio.run(print_mac_address())