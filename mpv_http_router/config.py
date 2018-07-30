
import configpp.tree
import configpp.soil

tree = configpp.tree.Tree()

from typing import List

StringList = List[str]

@tree.root()
class Config(object):

    mpv_socket_pattern: str

    logger: dict


def load() -> Config:
    config_loader = configpp.soil.Config('mpv-http-router.yaml', configpp.soil.YamlTransform())

    if not config_loader.load():
        return None

    return tree.load(config_loader.data)
