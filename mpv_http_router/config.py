
from configpp.tree import Tree, Settings
from configpp.soil import create_from_url

tree = Tree(Settings(convert_underscores_to_hypens = True))

@tree.root()
class Config():

    port: int
    host = '0.0.0.0'
    mpv_socket_pattern: str
    logger: dict


def load() -> Config:
    config_loader = create_from_url('configpp://mpv-http-router.yaml')

    if not config_loader.load():
        return None

    return tree.load(config_loader.data)
