import os

from fastapi import HTTPException


def get_os_secrets(setting):
    try:
        return os.environ[setting]
    except KeyError:
        raise HTTPException(status_code=404)
