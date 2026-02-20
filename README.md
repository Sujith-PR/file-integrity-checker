Project Page:
https://roadmap.sh/projects/file-integrity-monitor

\# File Integrity Checker



A Python-based File Integrity Monitoring (FIM) tool that detects unauthorized file modifications using SHA-256 hashing.



This project demonstrates core cybersecurity concepts such as hashing, baseline creation, and integrity verification.



------------------------------------------------------------



FEATURES



\- Generate SHA-256 hashes for files

\- Create a baseline database

\- Detect modified files

\- Update stored hashes

\- Ignores internal database file (db.json)

\- Works on Windows (PowerShell compatible)



------------------------------------------------------------



TECHNOLOGIES USED



\- Python 3

\- hashlib (SHA-256)

\- JSON

\- OS \& file system operations



------------------------------------------------------------



INSTALLATION



Make sure Python 3 is installed.



Clone the repository:



git clone https://github.com/Sujith-PR/file-integrity-checker.git

cd file-integrity-checker



------------------------------------------------------------



USAGE



1\) Initialize Baseline



python integrity\_check.py init .



Stores hashes of all files in the directory.



2\) Check File Integrity



python integrity\_check.py check .



Compares current hashes with stored hashes.



Example Output:



.\\integrity\_check.py: Unmodified

.\\test.txt: Modified (Hash mismatch)



3\) Update Stored Hashes



python integrity\_check.py update .



Updates the baseline after intentional changes.



------------------------------------------------------------



HOW IT WORKS



1\. Calculates SHA-256 hash of each file.

2\. Stores hashes in db.json.

3\. During checks, recalculates hashes and compares them with stored values.

4\. Reports any mismatches.



------------------------------------------------------------



PURPOSE



This project was built to understand:



\- File integrity monitoring

\- Hash-based verification

\- Basic cybersecurity defense mechanisms

\- Version control using Git \& GitHub



------------------------------------------------------------



FUTURE IMPROVEMENTS



\- Detect new files

\- Detect deleted files

\- Add logging with timestamps

\- Add colored CLI output

\- Convert into a background monitoring tool



------------------------------------------------------------



AUTHOR



Sujith PR

