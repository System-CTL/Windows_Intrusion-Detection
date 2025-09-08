# Windows_Intrusion-Detection

This checklist is intended for rapid triage of a potentially compromised Windows system using only built-in utilities. It follows the guidance of NIST SP 800-61 Revision 2, emphasizing efficient collection of critical information for initial incident response, without introducing external tools that may alter system state. The goal is to quickly identify indicators of compromise, running processes, persistence mechanisms, and system configuration to support early analysis and containment decisions.

# NOTE

The Python script supporting this workflow is still under development and has not yet been fully tested on Windows. However, the PDF checklist has been updated over time and provides a practical guide for quick wins for defenders, emphasizing the use of native Windows utilities to collect critical artifacts.

| What to Check       | Commands                           | Why It Matters                      |
|---------------------|------------------------------------|-------------------------------------|
| Running Processes   | `tasklist`, `Get-Process`          | Detect suspicious or unknown tasks. |
| Network Connections | `netstat -ano`, `Get-NetTCPConnection` | Spot unusual or persistent connections. |
| Scheduled Tasks     | `schtasks /query /fo LIST /v`      | Look for malicious persistence.     |
