*** Settings ***
Library     SeleniumLibrary


*** Variables ***
${SERVER}       localhost:5000
${BROWSER}      chrome
${DELAY}        1.0 seconds
${HOME URL}     http://${SERVER}
${LOGIN URL}    http://${SERVER}/login


*** Keywords ***
Open And Configure Browser
    Open Browser    browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}

Jetta Application Page Should Be Open
    Page Should Contain    Ohtu-Miniprojekti

Go To Main Page
    Go To    ${HOME URL}
