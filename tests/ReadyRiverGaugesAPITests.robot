*** Settings ***
Documentation   Ready River Gauges API Tests
Library    RiverGaugesAPI

*** Test Cases ***
Verify KC river gauge values
    [Tags]  API     RiverGauges
    verify kc river gauges

Verify Chiba river gauge values
    [Tags]  API     RiverGauges
    verify chiba river gauges

Verify Kawasaki river gauge values
    [Tags]  API     RiverGauges
    verify kawasaki river gauges

Verify Koriyama river gauge values
    [Tags]  API     RiverGauges
    verify koriyama river gauges

Verify Nagano river gauge values
    [Tags]  API     RiverGauges
    verify nagano river gauges

Verify Okayama river gauge values
    [Tags]  API     RiverGauges
    verify okayama river gauges

Verify Okazaki river gauge values
    [Tags]  API     RiverGauges
    verify okazaki river gauges
