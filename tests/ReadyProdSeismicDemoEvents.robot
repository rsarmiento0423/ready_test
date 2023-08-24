*** Settings ***
Documentation   Ready Seismic Demo Event Tests on Production
Library    ReadyLivePage     ${ENVFILE}     ${BROWSER}      ${URL}
Default Tags    Demo

*** Test Cases ***
Verify seismic event '23Z6DYIQf5pUUxUC5AZskQCLM1C' using Kumamoto Non-E2E account
    navigate to url     ${URL}library/prediction/23Z6DYIQf5pUUxUC5AZskQCLM1C
    log in  kcusername      kcpassword      False
    get seismic prediction view data

Verify seismic event '23Z9PnJ8fkrQYiIBBEf4dJ4hRaH' using Chiba Non-E2E accounts
    navigate to url     ${URL}library/prediction/23Z9PnJ8fkrQYiIBBEf4dJ4hRaH
    log in  chibausername       chibapassword      False
    get seismic prediction view data

Verify seismic event '23Z9PnJ8fkrQYiIBBEf4dJ4hRaH' using Kawasaki Non-E2E accounts
    navigate to url     ${URL}library/prediction/23Z9PnJ8fkrQYiIBBEf4dJ4hRaH
    log in  kawasakiusername       kawasakipassword      False
    get seismic prediction view data

Verify seismic event '23ZBL3vZJipewxRcjUWCwzjKUCb' using Chiba Non-E2E account
    navigate to url     ${URL}library/prediction/23ZBL3vZJipewxRcjUWCwzjKUCb
    log in  chibausername      chibapassword        False
    get seismic prediction view data

Verify seismic event '23ZBiLF1Rilj986kSUGussUiNEN' using Kawasaki Non-E2E account
    navigate to url     ${URL}library/prediction/23ZBiLF1Rilj986kSUGussUiNEN
    log in  kawasakiusername      kawasakipassword      False
    get seismic prediction view data

Verify seismic event '23ZBh5foM2RHQsIxpeAt8hSJBlz' using Nagano Non-E2E account
    navigate to url     ${URL}library/prediction/23ZBh5foM2RHQsIxpeAt8hSJBlz
    log in  naganousername      naganopassword      False
    get seismic prediction view data

Verify seismic event '23ZBcuPZDND75soUbl0RyBRWvfX' using Okayama Non-E2E account
    navigate to url     ${URL}library/prediction/23ZBcuPZDND75soUbl0RyBRWvfX
    log in  okayamausername      okayamapassword      False
    get seismic prediction view data

Verify seismic event '23ZBf6a8zbUrcaAiLaY53WbTDgP' using Okazaki Non-E2E account
    navigate to url     ${URL}library/prediction/23ZBf6a8zbUrcaAiLaY53WbTDgP
    log in  okazakiusername      okazakipassword      False
    get seismic prediction view data
