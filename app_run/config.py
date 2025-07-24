import configparser
from pathlib import Path

DEFAULT_CONFIG = {"DEFAULT": {"output_dir": "output", "max_retries": "3"}}


def load_config():
    config = configparser.ConfigParser()
    config.read_dict(DEFAULT_CONFIG)

    # 加载系统级配置
    system_config = Path("/etc/CUA/config.ini")
    if system_config.exists():
        config.read(system_config)

    # 加载用户级配置
    user_config = Path.home() / ".config" / "CUA" / "config.ini"
    if user_config.exists():
        config.read(user_config)

    # 加载项目级配置
    local_config = Path("CUA.ini")
    if local_config.exists():
        config.read(local_config)

    return config
