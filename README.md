# SQL Injection (CWE-89) Vulnerability Research & Exploit Validation Lab

[![Cybersecurity Lab](https://img.shields.io/badge/Lab-SQL%20Injection-red)](https://github.com/)
[![Target](https://img.shields.io/badge/Target-DVWA-blue)](https://github.com/)
[![PoC](https://img.shields.io/badge/PoC-Python3-green)](https://github.com/)

An educational security research project and penetration testing lab demonstrating the end-to-end lifecycle of **SQL Injection (CWE-89)**. This repository covers vulnerability identification, database schema enumeration, custom Python Proof-of-Concept (PoC) development, execution evidence, and remediation.

---

## Table of Contents
- [Overview](#-overview)
- [Lab Environment & Architecture](#-lab-environment--architecture)
- [Vulnerability Details (CWE-89)](#-vulnerability-details-cwe-89)
- [Custom Python Exploit PoC](#-custom-python-exploit-poc)
- [Execution & Evidence](#-execution--evidence)
- [Remediation & Mitigation](#-remediation--mitigation)

---

## Overview
- **Target Application:** Damn Vulnerable Web Application (DVWA) / Local Testbed
- **Vulnerability Class:** CWE-89: Improper Neutralization of Special Elements used in an SQL Command (SQL Injection).
- **Attack Vector:** User input concatenated directly into database backend query strings without sanitization or parameterization.

---

## Lab Environment & Architecture
This lab was executed within an **isolated, authorized local security lab** running on Kali Linux via VirtualBox and Docker.

- **Host OS:** Kali Linux (VirtualBox)
- **Database Backend:** MySQL / MariaDB
- **Validation Language:** Python 3 (`requests` / `urllib`)

---

## Vulnerability Details (CWE-89)
SQL Injection occurs when untrusted user input is directly concatenated into a dynamic SQL query. In vulnerable applications (such as DVWA Low Security Mode), input fields lack parameterization, allowing attackers to inject malicious SQL fragments (e.g., `' OR '1'='1`, `UNION SELECT`) to manipulate query logic, bypass authentication, or extract database contents.

---

## Custom Python Exploit PoC
A lightweight Python script (`poc/exploit.py`) was developed to automate session handling, inject payloads into vulnerable parameters, and parse extracted database records.

```python
import urllib.request, urllib.parse, http.cookiejar

base_url = "http://localhost/vulnerabilities/sqli/"
# Automated SQL injection query payload validation...
```
📸 Execution & Evidence
Exploit Execution (Payload Validation)
Database Enumeration / Output
Lab Directory Structure
🛡️ Remediation & Mitigation
To fix SQL Injection vulnerabilities:

Use Prepared Statements (Parameterized Queries): Ensure database drivers treat user input strictly as data, never as executable code.

Use Object-Relational Mapping (ORM): Implement secure ORMs (like Hibernate, Entity Framework, or SQLAlchemy) that automatically parameterize inputs.

Input Validation & Whitelisting: Validate input types, lengths, and formats before processing.

Disclaimer: Conducted exclusively within a localized, authorized, and isolated testing environment for educational and defensive engineering purposes.
