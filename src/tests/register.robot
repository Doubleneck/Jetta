*** Settings ***
Resource            resource.robot

Suite Setup         Open And Configure Browser
Suite Teardown      Close Browser
Test Setup          Create User And Go To Register Page


*** Test Cases ***
Register With Valid Username And Password
    Go To Register Page
    Register Page Should Be Open
    Set Username    Testuser1
    Set Password    Testpassword1
    Set Password Confirmation    Testpassword1
    Submit Credentials
    Register Should Succeed

Register With Not Matching Password And Password Confirmation
    Go To Register Page
    Register Page Should Be Open
    Set Username    Testuser
    Set Password    Testpassword
    Set Password Confirmation    testpassword
    Submit Credentials
    Register Should Fail


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

Register Should Succeed
    Main Page Should Be Open

Register Should Fail
    Register Page Should Be Open

Create User And Go To Register Page
    Create User    Username1    Password1
    Go To Register Page
    Register Page Should Be Open
