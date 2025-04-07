class ConfigConstants:
    # Prevent instantiation


    def __new__(cls):
        raise TypeError("This class is for constants only and cannot be instantiated.")

    # Section names
    DATASOURCE = "datasource"

    # Keys inside "datasource"
    DB_URL = "url"
    DB_MAX_POOL = "maxPool"
    DB_POOL_RECYCLE = "poolRecycle"
    DB_POOL_PRE_PING = "poolPrePing"
    DB_MAX_OVERFLOW = "maxOverflow"
    DB_POOL_TIMEOUT = "poolTimeout"
