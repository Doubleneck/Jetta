*** Settings ***
Resource            resource.robot

Suite Setup         Open And Configure Browser
Suite Teardown      Close Browser
Test Setup          Create User And Go To Home Page


*** Test Cases ***
Home Page Shown
    Home Page Should Be Open

Register Click
    Home Page Should Be Open
    Click Button    Register
    Register Page Should Be Open

Login With Correct Credentials
    Login Page Should Be Open
    Set Username    Loginuser1
    Set Password    Loginpassword1
    Submit Login Credentials
    Login Should Succeed

Login With Wrong Password
    Login Page Should Be Open
    Set Username    Loginuser1
    Set Password    Loginpassword2
    Submit Login Credentials
    Login Should Fail

*** Keywords ***
Submit Login Credentials
    Click Button    Login

Set Username
    [Arguments]    ${username}
    Input Text    username    ${username}

Set Password
    [Arguments]    ${password}
    Input Password    password    ${password}

Login Should Succeed
    Main Page Should Be Open

Login Should Fail
    Login Page Should Be Open
    

Create User And Go To Home Page
    Create User    Loginuser1    Loginpassword1
    Go To Home Page
    Home Page Should Be Open
