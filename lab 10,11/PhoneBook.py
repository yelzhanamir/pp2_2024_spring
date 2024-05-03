import psycopg2
from config import load_config

def insert_contact(username, phone):
    """ Вставка нового контакта """
    sql = """INSERT INTO tabletbook(username, phone) VALUES (%s, %s);"""
    try:
        config = load_config()
        conn = psycopg2.connect(**config)
        cur = conn.cursor()
        cur.execute(sql, (username, phone))
        conn.commit()
        print("Contact inserted successfully.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            cur.close()
            conn.close()

def update_contact(user_id, new_username, new_phone):
    """ Обновление контакта """
    sql = """UPDATE tabletbook SET username = %s, phone = %s WHERE id = %s;"""
    try:
        config = load_config()
        conn = psycopg2.connect(**config)
        cur = conn.cursor()
        cur.execute(sql, (new_username, new_phone, user_id))
        conn.commit()
        print("Contact updated successfully.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            cur.close()
            conn.close()

def delete_contact(user_id):
    """ Удаление контакта """
    sql = """DELETE FROM tabletbook WHERE id = %s;"""
    try:
        config = load_config()
        conn = psycopg2.connect(**config)
        cur = conn.cursor()
        cur.execute(sql, (user_id,))
        conn.commit()
        print("Contact deleted successfully.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            cur.close()
            conn.close()

def search_contacts(filter_by, value):
    """ Поиск контактов по фильтрам """
    sql = """SELECT * FROM tabletbook WHERE {} = %s;""".format(filter_by)
    try:
        config = load_config()
        conn = psycopg2.connect(**config)
        cur = conn.cursor()
        cur.execute(sql, (value,))
        rows = cur.fetchall()
        if rows:
            print("Search results:")
            for row in rows:
                print(row)
        else:
            print("No results found.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            cur.close()
            conn.close()

def main():
    while True:
        print("\nOptions:")
        print("1. Insert contact")
        print("2. Update contact")
        print("3. Delete contact")
        print("4. Search contacts")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            phone = input("Enter phone: ")
            insert_contact(username, phone)
        elif choice == "2":
            user_id = input("Enter contact ID: ")
            new_username = input("Enter new username: ")
            new_phone = input("Enter new phone: ")
            update_contact(user_id, new_username, new_phone)
        elif choice == "3":
            user_id = input("Enter contact ID: ")
            delete_contact(user_id)
        elif choice == "4":
            filter_by = input("Enter field for filtering (e.g., 'username'): ")
            value = input("Enter filter value: ")
            search_contacts(filter_by, value)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
