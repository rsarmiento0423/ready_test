*** Settings ***
Documentation   Ready 3hrs apart for Past River Gauge Prediction on Production
Library     ReadyPRGPPage      ${ENVFILE}    ${BROWSER}      ${URL}
Default Tags    PRGP    Prod

*** Test Cases ***
Verify 3 hours apart on Past River Gauge Predictions for KC with 36 hours duration
    log in   kcusername      kcpassword
    click past river gauge predictions
    verify threshold chart legend   kc
    ${start}    get graph start time
    ${end}      get graph end time
    get_total_duration  ${start}    ${end}  prod
    get past river gauge headers

Verify 3 hours apart on Past River Gauge Predictions for Kawasaki with 36 hours duration
    log in   kawasakiusername      kawasakipassword
    click past river gauge predictions
    verify threshold chart legend   kawasaki
    ${start}    get graph start time
    ${end}      get graph end time
    get_total_duration  ${start}    ${end}  prod
    get past river gauge headers

Verify 3 hours apart on Past River Gauge Predictions for Koriyama with 36 hours duration
    log in   koriyamausername      koriyamapassword
    click past river gauge predictions
    verify threshold chart legend   koriyama
    ${start}    get graph start time
    ${end}      get graph end time
    get_total_duration  ${start}    ${end}  prod
    get past river gauge headers

Verify 36 hours apart on Past River Gauge Predictions for Nagano with 36 hours duration
    log in   naganousername      naganopassword
    click past river gauge predictions
    verify threshold chart legend   nagano
    ${start}    get graph start time
    ${end}      get graph end time
    get_total_duration  ${start}    ${end}  prod
    get past river gauge headers

Verify 36 hours apart on Past River Gauge Predictions for Okayama with 36 hours duration
    log in   okayamausername       okayamapassword
    click past river gauge predictions
    verify threshold chart legend   okayama
    ${start}    get graph start time
    ${end}      get graph end time
    get_total_duration  ${start}    ${end}  prod
    get past river gauge headers

Verify 36 hours apart on Past River Gauge Predictions for Okazaki with 36 hours duration
    log in   okazakiusername      okazakipassword
    click past river gauge predictions
    verify threshold chart legend   okazaki
    ${start}    get graph start time
    ${end}      get graph end time
    get_total_duration  ${start}    ${end}  prod
    get past river gauge headers
