*** Settings ***
Documentation   Ready Past River Gauge Prediction Tests
Library     ReadyPRGPPage      ${ENVFILE}    ${BROWSER}      ${URL}
Default Tags    PRGP    Smoke

*** Test Cases ***
Get Past River Gauge Predictions for Chiba
    log in   chibausername      chibapassword
    click past river gauge predictions
    show no past river gauge predictions

Get Past River Gauge Predictions for KC
    log in   kcusername      kcpassword
    click past river gauge predictions
    get river gauge names   kc
    get posted
    get weather forecast time
    get max 1hr rainfall
    get max 24hr rainfall
    verify graph units
    ${start}    get graph start time
    ${end}      get graph end time
    get_total_duration  ${start}    ${end}
    get max past river gauge predictions
    verify view mlit links      kc

Get Past River Gauge Predictions for Kawasaki
    log in   kawasakiusername      kawasakipassword
    click past river gauge predictions
    get river gauge names   kawasaki
    get posted
    get weather forecast time
    get max 1hr rainfall
    get max 24hr rainfall
    verify graph units
    ${start}    get graph start time
    ${end}      get graph end time
    get_total_duration  ${start}    ${end}
    get max past river gauge predictions
    verify view mlit links      kawasaki

Get Past River Gauge Predictions for Koriyama
    log in   koriyamausername      koriyamapassword
    click past river gauge predictions
    get river gauge names   koriyama
    get posted
    get weather forecast time
    get max 1hr rainfall
    get max 24hr rainfall
    ${start}    get graph start time
    ${end}      get graph end time
    get_total_duration  ${start}    ${end}
    get max past river gauge predictions
    verify view mlit links      koriyama

Get Past River Gauge Predictions for Nagano
    log in   naganousername      naganopassword
    click past river gauge predictions
    get river gauge names   nagano
    get posted
    get weather forecast time
    get max 1hr rainfall
    get max 24hr rainfall
    verify graph units
    ${start}    get graph start time
    ${end}      get graph end time
    get_total_duration  ${start}    ${end}
    get max past river gauge predictions
    verify view mlit links      nagano

Get Past River Gauge Predictions for Okayama
    log in   okayamausername       okayamapassword
    click past river gauge predictions
    get river gauge names   okayama
    get posted
    get weather forecast time
    get max 1hr rainfall
    get max 24hr rainfall
    verify graph units
    ${start}    get graph start time
    ${end}      get graph end time
    get_total_duration  ${start}    ${end}
    get max past river gauge predictions
    verify view mlit links      okayama

Get Past River Gauge Predictions for Okazaki
    log in   okazakiusername      okazakipassword
    click past river gauge predictions
    get river gauge names   okazaki
    get posted
    get weather forecast time
    get max 1hr rainfall
    get max 24hr rainfall
    verify graph units
    ${start}    get graph start time
    ${end}      get graph end time
    get_total_duration  ${start}    ${end}
    get max past river gauge predictions
    verify view mlit links      okazaki
