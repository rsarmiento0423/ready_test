*** Settings ***
Documentation   Ready Library API Tests
Library    LibraryAPI

*** Test Cases ***
Verify KC Library events
    [Tags]  API     LibraryAPI
    get kc library events

Verify Chiba Library events
    [Tags]  API     LibraryAPI
    get chiba library events

Verify Kawasaki Library events
    [Tags]  API     LibraryAPI
    get kawasaki library events

Verify Koriyama Library events
    [Tags]  API     LibraryAPI
    get koriyama library events

Verify Nagano Library events
    [Tags]  API     LibraryAPI
    get nagano library events

Verify Okayama Library events
    [Tags]  API     LibraryAPI
    get okayama library events

Verify Okazaki Library events
    [Tags]  API     LibraryAPI
    get okazaki library events
