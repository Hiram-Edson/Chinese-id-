#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Chinese ID Generator (For Educational Use Only)
WARNING: This is NOT a real ID generator. Do NOT enter sensitive data.
"""

import sys
import os

def setup_encoding():
    """Ensure UTF-8 encoding in Windows terminal."""
    if os.name == 'nt':
        os.system('chcp 65001')

def display_warning():
    """Show a warning message about the program's purpose."""
    print("=======================")
    print("       WARNING")
    print("=======================")
    print("This is a SIMULATED Chinese ID generator for educational purposes.")
    print("DO NOT enter real or sensitive information.")
    print("All output is in English for compatibility.")
    print("=======================\n")

def get_user_input():
    """Collect user input for ID generation."""
    print("Enter the following details (fake data only):")
    full_name = input("Full Name: ")
    gender = input("Gender (Male/Female/Other): ")
    ethnicity = input("Ethnic Group: ")
    date_of_birth = input("Date of Birth (DD/MM/YYYY): ")
    domicile = input("Residence (City/Province): ")
    id_number = input("18-digit ID Number (fake): ")
    issuing_authority = input("Issuing Police Department: ")
    return full_name, gender, ethnicity, date_of_birth, domicile, id_number, issuing_authority

def generate_id_card(full_name, gender, ethnicity, date_of_birth, domicile, id_number, issuing_authority):
    """Format and display the generated ID card."""
    print("\n+---------------------------------------------------+")
    print("|            CHINA RESIDENT IDENTITY CARD           |")
    print("+---------------------------------------------------+")
    print(f"| Name: {full_name.ljust(20)} Gender: {gender.ljust(6)} Ethnicity: {ethnicity.ljust(10)} |")
    print(f"| DOB: {date_of_birth.ljust(10)}{'':33} |")
    print(f"| Address: {domicile.ljust(45)} |")
    print(f"| ID Number: {id_number.ljust(25)} |")
    print("+---------------------------------------------------+")
    print(f"| Issued by: {issuing_authority.ljust(20)} Issue Date: 01/01/2025 |")
    print("| Valid: 2025.01.01 - 2035.01.01                     |")
    print("+---------------------------------------------------+")

def main():
    setup_encoding()
    display_warning()
    user_data = get_user_input()
    generate_id_card(*user_data)

if __name__ == "__main__":
    main()
