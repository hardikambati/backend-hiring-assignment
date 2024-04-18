# internal imports
import subprocess

# django imports
from django.contrib.auth import get_user_model


User = get_user_model()
passed, failed = 0, 0
failed_messages = []


def migrate_db() -> None:
    global failed, passed, failed_messages
    try:
        subprocess.run(["python3", "manage.py", "migrate"])
        passed += 1
    except Exception as e:
        failed += 1
        failed_messages.append(str(e))


def create_superuser() -> None:
    global failed, passed, failed_messages
    
    superuser_info = {
        "username": "admin",
        "email": "admin@admin.com",
        "password": "admin",
        "first_name": "admin",
        "last_name": "test"
    }

    try:
        if not User.objects.filter(
                username=superuser_info.get('username')
            ).exists():
            User.objects.create_superuser(
                **superuser_info
            )
        passed += 1
    except Exception as e:
        failed_messages.append(str(e))
        failed += 1


def collect_static() -> None:
    global failed, passed, failed_messages
    try:
        subprocess.run(['python3', 'manage.py', 'collectstatic', '--no-input'])
        passed += 1
    except Exception as e:
        failed_messages.append(str(e))
        failed += 1


def create_sample_user() -> None:

    user_info = {
        "username": "user1",
        "email": "user@1.com",
        "password": "user1",
        "first_name": "user",
        "last_name": "test"
    }

    global failed, passed, failed_messages
    try:
        if not User.objects.filter(
            username=user_info.get('username')
        ).exists():
            User.objects.create(
                **user_info
            )
        passed += 1
    except Exception as e:
        failed_messages.append(str(e))
        failed += 1


def run():
    print("[SETUP] performing setups...")

    migrate_db()
    create_superuser()
    collect_static()
    create_sample_user()

    print("[SETUP] setup completed")
    print(f"[SETUP] {passed} setups passed")
    print(f"[SETUP] {failed} setups failed")

    if len(failed_messages):
        print(f"[SETUP] failed messages array - {failed_messages}")
