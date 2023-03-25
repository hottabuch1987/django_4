import asyncio
import httpx


async def get_link(query: str, current_page:int):
    headers = {'Authorization': '5ddba27f0f1454a8314037f756e2b817bfd8eb73cf32c3f6ef77a56ed89faaa8'}
    params = {'query': query, 'par_page': 1, 'page': current_page}
    url = 'https://api.pexels.com/v1/search'

    async with httpx.AsyncClient() as client:
        res = await client.get(url, headers=headers, params=params)
        if res. status_code == 200:
            response = res.json()
            print('current_page', current_page)
            return response.get('photos')[0].get('src').get('original')


async def search_image(query: str, count: int):
    current_page = 0
    images = await asyncio.gather(
        *(get_link(query, count) for count in range(current_page, count)),
        return_exceptions=True
    )
    print(images)
    return images

asyncio.run(search_image('fox', 3))