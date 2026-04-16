import time
from src.runtime_engine import get_system_health

print("🚀 Running Health Monitor...\n")

while True:
    data = get_system_health()

    print(f"Score: {data['score']} | Status: {data['category']}")

    if data["alert"]:
        print(data["alert"])

    time.sleep(1)


        