*** Settings ***
Resource            resource.robot
Resource            register_resource.robot
Resource            note_resource.robot

Suite Setup         Open And Configure Browser
Suite Teardown      Close Browser
Test Setup          Reset Application And Create User


*** Test Cases ***
Main page Shown
    Main Page Should Be Open

Adding And Viewing notes
    Add Note And Verify  Robert Martin  Clean Code  Book  CCRM08  2008  ISBN:978-0-13-235088-4
    Add Note And Verify  Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides, Grady Booch  Design Patterns: Elements of Reusable Object-Oriented Software, 1st Edition  Book  DP94  1994  ISBN-13:978-0201633610
    Add Note And Verify  Brian Kernighan, Dennis Ritchie  The C Programming Language  Book  TCPL78  1978  ISBN:9780131101630

*** Keywords ***
Reset Application And Create User
    Reset Application
    Create User  ${VALID_USERNAME}  ${VALID_PASSWORD}
