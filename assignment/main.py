from client import Client


def main():
    # ACSII Art Generated at https://patorjk.com/software/taag
    print("""
  ___ _   _ ___ ___   ___            _   _             _    _       _ _          _
 / __| | | | _ ) __| | _ ) __ _ _ _ | |_(_)_ _  __ _  | |  (_)_ __ (_) |_ ___ __| |
| (__| |_| | _ \\__ \\ | _ \\/ _` | ' \\| / / | ' \\/ _` | | |__| | '  \\| |  _/ -_) _` |
 \\___|\\___/|___/___/ |___/\\__,_|_||_|_\\_\\_|_||_\\__, | |____|_|_|_|_|_|\\__\\___\\__,_|
                                               |___/
        """)
    print("Welcome to CUBS Banking's online services! What can we help you with today?")
    print()

    client = Client()
    client.create_user()


if __name__ == "__main__":
    main()
