# PDF Auto Organizer

Python automation tool that monitors the Windows Downloads folder and automatically moves newly downloaded PDF files into date-based directories.

## Overview

The project reduces repetitive file organization by continuously watching for new PDF files and sorting them into folders based on the current date.

## Features

- Continuous Downloads-folder monitoring
- PDF-only filtering
- Automatic date-based folder creation
- Automatic file moving
- Delay to allow downloads to finish before moving files
- Basic error handling
- Windows batch launcher included

## Tech Stack

- Python
- Python standard library (`os`, `time`, `shutil`, `datetime`)
- Windows Batch

## Running the Project

Update the source and destination paths in `main.py` if necessary, then run:

```bash
python main.py
```

On Windows, the included batch file can also be used:

```text
start_robo.bat
```

## Use Case

This type of automation is useful in administrative workflows where documents are downloaded frequently and need to be organized automatically for later processing or archiving.

## Author

Developed by **Gustavo Henrique Pires**.
