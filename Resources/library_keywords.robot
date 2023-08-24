*** Settings ***
Documentation   Library Keywords
Library    ReadyLibraryPage     ${ENVFILE}     ${BROWSER}      ${URL}

*** Keywords ***
View Seismic Prediction Card
    click library
    click first historical seismic event
    get first prediction view

View Old Flood Event With No River Gauge
    click library
    choose first historical flood event
    verify river gauge tab
    verify no river gauge station

View Old Flood Event With River Gauge
    [Arguments]  ${geo}
    click library
    choose first historical flood event
    verify river gauge tab
    verify river gauges     ${geo}
    verify view mlit links  ${geo}
    verify river gauge graphs   ${geo}
    get gauge addresses
    get river systems
    get river names
    get river threshold list
    get river threshold legend text
    click play

View Seismic Events
    click library
    get all prediction cards titles
    get all prediction cards types
    get all prediction cards total impacted people
    get all prediction cards total impacted buildings
    get all prediction cards time of earthquake
    get all prediction cards magnitude
    get all prediction cards location
    get all prediction cards epicenter
    get all prediction cards depth
    get all library urls
