*** Settings ***
Library             SeleniumLibrary
Library             ../AppLibrary.py
Resource            resource.robot

*** Keywords ***
Input Login Credentials
    [Arguments]  ${username}  ${password}
    Set Login Username  ${username}
    Set Login Password  ${password}
    Click Button  Login

Set Login Username
    [Arguments]  ${username}    
    Input Text  username  ${username}

Set Login Password
    [Arguments]  ${password}
    Input Text  password  ${password}

Login Should Succeed
    Main Page Should Be Open

Login Should Fail
    Login Page Should Be Open
