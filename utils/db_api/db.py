import asyncpg


class DBComm:
    async def db_edit_text(text):
        conn = await asyncpg.connect(host='92.53.105.234', database='texts', user='personnel', password='personnel',
                                     port='5432')
        await conn.execute('UPDATE texts SET text = $1 RETURNING id', text)
        await conn.close()

    async def db_get_text():
        conn = await asyncpg.connect(host='92.53.105.234', database='texts', user='personnel', password='personnel',
                                     port='5432')
        text = await conn.fetchrow('SELECT text FROM texts')
        text = text['text']
        await conn.close()
        return text

    async def db_edit_time(time):
        conn = await asyncpg.connect(host='92.53.105.234', database='texts', user='personnel', password='personnel',
                                     port='5432')
        await conn.execute('UPDATE texts SET time = $1', time)
        await conn.close()

    async def db_get_time():
        conn = await asyncpg.connect(host='92.53.105.234', database='texts', user='personnel', password='personnel',
                                     port='5432')
        time = await conn.fetchrow('SELECT time FROM texts')
        time = time['time']
        await conn.close()
        return time
