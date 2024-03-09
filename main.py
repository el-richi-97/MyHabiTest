from app.habi_properties_query.server import run_server

if __name__ == '__main__':

    try:
        run_server()

    except ValueError:
        print(
            "Server declaration error. Please verify your .env file and try again. If the problem persist, "
            "contact with the developer."
        )

    except Exception as e:
        print(f"An unexpected error was encountered. Details: {e}")
