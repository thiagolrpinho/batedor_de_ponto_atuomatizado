from dotenv import load_dotenv
import os

load_dotenv()

load_dotenv(verbose=True)

CREDENCIAIS_AHGORA = {
    "matricula": str(os.getenv("CREDENCIAIS_AHGORA_MATRICULA")),
    "senha": str(os.getenv("CREDENCIAIS_AHGORA_SENHA")),
}