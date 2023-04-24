from typing import Dict
from functools import partial
import sqlite3

from squirrels import ConnectionSet, QueuePool

# All connections must be shareable across multiple thread. No writes will occur on them
def main(proj: Dict[str, str], *args, **kwargs) -> ConnectionSet:
    weather_db_connector = partial(sqlite3.connect, './database/seattle_weather.db', check_same_thread=False)
    return ConnectionSet({
        'weather_db': QueuePool(weather_db_connector)
    })
