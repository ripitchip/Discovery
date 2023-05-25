# coding: utf-8
import subprocess


def main() -> None:
    """Main function.

    Print("Hello, World!")
    """
    #run this command as subprocess uvicorn api:app --host 0.0.0.0 --port 8000                                                                                                                                                                         
    subprocess.run(["uvicorn", "src.API.api:app", "--host", "0.0.0.0", "--port", "8000"])


if __name__ == "__main__":
    main()
