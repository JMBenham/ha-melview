import asyncio
from custom_components.melview.melview import MelViewAuthentication, MelView, MelViewDevice

EMAIL="jmbenham@outlook.com"
PASSWORD="wM267UztBB1HiFAGHMsgQ"

async def main():
    print("Hello from ha-melview!")
    authentication = MelViewAuthentication(email=EMAIL, password=PASSWORD)
    await authentication.async_login()

    melview = MelView(authentication=authentication)
    devices = await melview.async_get_devices_list()

    for device in devices:
        # print(device.get_friendly_name())

        print(await device.async_get_temperature())
        print(await device.async_get_room_temperature())
        
        await device.async_refresh()

        zones = device.get_zones()

        for zone in zones:
            print(zone)

if __name__ == "__main__":
    asyncio.run(main())
