*** Settings ***
Library             SeleniumLibrary
Library             ../AppLibrary.py
Resource            resource.robot

*** Keywords ***
Create User
    [Arguments]  ${username}  ${password}
    Go To Register Page
    Register Page Should Be Open
    Input Register Credentials  ${username}  ${password}  ${password}

Input Register Credentials
    [Arguments]  ${username}  ${password}  ${password_confirmation}
    Set Register Username  ${username}
    Set Register Password  ${password}
    Set Register Password Confirmation  ${password_confirmation}
    Click Button  Register

Set Register Username
    [Arguments]  ${username}    
    Input Text  username  ${username}

Set Register Password
    [Arguments]  ${password}
    Input Text  password  ${password}

Set Register Password Confirmation
    [Arguments]  ${password}
    Input Text  password_confirm  ${password}

Register Should Succeed
    Main Page Should Be Open

Register Should Fail
    Register Page Should Be Open
