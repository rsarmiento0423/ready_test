*** Settings ***
Documentation  Past Predciton Keywords
Library    ReadyPastPredictionsPage    ${ENVFILE}    ${BROWSER}      ${URL}

*** Keywords ***
Hit Play Button
    click past predictions
    click first prediction card
    click play

View Shelters for Flood Map
    click past predictions
    click first prediction card
    click nav layers
    click flood normal map
    click velocity arrows
    click velocity arrows
    click basic shelters
    click short term shelters
    click wide area shelters
    click all shelters
    click all shelters

View Shelters for Satellite Map
    click past predictions
    click first prediction card
    click nav layers
    click show satellite
    click velocity arrows
    click velocity arrows
    click basic shelters
    click short term shelters
    click wide area shelters
    click all shelters
    click all shelters

View Shelters for Impact Map
    click past predictions
    click first prediction card
    click nav layers
    click impact map
    click basic shelters
    click short term shelters
    click wide area shelters
    click all shelters
    click all shelters

View Past Predictions
    click past predictions
    get all prediction cards titles
    get all prediction cards total impacted people
    get all prediction cards total impacted buildings
    get all prediction cards date prediction begins
    get all prediction cards date prediction ends
    get all prediction cards date posted
    get all past predictions urls

Check No River Gauge Tab
    click past predictions
    click first prediction card
    verify no river gauge tab
