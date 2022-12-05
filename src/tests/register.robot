*** Settings ***
Resource            resource.robot
Resource            register_resource.robot

Suite Setup         Open And Configure Browser
Suite Teardown      Close Browser
Test Setup          Reset Application And Go To Register Page


*** Test Cases ***
Register With Valid Username And Password
    Create User  ${VALID_USERNAME}  ${VALID_PASSWORD}
    Register Should Succeed

Register With Not Matching Password And Password Confirmation
    Go To Register Page
    Register Page Should Be Open
    Input Register Credentials  ${VALID_USERNAME}  Salasana1  Salesana1
    Register Should Fail

*** Keywords ***
Reset Application And Go To Register Page
    Reset Application
    Go To Register Page
