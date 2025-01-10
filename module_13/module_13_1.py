import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for x in range(1, 6):
        await asyncio.sleep(power)
        print(f'Силач {name} поднял {x}' )
    print(f'Силач {name} закончил соревнования.')

async def start_tournament(_list):
    tasks = [start_strongman(name, power) for name, power in _list]
    await asyncio.gather(*tasks)

async def main():
    user = [('Pasha', 3),
            ('Denis', 4),
            ('Apollon', 5)
            ]
    await start_tournament(user)

asyncio.run(main())