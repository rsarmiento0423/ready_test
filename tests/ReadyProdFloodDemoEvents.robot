*** Settings ***
Documentation   Ready Flood Demo Event Tests on Production
Library    ReadyLivePage     ${ENVFILE}     ${BROWSER}      ${URL}
Default Tags    Demo

*** Test Cases ***
Verify flood event '8045361v2_9_kumamoto' using Kumamoto Non-E2E account
    navigate to url     ${URL}library/prediction/8045361v2_9_kumamoto
    log in  kcusername      kcpassword      False
    get library flood prediction view data
    click play

Verify flood event '87003754v2_13_okayama' using Okayama Non-E2E account
    navigate to url     ${URL}library/prediction/87003754v2_13_okayama
    log in  okayamausername       okayamapassword      False
    get library flood prediction view data
    click play

Verify flood event '11172778v2_64_okazaki' using Okazaki Non-E2E account
    navigate to url     ${URL}library/prediction/11172778v2_64_okazaki
    log in  okazakiusername      okazakipassword      False
    get library flood prediction view data
    click play

Verify flood event '65098633v2_58_nagano' using Nagano Non-E2E account
    navigate to url     ${URL}library/prediction/65098633v2_58_nagano
    log in  naganousername      naganopassword      False
    get library flood prediction view data
    click play

Verify flood event '89129740v2_6_kawasaki' using Kawasaki Non-E2E account
    navigate to url     ${URL}library/prediction/89129740v2_6_kawasaki
    log in  kawasakiusername      kawasakipassword      False
    get library flood prediction view data
    click play

Verify flood event '64659501v2_2_chiba' using Chiba Non-E2E account
    navigate to url     ${URL}library/prediction/64659501v2_2_chiba
    log in  chibausername      chibapassword        False
    get library flood prediction view data
    click play

Verify flood event '45051247_46_koriyam' using Koriyama Non-E2E account
    navigate to url     ${URL}library/prediction/45051247_46_koriyam
    log in  koriyamausername      koriyamapassword      False
    get library flood prediction view data
    click play
