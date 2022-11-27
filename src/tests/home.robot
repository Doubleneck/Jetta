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
    Set Username    Username
    Set Password    Password
    Submit Credentials
    Login Should Succeed


*** Keywords ***
Submit Credentials
    Click Button    Register

Set Username
    [Arguments]    ${username}
    Input Text    username    ${username}

Set Password
    [Arguments]    ${password}
    Input Password    password    ${password}

Set Password Confirmation
    [Arguments]    ${password}
    Input Password    password_confirm    ${password}

Login Should Succeed
    Main Page Should Be Open
    #Ei wörki, pysyy home-sivulla

Login Should Fail With Message
    [Arguments]    ${message}
    Login Page Should Be Open
    Page Should Contain    ${message}

Create User And Go To Home Page
    #ei wörki, syntyyköhän useri oikein?
    Create User    Username    Password
    Go To Home Page
    Home Page Should Be Open
