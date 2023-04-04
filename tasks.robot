*** Settings ***
Documentation       Template robot main suite.

Library             RPA.PDF


*** Variables ***
${TESTDATA_DIR} =       D:\\OneDrive - SLK Software Services Pvt Ltd\\Desktop\\PDF files


*** Tasks ***
Merge
    Merge pdfs


*** Keywords ***
Merge pdfs
    ${files}=    Create List
    ...    ${TESTDATA_DIR}${/}newdoc.pdf:1,2-3

    Add Files To Pdf    ${files}    ${TESTDATA_DIR}${/}newdoc3.pdf
