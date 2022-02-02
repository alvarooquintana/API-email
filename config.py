from pydantic import BaseSettings


class Settings(BaseSettings):
    user: str 
    password: str
    to_addrs: str
    from_addr: str

settings = Settings(_env_file='.env')