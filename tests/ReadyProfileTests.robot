*** Settings ***
Documentation   Ready Profile Tests
Library    ReadyProfilePage     ${ENVFILE}   ${BROWSER}      ${URL}
Default Tags    Profile  Smoke

*** Test Cases ***
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
