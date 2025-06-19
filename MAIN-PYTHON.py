# Chinese-id-
# -*- coding: utf-8 -*-
import sys
import os

# Ensure Windows terminal uses UTF-8 encoding
if os.name == 'nt':
    os.system('chcp 65001')
# Make sure He Knows Thi Is In English
print("=======================")
print("       WARNING")
print("=======================")
print("Everything in this program will appear in English")
print("due to possible character encoding (UTF-8) issues.")
print()
print("This ID is NOT official and is only for fun/testing.")
print()
print("DO NOT enter sensitive or real information.")
print("You are on the open internet.")
print("=======================")
print()
print("=======================")
# Collect user input
full_name = input("What is your full name? ")
gender = input("What is your Gender? ")
ethnicity = input("What is your ethnic group? ")
date_of_birth = input("What is your date of birth (DD/MM/YYYY)? ")
domicile = input("What is your residence? ")
id_number = input("Enter ID number (18 digits): ")
City_Police = input("City Police that is isuring this: ")

# Format output neatly (truncate if too long)
def format_field(value, length):
    return value[:length].ljust(length)

print("\n")
print("+---------------------------------------------------+")
print("|            CHINA RESIDENT IDENTITY CARD           |")
print("+---------------------------------------------------+")
print(f"| Name: {full_name.ljust(20)} Gender: {gender.ljust(6)} Ethnicity: {ethnicity.ljust(10)} |")
print(f"| DOB: {date_of_birth.ljust(10)}{'':33} |")
print(f"| Address: {domicile.ljust(45)} |")
print(f"| ID Number: {id_number.ljust(25)} |")

print("+---------------------------------------------------+")
print("| Issued by: " + City_Police + "       Issue Date: 01/01/2025 |")
print("| Valid: 2025.01.01 - 2035.01.01                     |")
print("+---------------------------------------------------+")

