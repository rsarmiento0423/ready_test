*** Settings ***
Documentation   Ready Live Tests
Library    ReadyLivePage    ${ENVFILE}   ${BROWSER}     ${URL}
Default Tags    Live  Smoke

*** Test Cases ***
Verify Blue Sky as KC user
    log in   kcusername      kcpassword
    verify blue sky

Verify Blue Sky as Chiba user
    log in   chibausername      chibapassword
    verify blue sky

Verify Blue Sky as Kawsaki user
    log in   kawasakiusername      kawasakipassword
    verify blue sky

Verify Blue Sky as Koriyama user
    log in   koriyamausername      koriyamapassword
    verify blue sky

Verify Blue Sky as Nagano user
    log in   naganousername      naganopassword
    verify blue sky

Verify Blue Sky as Okayama user
    log in   okayamausername      okayamapassword
    verify blue sky

Verify Blue Sky as Okazaki user
    log in   okazakiusername      okazakipassword
    verify blue sky

Navigate to Past Prediction as KC user
    log in   kcusername      kcpassword
    click past predictions

Navigate to Library as KC user
    log in   kcusername      kcpassword
    click library

Navigate to Live as KC user
    log in   kcusername      kcpassword
    click live

Navigate to Profile as KC user
    log in   kcusername      kcpassword
    click profile

Navigate to Help as KC user
    log in   kcusername      kcpassword
    click help

Navigate to Terms and Conditions as KC user
    log in   kcusername      kcpassword
    click terms conditions

Get all prediction cards displayed on Live as KC user
    [Tags]  Skip
    log in   kcusername      kcpassword
    get live prediction cards titles
    get prediction cards total impacted people
    get prediction cards total impacted buildings

Get seismic event displayed on Live as KC user
    [Tags]  Skip
    log in   kcusername      kcpassword
    find seismic event
    click seismic view prediction button
    get seismic prediction view data

Get flood event displayed on Live as KC user
    [Tags]  Skip
    log in   kcusername      kcpassword
    find flood event
    click flood view prediction button
    get flood prediction view_data

Get all prediction cards displayed on Live as Chiba user
    [Tags]  Skip
    log in   chibausername      chibapassword
    get live prediction cards titles
    get prediction cards total impacted people
    get prediction cards total impacted buildings

Get seismic event displayed on Live as Chiba user
    [Tags]  Skip
    log in   chibausername      chibapassword
    find seismic event
    click seismic view prediction button
    get seismic prediction view data

Get flood event displayed on Live as Chiba user
    [Tags]  Skip
    log in   chibausername      chibapassword
    find flood event
    click flood view prediction button
    get flood prediction view_data

Get all prediction cards displayed on Live as Kawasaki user
    [Tags]  Skip
    log in   kawasakiusername      kawasakipassword
    get live prediction cards titles
    get prediction cards total impacted people
    get prediction cards total impacted buildings

Get seismic event displayed on Live as Kawasaki user
    [Tags]  Skip
    log in   kawasakiusername      kawasakipassword
    find seismic event
    click seismic view prediction button
    get seismic prediction view data

Get flood event displayed on Live as Kawasaki user
    [Tags]  Skip
    log in   kawasakiusername      kawasakipassword
    find flood event
    click flood view prediction button
    get flood prediction view_data

Get all prediction cards displayed on Live as Nagano user
    [Tags]  Skip
    log in   naganousername      naganopassword
    get live prediction cards titles
    get prediction cards total impacted people
    get prediction cards total impacted buildings

Get seismic event displayed on Live as Nagano user
    [Tags]  Skip
    log in   naganousername      naganopassword
    find seismic event
    click seismic view prediction button
    get seismic prediction view data

Get flood event displayed on Live as Nagano user
    [Tags]  Skip
    log in   naganousername      naganopassword
    find flood event
    click flood view prediction button
    get flood prediction view_data

Get all prediction cards displayed on Live as Okayama user
    [Tags]  Skip
    log in   okayamausername      okayamapassword
    get live prediction cards titles
    get prediction cards total impacted people
    get prediction cards total impacted buildings

Get seismic event displayed on Live as Okayama user
    [Tags]  Skip
    log in   okayamausername      okayamapassword
    find seismic event
    click seismic view prediction button
    get seismic prediction view data

Get flood event displayed on Live as Okayama user
    [Tags]  Skip
    log in   okayamausername      okayamapassword
    find flood event
    click flood view prediction button
    get flood prediction view_data

Get all prediction cards displayed on Live as Okazaki user
    [Tags]  Skip
    log in   okazakiusername      okazakipassword
    get live prediction cards titles
    get prediction cards total impacted people
    get prediction cards total impacted buildings

Get seismic event displayed on Live as Okazaki user
    [Tags]  Skip
    log in   okazakiusername      okazakipassword
    find seismic event
    click seismic view prediction button
    get seismic prediction view data

Get flood event displayed on Live as Okazaki user
    [Tags]  Skip
    log in   okazakiusername      okazakipassword
    find flood event
    click flood view prediction button
    get flood prediction view_data

Verify river gauge graph is in meters for EN and JP
    log in   kcusername      kcpassword
    switch locale verify units
