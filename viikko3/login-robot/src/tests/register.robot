*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Input Register Command
    Input Credentials  abc  abcdefgh123
    Output Should Contain  New user registered


Register With Already Taken Username And Valid Password
    Input Register Command
    Input Credentials  abc  abcdefgh123
    Input Register Command
    Input Credentials  abc  abcdefgh123
    Output Should Contain  Username already exists


Register With Too Short Username And Valid Password
    Input Register Command
    Input Credentials  ab  abcdefgh123
    Output Should Contain  Username is not valid

Register With Enough Long But Invalid Username And Valid Password
    Input Register Command
    Input Credentials  abc123  abcdefgh123
    Output Should Contain  Username is not valid

Register With Valid Username And Too Short Password
    Input Register Command
    Input Credentials  abc  abcd
    Output Should Contain  Password is not valid

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Register Command
    Input Credentials  abc  abcdefgh
    Output Should Contain  Password is not valid