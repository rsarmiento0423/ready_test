*** Settings ***
Documentation   Ready Smoke Tests
Library     ReadyProfilePage     ${ENVFILE}     ${BROWSER}      ${URL}
Default Tags    Sanity

*** Test Cases ***
Login as KC User
    log in   kcusername     kcpassword
    log out

Login as Chiba User
    log in   chibausername      chibapassword
    log out

Login as Kawasaki User
    log in   kawasakiusername      kawasakipassword
    log out

Login as Koriyama User
    log in   koriyamausername      koriyamapassword
    log out

Login as Nagano User
    log in   naganousername      naganopassword
    log out

Login as Okayama User
    log in   okayamausername       okayamapassword
    log out

Login as Okazaki User
    log in   okazakiusername      okazakipassword
    log out

Login with invalid password
    login negative    rsarmiento+okazaki@oneconcern.com    therandompasswor

Login with no password
    login negative    rsarmiento+okazaki@oneconcern.com    blank

Login with invalid username
    login negative    rsarmiento+okazaki2@oneconcern.com   therandompassword

Login with no username
    login negative    blank    therandompassword

Login as Domino user with no access to Ready
    login with no permission    dominousername    dominopassword

Click Forgot password link
    click forgot password

Update job title in Profile as KC User
    log in   kcusername      kcpassword
    click profile
    verify profile
    enter firstname  Ray
    enter lastname  KC
    enter jobtitle  QA Tester
    click save changes

Missing required first name in Profile as KC User
    log in   kcusername      kcpassword
    click profile
    verify profile
    missing required    nofirst     skip

Missing required last name in Profile as KC User
    log in   kcusername      kcpassword
    click profile
    verify profile
    missing required    skip     nolast

Missing job title in Profile as KC User
    log in   kcusername      kcpassword
    click profile
    verify profile
    enter firstname  Ray
    enter lastname  KC
    enter jobtitle  missing
    click save changes
