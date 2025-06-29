def send_alert(leaks):
    print("🚨 ALERT: Data leak detected!")
    for item in leaks:
        print(f"- {item}")

