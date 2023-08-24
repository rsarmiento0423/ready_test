*** Settings ***
Documentation   Ready User API Tests
Library    UserAPI

*** Test Cases ***
Verify KC User
    [Tags]  API     User
    get kc user

Verify Chiba User
    [Tags]  API     User
    get chiba user

Verify Kawasaki User
    [Tags]  API     User
    get kawasaki user

Verify Koriyama User
    [Tags]  API     User
    get koriyama user

Verify Nagano User
    [Tags]  API     User
    get nagano user

Verify Okayama User
    [Tags]  API     User
    get okayama user

Verify Okazaki User
    [Tags]  API     User
    get okazaki user
