*** Settings ***
Library     SeleniumLibrary
Library     ../AppLibrary.py
Resource    resource.robot


*** Keywords ***
Add Note And Verify
    [Arguments]    ${author}    ${title}    ${bib_category}    ${bib_citekey}    ${year}    ${doi}
    Add New Note    ${author}    ${title}    ${bib_category}    ${bib_citekey}    ${year}    ${doi}
    Main Page Should Be Open
    Verify Succesful Addition    ${author}    ${title}    ${bib_category}    ${bib_citekey}    ${year}    ${doi}

Add New Note
    [Arguments]    ${author}    ${title}    ${bib_category}    ${bib_citekey}    ${year}    ${doi}
    Main Page Should Be Open
    Click Link    add_reference_btn
    Input Text    author    ${author}
    Input Text    title    ${title}
    Input Text    bib_category    ${bib_category}
    Input Text    bib_citekey    ${bib_citekey}
    Input Text    year    ${year}
    Input Text    doi_address    ${doi}
    Click Button    submit_note

Verify Succesful Addition
    [Arguments]    ${author}    ${title}    ${bib_category}    ${bib_citekey}    ${year}    ${doi}
    Go To Main Page
    Page Should Contain    ${author}
    Page Should Contain    ${title}
    Page Should Contain    ${bib_category}
    Page Should Contain    ${bib_citekey}
    Page Should Contain    ${year}
    Page Should Contain    ${doi}
