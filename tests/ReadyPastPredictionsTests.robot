*** Settings ***
Documentation   Ready Past Prediction Tests
Resource  ../Resources/past_prediction_keywords.robot
Library    ReadyPastPredictionsPage    ${ENVFILE}    ${BROWSER}      ${URL}
Default Tags    PastPredictions  Smoke

*** Test Cases ***
Toggle Nagano flood favorite
    [Tags]  Staging
    log in   naganousername      naganopassword
    click past predictions
    click first prediction card
    toggle star prediction

Play Chiba flood
    log in   chibausername      chibapassword
    Hit Play Button

Play KC flood
    log in   naganousername      naganopassword
    Hit Play Button

Play Kawasaki flood
    log in   kawasakiusername      kawasakipassword
    Hit Play Button

Play Koriyama flood
    log in   koriyamausername      koriyamapassword
    Hit Play Button

Play Nagano flood
    log in   naganousername      naganopassword
    Hit Play Button

Play Okayama flood
    log in   okayamausername       okayamapassword
    Hit Play Button

Play Okazaki flood
    log in   okazakiusername      okazakipassword
    Hit Play Button

Show flood map with velocity arrows and all shelter combinations for Chiba flood
    log in   chibausername      chibapassword
    View Shelters for Flood Map

Show satellite map with velocity arrows and all shelter combinations for Chiba flood
    log in   chibausername      chibapassword
    View Shelters for Satellite Map

Show impact map with all shelter combinations for Chiba flood
    log in   chibausername      chibapassword
    View Shelters for Impact Map

Show flood map with velocity arrows and all shelter combinations for KC flood
    log in   kcusername     kcpassword
    View Shelters for Flood Map

Show satellite map with velocity arrows and all shelter combinations for KC flood
    log in   kcusername     kcpassword
    View Shelters for Satellite Map

Show impact map with all shelter combinations for KC flood
    log in   kcusername     kcpassword
    View Shelters for Impact Map

Show flood map with velocity arrows and all shelter combinations for Kawasaki flood
    log in   kawasakiusername      kawasakipassword
    View Shelters for Flood Map

Show satellite map with velocity arrows and all shelter combinations for Kawasaki flood
    log in   kawasakiusername      kawasakipassword
    View Shelters for Satellite Map

Show impact map with all shelter combinations for Kawasaki flood
    log in   kawasakiusername      kawasakipassword
    View Shelters for Impact Map

Show flood map with velocity arrows and all shelter combinations for Koriyama flood
    log in   koriyamausername      koriyamapassword
    View Shelters for Flood Map

Show satellite map with velocity arrows and all shelter combinations for Koriayma flood
    log in   koriyamausername      koriyamapassword
    View Shelters for Satellite Map

Show impact map with all shelter combinations for Koriyama flood
    log in   koriyamausername      koriyamapassword
    View Shelters for Impact Map

Show flood map with velocity arrows and all shelter combinations for Nagano flood
    log in   naganousername      naganopassword
    View Shelters for Flood Map

Show satellite map with velocity arrows and all shelter combinations for Nagano flood
    log in   naganousername      naganopassword
    View Shelters for Satellite Map

Show impact map with all shelter combinations for Nagano flood
    log in   naganousername      naganopassword
    View Shelters for Impact Map

Show flood map with velocity arrows and all shelter combinations for Okayama flood
    log in   okayamausername       okayamapassword
    View Shelters for Flood Map

Show satellite map with velocity arrows and all shelter combinations for Okayama flood
    log in   okayamausername       okayamapassword
    View Shelters for Satellite Map

Show impact map with all shelter combinations for Okayama flood
    log in   okayamausername       okayamapassword
    View Shelters for Impact Map

Show flood map with velocity arrows and all shelter combinations for Okazaki flood
    log in   okazakiusername      okazakipassword
    View Shelters for Flood Map

Show satellite map with velocity arrows and all shelter combinations for Okazaki flood
    log in   okazakiusername      okazakipassword
    View Shelters for Satellite Map

Show impact map with all shelter combinations for Okazaki flood
    log in   okazakiusername      okazakipassword
    View Shelters for Impact Map

Get list of Past Predictions as Chiba user
    log in   chibausername      chibapassword
    View Past Predictions
    verify expected geo   chiba

Get list of Past Predictions as Koriyama user
    log in   koriyamausername      koriyamapassword
    View Past Predictions
    verify expected geo   koriyam

Get list of Past Predictions as KC user
    log in   kcusername      kcpassword
    View Past Predictions

Get list of Past Predictions as Nagano user
    log in   naganousername      naganopassword
    View Past Predictions
    verify expected geo     nagano

Get list of Past Predictions as Okayama user
    log in   okayamausername       okayamapassword
    View Past Predictions
    verify expected geo     okayama

Get list of Past Predictions as Okazaki user
    log in   okazakiusername      okazakipassword
    View Past Predictions
    verify expected geo     okazaki

Get list of Past Predictions as KC e2e user
    log in   kce2eusername      kce2epassword
    View Past Predictions

Verify no presence of river gauge tab as Chiba user
    log in   chibausername      chibapassword
    Check No River Gauge Tab

Verify no presence of river gauge tab as KC user
    log in   kcusername      kcpassword
    Check No River Gauge Tab

Verify no presence of river gauge tab as Kawasaki user
    log in   kawasakiusername      kawasakipassword
    Check No River Gauge Tab

Verify no presence of river gauge tab as Koriyama user
    log in   koriyamausername      koriyamapassword
    Check No River Gauge Tab

Verify no presence of river gauge tab as Okayama user
    log in   okayamausername      okayamapassword
    Check No River Gauge Tab

Verify no presence of river gauge tab as Okazaki user
    log in   okazakiusername      okazakipassword
    Check No River Gauge Tab
