import time
import random
import requests


API_URL = "http://robotops-api:5000"

robots = [
    "R-001",
    "R-002",
    "R-003",
    "R-004",
    "R-005"
]


def send_telemetry(robot_code):

    battery = random.randint(40, 100)

    locations = [
        "Zone A",
        "Zone B",
        "Zone C",
        "Zone D"
    ]

    location = random.choice(locations)

    status = random.choice([
        "working",
        "available",
        "charging"
    ])

    data = {
        "robot_code": robot_code,
        "battery": battery,
        "location": location,
        "status": status
    }

    response = requests.post(
        f"{API_URL}/telemetry",
        json=data
    )

    print(
        f"{robot_code} → "
        f"{status} | "
        f"{battery}% | "
        f"{location} | "
        f"Telemetry API {response.status_code}"
    )


def check_assignment(robot_code):

    response = requests.get(
        f"{API_URL}/robots/{robot_code}/assignment"
    )

    assignment = response.json()

    if "task_name" in assignment:

        print(
            f"{robot_code} ← Assignment: "
            f"{assignment['task_name']} "
            f"({assignment['status']})"
        )

    else:

        print(
            f"{robot_code} ← No assignment"
        )


while True:

    for robot in robots:

        send_telemetry(robot)

        check_assignment(robot)

    print("-" * 60)

    time.sleep(5)
