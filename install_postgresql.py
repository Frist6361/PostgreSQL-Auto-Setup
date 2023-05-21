import subprocess

def install_postgresql():
    try:
        # Check if PostgreSQL is already installed
        postgres_installed = subprocess.run(['dpkg', '-s', 'postgresql'], capture_output=True).returncode == 0

        if postgres_installed:
            # PostgreSQL is already installed
            print('PostgreSQL is already installed.')
            while True:
                print('Select an action:')
                print('1. Create a new database')
                print('2. Show list of databases')
                print('3. Show connection information for PostgreSQL')
                print('4. Start PostgreSQL')
                print('5. Stop PostgreSQL')
                print('0. Exit')
                choice = input('Enter the action number: ')

                if choice == '1':
                    db_name = input('Enter the name of the new database: ')
                    create_database(db_name)
                elif choice == '2':
                    list_databases()
                elif choice == '3':
                    show_connection_data()
                elif choice == '4':
                    start_postgresql()
                elif choice == '5':
                    stop_postgresql()
                elif choice == '0':
                    break
                else:
                    print('Invalid choice. Please try again.')
        else:
            # Install PostgreSQL
            subprocess.run(['apt-get', 'install', 'postgresql', '-y'])  # Use the appropriate command for your system (apt, yum, etc.)
            print('PostgreSQL installed successfully.')

            while True:
                print('Select an action:')
                print('1. Create a new database')
                print('2. Show list of databases')
                print('3. Show connection information for PostgreSQL')
                print('4. Start PostgreSQL')
                print('5. Stop PostgreSQL')
                print('0. Exit')
                choice = input('Enter the action number: ')

                if choice == '1':
                    db_name = input('Enter the name of the new database: ')
                    create_database(db_name)
                elif choice == '2':
                    list_databases()
                elif choice == '3':
                    show_connection_data()
                elif choice == '4':
                    start_postgresql()
                elif choice == '5':
                    stop_postgresql()
                elif choice == '0':
                    break
                else:
                    print('Invalid choice. Please try again.')

    except subprocess.CalledProcessError as e:
        print('Error installing PostgreSQL:', e)

def create_database(db_name):
    try:
        subprocess.run(['sudo', '-u', 'postgres', 'createdb', db_name])
        print()
        print(f'Database {db_name} created successfully.')
        print()
    except subprocess.CalledProcessError as e:
        print(f'Error creating database {db_name}:', e)

def list_databases():
    try:
        subprocess.run(['sudo', '-u', 'postgres', 'psql', '--dbname=postgres', '-c', '\l'])
    except subprocess.CalledProcessError as e:
        print('Error getting the list of databases:', e)

def show_connection_data():
    print()
    print('You can connect to PostgreSQL using the following information:')
    print('Host: localhost')
    print('Port: 5432')  # Assuming the PostgreSQL port is 5432
    print('Username: postgres')
    print('Password: 0000')
    print()

def start_postgresql():
    try:
        subprocess.run(['service', 'postgresql', 'start'])  # Use the appropriate command for your system
        print()
        print('PostgreSQL started.')
        print()
    except subprocess.CalledProcessError as e:
        print('Error starting PostgreSQL:', e)

def stop_postgresql():
    try:
        subprocess.run(['service', 'postgresql', 'stop'])  # Use the appropriate command for your system
        print()
        print('PostgreSQL stopped.')
        print()
    except subprocess.CalledProcessError as e:
        print('Error stopping PostgreSQL:', e)

if __name__ == '__main__':
    install_postgresql()
