import os
import random
from collections import defaultdict
from datetime import datetime, timedelta

# === Step 1: Simulate Distributed Log Files ===

def generate_user_logs():
    print("📁 Generating logs for multiple users...\n")
    users = ['user1.log', 'user2.log', 'user3.log']
    start_time = datetime.now()
    normal_ips = ["192.168.1.10", "192.168.1.20", "192.168.1.30"]
    attacker_ip = "192.168.1.99"
    resources = ["/index", "/login", "/data", "/dashboard"]
    
    for filename in users:
        lines = []
        curr_time = start_time

        for i in range(30):
            if i < 10 and filename == 'user2.log':  # simulate attack from user2
                ip = attacker_ip
                curr_time += timedelta(milliseconds=500)
            else:
                ip = random.choice(normal_ips)
                curr_time += timedelta(seconds=random.randint(1, 3))

            resource = random.choice(resources)
            timestamp = curr_time.strftime("%Y-%m-%d %H:%M:%S")
            line = f"[{timestamp}] IP:{ip} requested {resource}"
            lines.append(line)

        with open(filename, "w") as f:
            for line in lines:
                f.write(line + "\n")

    print("✅ Logs generated: user1.log, user2.log, user3.log\n")

# === Step 2: Analyze Logs for Intrusions ===

def analyze_logs():
    print("🕵  Analyzing logs for intrusion patterns...\n")
    log_files = ["user1.log", "user2.log", "user3.log"]
    ip_requests = defaultdict(list)
    time_window = 5  # seconds
    request_threshold = 5

    def parse_line(line):
        try:
            time_str = line.split("]")[0].strip("[")
            ip = line.split("IP:")[1].split()[0]
            timestamp = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
            return ip, timestamp
        except:
            return None, None

    # Read all user logs
    for logfile in log_files:
        with open(logfile, "r") as f:
            for line in f:
                ip, timestamp = parse_line(line)
                if ip and timestamp:
                    ip_requests[ip].append(timestamp)

    # Analyze IP patterns
    print("=== Intrusion Detection Report ===")
    alert_triggered = False
    for ip, timestamps in ip_requests.items():
        timestamps.sort()
        for i in range(len(timestamps)):
            count = 1
            window_start = timestamps[i]
            for j in range(i+1, len(timestamps)):
                if (timestamps[j] - window_start).seconds <= time_window:
                    count += 1
                else:
                    break
            if count >= request_threshold:
                print(f"🚨 Intrusion attempt from IP: {ip} — {count} requests in {time_window} seconds")
                alert_triggered = True
                break
    if not alert_triggered:
        print("✅ No suspicious activity detected.")
    print("=== End of Report ===")

# === Main ===

generate_user_logs()
analyze_logs()
