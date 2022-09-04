import httpx


class HttpClient:
    def __init__(self, base_url: str, **kwargs):
        self.client = httpx.AsyncClient(**kwargs, base_url=base_url)

    async def get(self, url: str, **kwargs):
        res = await self.client.get(url, **kwargs)
        return res.json()

    async def close(self):
        await self.client.aclose()
