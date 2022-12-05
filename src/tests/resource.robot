*** Settings ***
Library             SeleniumLibrary
Library             ../AppLibrary.py


*** Variables ***
${SERVER}           localhost:5000
${BROWSER}          headlesschrome
# ${BROWSER}          chrome
${DELAY}            0 seconds
# ${DELAY}            0.2 seconds
${LOGIN URL}        http://${SERVER}
${REGISTER URL}     http://${SERVER}/register
${MAIN_URL}         http://${SERVER}/main
${VALID_USERNAME}   testaaja
${VALID_PASSWORD}   Salasana1


*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Go To Login Page
    Go To  ${LOGIN URL}

Go To Register Page
    Go To  ${REGISTER URL}

Go To Main Page
    Go To  ${MAIN_URL}

Login Page Should Be Open
    Title Should Be  Login

Register Page Should Be Open
    Title Should Be  Register

Main Page Should Be Open
    Page Should Contain  ${VALID_USERNAME}
