import sys

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    print("Please install python-dotenv (pip install python-dotenv).")
    print("Then create .env file inside root project folder (like .gitignore),")
    print("Add line `BOT_TOKEN=<token from @botfather>` to .env")

from .main import main


if __name__ == "__main__":
    sys.exit(main())
