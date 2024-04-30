import os


class Mody(object):
    STRONG = os.environ.get(" STRONG", "")

    API_ID = int(os.environ.get("API_ID", 25829176))

    API_HASH = os.environ.get("API_HASH", "160b2bf653ee7dd974bd6d09a7968cd1")
    
    OWNER = int(os.environ.get("OWNER", 6878497585))
