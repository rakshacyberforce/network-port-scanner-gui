🔍 Network Port Scanner GUI



A lightweight and efficient TCP Port Scanner with a graphical user interface (GUI) built using Python and Tkinter.

This tool helps in identifying open ports on a target system for basic network analysis and cybersecurity learning.



---



 👨‍💻 Author



Kunj Patel





---



 🚀 Features



\* ✅ Simple and user-friendly GUI

\* ⚡ Multi-threaded fast port scanning

\* 🔍 Service detection (HTTP, SSH, FTP, etc.)

\* 📊 Real-time scanning results

\* ⏹️ Stop scan anytime

\* 💾 Save results to `.txt` file

\* 🖥️ Cross-platform (Windows, Linux, macOS)



---



🧠 How It Works



1\. User enters a \*\*target IP or hostname\*\*

2\. Defines a \*\*range of ports\*\*

3\. The tool sends connection requests to each port

4\. If connection is successful → port is \*\*OPEN\*\*

5\. Displays results with detected service names



---



 🛠️ Technologies Used



\* Python 3

\* Tkinter (GUI)

\* Socket Programming

\* Multithreading



---



 📦 Installation





git clone https://github.com/rakshacyberforce/network-port-scanner-gui.git

cd network-port-scanner-gui





---



 ▶️ Usage





python scanner\_gui.py





Steps:



1\. Enter target (e.g. `127.0.0.1` or `scanme.nmap.org`)

2\. Enter start port (default: 1)

3\. Enter end port (default: 1024)

4\. Click \*\*Start Scan\*\*

5\. View open ports in real-time

6\. Click \*\*Stop\*\* to cancel scan

7\. Click \*\*Save Results\*\* to export output



---



 🔍 Common Ports Detected



| Port | Service  |

| ---- | -------- |

| 21   | FTP      |

| 22   | SSH      |

| 80   | HTTP     |

| 443  | HTTPS    |

| 3306 | MySQL    |

| 3389 | RDP      |

| 8080 | HTTP-Alt |



---



 🧪 Testing



You can safely test using:



\* `127.0.0.1` (Localhost)

\* `scanme.nmap.org` (Official test server)



---



 📁 Project Structure




network-port-scanner-gui/

│

├── scanner\_gui.py   # Main application

└── README.md        # Project documentation





---



⚠️ Disclaimer



This tool is developed for \*\*educational purposes only\*\*.

Do not use it on unauthorized systems.

The author is not responsible for any misuse.



---



⭐ Future Improvements



\* Dark mode GUI

\* OS detection

\* Advanced scanning techniques

\* Export in CSV/JSON

\* Integration with Nmap



---



 🙌 Acknowledgment



This project is created as part of learning \*\*Cybersecurity and Networking concepts\*\*.



