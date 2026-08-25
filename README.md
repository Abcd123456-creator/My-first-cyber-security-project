# 🛡️ Advanced Python Password Security Guard

An advanced, enterprise-grade password scanner built in Python. This tool moves beyond simple length checks by integrating live threat intelligence and pattern analysis to defend against modern cyber threats.

## ✨ Advanced Features
- **🌐 Live Threat Intelligence**: Automatically downloads and checks passwords against a real-world hacker blocklist of the top 1,000 most common breached passwords globally.
- **🧠 Pattern Complexity Analysis**: Scans internal password structure for uppercase letters, lowercase letters, numbers, and special symbols using Regular Expressions (`re`).
- **🛡️ NIST-Aligned Rules**: Enforces strict industry-standard rules including a minimum 8-character limit.
- **🔄 Continuous Session Loop**: Runs safely in a continuous test loop so users can analyze multiple credentials in one session.
- **🔌 Offline Fallback**: Features a built-in safety net to keep scanning using an offline database if internet connectivity is lost.

## 🚀 How It Works
1. Run `security_guard.py` in your terminal or Python IDLE.
2. The script establishes a connection to online threat databases to load the latest blocklist.
3. Enter any password to view real-time security telemetry and risk flags.
4. Type `exit` to safely close the program.

## 🛠️ Built With
- **Python 3** (Core Language)
- `urllib.request` (For live threat data fetching)
- `re` (For cryptographic text pattern matching)
