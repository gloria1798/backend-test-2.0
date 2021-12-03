import logging

from src.shared.app import create_app

logging.getLogger().setLevel(logging.INFO)

app = create_app()

def main(): 
    return app.run()

if __name__ == '__main__':
    main()
