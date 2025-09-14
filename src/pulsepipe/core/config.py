import os

class Config:
    def __init__(self):
        self.sqlite_path = os.getenv("PULSEPIPE_SQLITE_PATH", "pulsepipe.db")
        self.model_backend = os.getenv("PULSEPIPE_MODEL_BACKEND", "lmstudio")
        self.chunk_size = int(os.getenv("PULSEPIPE_CHUNK_SIZE", "512"))
        # Add more config values as needed

    @staticmethod
    def load():
        return Config()
