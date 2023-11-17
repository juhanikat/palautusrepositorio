*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kallestart
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  Username is not valid

Register With Valid Username And Invalid Password
    Set Username  kalle2
    Set Password  kalle
    Set Password Confirmation  kalle
    Submit Credentials
    Register Should Fail With Message  Password is not valid

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle3
    Set Password  kalle123
    Set Password Confirmation  kalleeeh
    Submit Credentials
    Register Should Fail With Message  Password does not match confirmation

Login After Successful Registration
    Set Username  kallestart
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Go To Login Page
    Set Username  kallestart
    Set Password  kalle123
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  k
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Go To Login Page
    Set Username  k
    Set Password  kalle123
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password
*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login


Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Register Should Succeed
    Title Should Be  Welcome to Ohtu Application!

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}