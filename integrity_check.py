import os
import sys
import json
import hashlib

DB_FILE = "db.json"


def calculate_hash(file_path):
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception:
        return None


def load_db():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r") as f:
        return json.load(f)


def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)


def get_files(path):
    if os.path.isfile(path):
        if os.path.basename(path) == DB_FILE:
            return []
        return [path]

    elif os.path.isdir(path):
        files = []
        for root, _, filenames in os.walk(path):
            for name in filenames:
                if name == DB_FILE:
                    continue  # Ignore database file
                files.append(os.path.join(root, name))
        return files
    else:
        print("Invalid path.")
        sys.exit(1)


def init(path):
    files = get_files(path)

    if not files:
        print("No valid files found to initialize.")
        return

    db = {}

    for file in files:
        file_hash = calculate_hash(file)
        if file_hash:
            db[file] = file_hash

    save_db(db)
    print("Hashes stored successfully.")


def check(path):
    if not os.path.exists(DB_FILE):
        print("Database not initialized. Run 'init' first.")
        return

    db = load_db()
    files = get_files(path)

    if not files:
        print("No valid files found to check.")
        return

    for file in files:
        current_hash = calculate_hash(file)
        stored_hash = db.get(file)

        if not stored_hash:
            print(f"{file}: Not initialized.")
        elif current_hash != stored_hash:
            print(f"{file}: Modified (Hash mismatch)")
        else:
            print(f"{file}: Unmodified")


def update(path):
    if not os.path.exists(DB_FILE):
        print("Database not initialized. Run 'init' first.")
        return

    db = load_db()
    files = get_files(path)

    if not files:
        print("No valid files found to update.")
        return

    for file in files:
        file_hash = calculate_hash(file)
        if file_hash:
            db[file] = file_hash

    save_db(db)
    print("Hash updated successfully.")


def main():
    if len(sys.argv) < 3:
        print("Usage: python integrity_check.py [init|check|update] <path>")
        sys.exit(1)

    command = sys.argv[1]
    path = sys.argv[2]

    if command == "init":
        init(path)
    elif command == "check":
        check(path)
    elif command == "update":
        update(path)
    else:
        print("Invalid command.")


if __name__ == "__main__":
    main()

# test modification