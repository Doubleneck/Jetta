*** Settings ***
Resource            resource.robot
Resource            register_resource.robot
Resource            login_resource.robot

Suite Setup         Open And Configure Browser
Suite Teardown      Close Browser
Test Setup          Reset Application And Create User And Go To Login Page


*** Test Cases ***
Login Page Shown
    Login Page Should Be Open

Register Click
    Click Button  Register
    Register Page Should Be Open

Login With Correct Credentials
    Input Login Credentials  ${VALID_USERNAME}  ${VALID_PASSWORD}
    Login Should Succeed

Login With Wrong Password
    Input Login Credentials  feilaaja  Salsana1
    Login Should Fail

*** Keywords ***
Reset Application And Create User And Go To Login Page
    Reset Application
    Create User  ${VALID_USERNAME}  ${VALID_PASSWORD}
    Go To Login Page
