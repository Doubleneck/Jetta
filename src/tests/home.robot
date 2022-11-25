*** Settings ***
Resource            resource.robot

Suite Setup         Open And Configure Browser
Suite Teardown      Close Browser
Test Setup          Go To Main Page


*** Test Cases ***
Homepage Should Be Succeed
    Access Jetta main Succeed


*** Keywords ***
Access Jetta main Succeed
    Jetta Application Page Should Be Open
