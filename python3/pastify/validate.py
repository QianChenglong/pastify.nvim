from .type import Config


def validate_config(config: Config, logger, filetype: str) -> bool:
    c = config
    opts = c["opts"]

    if filetype not in c["ft"]:
        logger("Not in a filetype configured in config.ft", "WARN")

    if c is None:
        return False

    if opts["apikey"] == "" and opts["save"] == "online":
        logger(
            "You need to get a free API key for online saving, get one at https://api.imgbb.com/",
            "WARN",
        )
        return False

    valid_save = ["local", "local_file", "online"]
    if opts["save"] not in valid_save:
        logger(str(opts["save"]), "WARN")
        return False
    return True
