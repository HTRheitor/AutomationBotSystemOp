# Accounting Entry Automation Bot

A Python automation solution that streamlines the process of entering accounting data from Excel spreadsheets into accounting systems.

## 📋 Project Overview

This project demonstrates how to automate repetitive data entry tasks using Python. The bot reads data from an Excel spreadsheet and automatically inputs it into a form-based system, eliminating the need for manual entry.

![Captura de tela 2025-03-19 223744](https://github.com/user-attachments/assets/dc33c552-104d-4625-8a2f-af77833cb2ed)


## 🔍 The Problem

Many accounting professionals spend hours manually entering data into legacy systems with no API or integration capabilities. This project addresses that challenge by:

- Automating repetitive data entry tasks
- Reducing human error in the process
- Freeing up valuable time for more strategic activities
- Providing a reliable, consistent entry process

## 💡 Solution

The solution consists of:

1. A Python script that reads data from an Excel spreadsheet
2. Automation using PyAutoGUI to control mouse and keyboard actions 
3. A demo system application built with PySimpleGUI to showcase the functionality

## 🛠️ Technologies Used

- **Python**: Core programming language
- **PyAutoGUI**: For controlling mouse and keyboard inputs
- **OpenPyXL**: For reading Excel spreadsheet data
- **PySimpleGUI**: For the demonstration application interface
- **Subprocess**: For system integration and running parallel processes

## 📁 Project Structure

```
.
├── app.py                 # Main application that performs the automation
├── System_app.py          # Demo system application for demonstration purposes
├── vendas_de_produtos.xlsx # Sample data spreadsheet
└── README.md              # Documentation
```

## 🚀 How It Works

1. The bot loads data from an Excel spreadsheet
2. For each row in the spreadsheet, it:
   - Locates the appropriate field in the system
   - Enters the data 
   - Submits the form
   - Confirms the entry
3. This process repeats until all data has been entered

## 📋 Usage

### Prerequisites

- Python 3.6 or higher
- Required libraries:
  - pyautogui
  - openpyxl
  - PySimpleGUI
  
### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/accounting-automation-bot.git
cd accounting-automation-bot

# Install required packages
pip install pyautogui openpyxl PySimpleGUI
```

### Running the Demo

```bash
# Run the main application
python app.py
```

**Note**: The coordinates in the automation script are set for the demo application. For actual implementation with a different system, you'll need to adjust the coordinates to match your specific application's UI.

## ⚠️ Important Notes

- This repository contains a demonstration version with fictitious data
- The demo system (System_app.py) simulates a real accounting system for demonstration purposes
- In a real implementation, you would need to:
  - Adjust the coordinate positions to match your specific application
  - Potentially add error handling and recovery mechanisms
  - Set up a proper logging system

## 🔄 Customization

To adapt this solution to your specific system:

1. Update the Excel file path in `app.py`
2. Modify the click coordinates to match your system's UI
3. Adjust field navigation and data entry logic as needed
4. Add additional error handling as required for your environment

## 📄 License
6HTR66. This is a demonstration version project. All rights reserved.


**Note**: This project demonstrates automation capabilities for educational purposes.
