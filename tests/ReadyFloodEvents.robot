*** Settings ***
Documentation   Ready Staging Flood Tests
Library    ReadyLivePage     ${ENVFILE}     ${BROWSER}      ${URL}
Default Tags    Flood   Staging

*** Test Cases ***
Verify Kumamoto flood event on staging
    navigate to url     ${URL}library/prediction/8045361v2_9_kumamoto
    log in  kcusername      kcpassword      False
    get library flood prediction view data

Verify Chiba flood event on staging
    navigate to url     ${URL}library/prediction/64659501v2_2_chiba
    log in  chibausername      chibapassword        False
    get library flood prediction view data

Verify Kawasaki flood event on staging
    navigate to url     ${URL}library/prediction/89129740v2_6_kawasaki
    log in  kawasakiusername      kawasakipassword      False
    get library flood prediction view data

Verify Nagano flood event on staging
    navigate to url     ${URL}library/prediction/65098633v2_58_nagano
    log in  naganousername      naganopassword      False
    get library flood prediction view data

Verify Okayama flood event on staging
    navigate to url     ${URL}library/prediction/87003754v2_13_okayama
    log in  okayamausername       okayamapassword      False
    get library flood prediction view data

Verify Okazaki flood event on staging
    navigate to url     ${URL}library/prediction/11172778v2_64_okazaki
    log in  okazakiusername      okazakipassword      False
    get library flood prediction view data
