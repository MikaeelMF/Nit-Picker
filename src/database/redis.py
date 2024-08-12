from database import r


def set(key: int, value: str) -> bool:
    res = r.set(name=key, value=value)
    if res != True:
        raise RuntimeError('Error while saving to DataBase',
                           res, f'key:{key}', f'value:{value}')
    return res


def get(key) -> str:
    value = r.get(key)
    if value == None:
        raise RuntimeError(f'Key:{key} not found!')
    return value

def save():
    r.bgsave()