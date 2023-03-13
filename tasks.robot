*** Settings ***
Documentation       Template robot main suite.

Library             split.py
Library             RPA.PDF


*** Tasks ***
Minimal task
    Split Pdf    file_name    page_range    output_folder
