*** Settings ***
Documentation   Ready Live River Gauge Tests
Library     ReadyLivePage      ${ENVFILE}    ${BROWSER}      ${URL}
Default Tags    LRG     Smoke

*** Test Cases ***
View Live River Gauge for Chiba
    log in   chibausername      chibapassword
    show no live river gauge predictions

View Live River Gauge for KC
    log in   kcusername      kcpassword
    get river gauge names   kc
    verify threshold chart legend   kc
    get no stats message
    get threshold reached list
    get posted
    get weather forecast time
    get max 1hr rainfall
    get max 24hr rainfall
    verify graph units
    ${start}    get graph start time
    ${end}      get graph end time
    get_total_duration  ${start}    ${end}
    verify view mlit links      kc

View Live River Gauge for Kawasaki
    log in   kawasakiusername      kawasakipassword
    get river gauge names   kawasaki
    verify threshold chart legend   kawasaki
    get no stats message
    get threshold reached list
    get posted
    get weather forecast time
    get max 1hr rainfall
    get max 24hr rainfall
    ${start}    get graph start time
    ${end}      get graph end time
    get_total_duration  ${start}    ${end}
    get graph end time
    verify view mlit links      kawasaki

View Live River Gauge for Koriyama
    log in   koriyamausername      koriyamapassword
    get river gauge names   koriyama
    verify threshold chart legend   koriyama
    get no stats message
    get threshold reached list
    get posted
    get weather forecast time
    get max 1hr rainfall
    get max 24hr rainfall
    verify graph units
    ${start}    get graph start time
    ${end}      get graph end time
    get_total_duration  ${start}    ${end}
    verify view mlit links      koriyama

View Live River Gauge for Nagano
    log in   naganousername      naganopassword
    get river gauge names   nagano
    verify threshold chart legend   nagano
    get no stats message
    get threshold reached list
    get posted
    get weather forecast time
    get max 1hr rainfall
    get max 24hr rainfall
    verify graph units
    ${start}    get graph start time
    ${end}      get graph end time
    get_total_duration  ${start}    ${end}
    verify view mlit links      nagano

View Live River Gauge for Okayama
    log in   okayamausername       okayamapassword
    get river gauge names   okayama
    verify threshold chart legend   okayama
    get no stats message
    get threshold reached list
    get posted
    get weather forecast time
    get max 1hr rainfall
    get max 24hr rainfall
    verify graph units
    ${start}    get graph start time
    ${end}      get graph end time
    get_total_duration  ${start}    ${end}
    verify view mlit links      okayama

View Live River Gauge for Okazaki
    log in   okazakiusername      okazakipassword
    get river gauge names   okazaki
    verify threshold chart legend   okazaki
    get no stats message
    get threshold reached list
    get posted
    get weather forecast time
    get max 1hr rainfall
    get max 24hr rainfall
    verify graph units
    ${start}    get graph start time
    ${end}      get graph end time
    get_total_duration  ${start}    ${end}
    verify view mlit links      okazaki
