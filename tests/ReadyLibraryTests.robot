*** Settings ***
Documentation   Ready Library Tests
Resource  ../Resources/library_keywords.robot
Library    ReadyLibraryPage     ${ENVFILE}     ${BROWSER}      ${URL}
Default Tags    Library   Smoke

*** Test Cases ***
View seismic prediction card from Library as KC user
    log in   kcusername      kcpassword
    View Seismic Prediction Card

View seismic prediction card from Library as Chiba user
    log in   chibausername      chibapassword
    View Seismic Prediction Card

View seismic prediction card from Library as Kawasaki user
    log in   kawasakiusername      kawasakipassword
    View Seismic Prediction Card

View seismic prediction card from Library as Koriyama user
    log in   koriyamausername      koriyamapassword
    View Seismic Prediction Card

View seismic prediction card from Library as Nagano user
    log in   naganousername      naganopassword
    View Seismic Prediction Card

View seismic prediction card from Library as Okayama user
    log in   okayamausername      okayamapassword
    View Seismic Prediction Card

View seismic prediction card from Library as Okazaki user
    log in   okazakiusername      okazakipassword
    View Seismic Prediction Card

Verify old flood event with river gauge tab and no river gauges for Chiba
    log in   chibausername      chibapassword
    View Old Flood Event With No River Gauge

Verify old flood event with river gauge tab and 4 river gauges for KC
    log in   kcusername      kcpassword
    View Old Flood Event With River Gauge     kc

Verify old flood event with river gauge tab and 2 river gauges for Kawasaki
    log in   kawasakiusername      kawasakipassword
    View Old Flood Event With River Gauge     kawasaki


Verify old river event with river gauge tab and 2 river gauges for Koriyama
    log in   koriyamausername      koriyamapassword
    View Old Flood Event With River Gauge     koriyama

Verify old flood event with river gauge tab and 2 river gauges for Nagano
    log in   naganousername      naganopassword
    View Old Flood Event With River Gauge     nagano

Verify old flood event with river gauge tab and 2 river gauges for Okayama
    log in   okayamausername       okayamapassword
    View Old Flood Event With River Gauge     okayama

Verify old flood event with river gauge tab and 2 river gauges for Okazaki
    log in   okazakiusername      okazakipassword
    View Old Flood Event With River Gauge     okazaki

Verify no Seismic Simulation button exists for KC user
    log in   kcusername      kcpassword
    click library
    verify seismic simulation

Verify no Seismic Simulation button exists for Chiba user
    log in   chibausername      chibapassword
    click library
    verify seismic simulation

Verify no Seismic Simulation button exists for Kawasaki user
    log in   kawasakiusername      kawasakipassword
    click library
    verify seismic simulation

Verify no Seismic Simulation button exists for Koriyama user
    log in   koriyamausername      koriyamapassword
    click library
    verify seismic simulation

Verify no Seismic Simulation button exists for Nagano user
    log in   naganousername      naganopassword
    click library
    verify seismic simulation

Verify no Seismic Simulation button exists for Okayama user
    log in   okayamausername      okayamapassword
    click library
    verify seismic simulation

Verify no Seismic Simulation button exists for Okazaki user
    log in   okazakiusername      okazakipassword
    click library
    verify seismic simulation

Get list of seismic events as KC user
    log in   kcusername      kcpassword
    View Seismic Events

Get list of seismic events as Chiba user
    log in   chibausername      chibapassword
    View Seismic Events

Get list of seismic events as Kawasaki user
    log in   kawasakiusername      kawasakipassword
    View Seismic Events

Get list of seismic events as Koriyama user
    log in   koriyamausername      koriyamapassword
    View Seismic Events

Get list of seismic events as Nagano user
    log in   naganousername      naganopassword
    View Seismic Events

Get list of seismic events as Okayama user
    log in   okayamausername      okayamapassword
    View Seismic Events

Get list of seismic events as Okazaki user
    log in   okazakiusername      okazakipassword
    View Seismic Events

Verify library contains both seismic and flood events as KC user
    log in   kcusername      kcpassword
    click library
    verify library events

Verify library contains both seismic and flood events as Chiba user
    log in   chibausername      chibapassword
    click library
    verify library events

Verify library contains both seismic and flood events as Kawasaki user
    log in   kawasakiusername      kawasakipassword
    click library
    verify library events

Verify library contains both seismic and flood events as Koriyama user
    log in   koriyamausername      koriyamapassword
    click library
    verify library events

Verify library contains both seismic and flood events as Nagano user
    log in   naganousername      naganopassword
    click library
    verify library events

Verify library contains both seismic and flood events as Okayama user
    log in   okayamausername      okayamapassword
    click library
    verify library events

Verify library contains both seismic and flood events as Okazaki user
    log in   okazakiusername      okazakipassword
    click library
    verify library events

Verify no Simulation events under Library as Chiba user
    [Tags]  Skip
    log in   chibausername      chibapassword
    click library
    verify no simulation events

Verify no Simulation events under Library as KC user
    [Tags]  Library     Prod
    log in   kcusername      kcpassword
    click library
    verify no simulation events

Verify no Simulation events under Library as Kawasaki user
    [Tags]  Skip
    log in   kawasakiusername      kawasakipassword
    click library
    verify no simulation events

Verify no Simulation events under Library as Koriyama user
    [Tags]  Library     Prod
    log in   koriyamausername      koriyamapassword
    click library
    verify no simulation events

Verify no Simulation events under Library as Nagano user
    [Tags]  Skip
    log in   naganousername      naganopassword
    click library
    verify no simulation events

Verify no Simulation events under Library as Okayama user
    [Tags]  Skip
    log in   okayamausername       okayamapassword
    click library
    verify no simulation events

Verify no Simulation events under Library as Okazaki user
    [Tags]  Skip
    log in   okazakiusername      okazakipassword
    click library
    verify no simulation events
