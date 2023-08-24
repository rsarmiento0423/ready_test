*** Settings ***
Documentation   Ready Library Tests
Library     SeleniumLibrary         
Library     ReadyPredictionsPage     ${ENVFILE}     ${BROWSER}      ${URL} 
Library     ../../libs/DebugLib.py

Default Tags        E2E     regression      seismicv2regression     v2regression


*** Test Cases ***
Great Tohuku - Chiba user
    [Documentation]     Log in with Chiba user and make sure cards for kawasaki doesnt appear
    log in   chibausername      chibapassword
    click library
    impacted people shouldnt appear    3310   

Great Tohuku - Kawasaki user
    [Documentation]     Log in with Kawasaki user and make sure cards for Chiba doesnt appear
    log in   kawasakiusername      kawasakipassword
    click library
    impacted people shouldnt appear    1780

Hexagon opacity
    [Documentation]     Change the opacity of hexagons to 100
    log in      kawasakiusername      kawasakipassword
    click library
    click first prediction card
    click map display
    slide hexagon opacity

Impacted people/buildings Kawasaki
    [Documentation]     Validate if the impacted number are correct for the region
    log in      kawasakiusername      kawasakipassword
    click library
    impacted geo people should be       kawasaki-auto-      98300
    impacted geo building should be     kawasaki-auto-      14000          

Impacted people/buildings Kawasaki-Great Tohuku
    [Documentation]     Validate if the impacted number are correct for the region
    log in      kawasakiusername      kawasakipassword
    click library
    impacted geo people should be       great-tohuku-auto-      2940
    impacted geo building should be     great-tohuku-auto-      490

Impacted people/buildings Chiba
    [Documentation]     Validate if the impacted number are correct for the region
    log in      chibausername      chibapassword
    click library
    impacted geo people should be       chiba-auto-         73900
    impacted geo building should be     chiba-auto-         12200

Impacted people/buildings Chiba-Great Tohuku
    [Documentation]     Validate if the impacted number are correct for the region
    log in      chibausername      chibapassword  
    click library
    impacted geo people should be       great-tohuku-auto-      1640
    impacted geo building should be     great-tohuku-auto-      512

Impacted people/buildings Nagano
    [Documentation]     Validate if the impacted number are correct for the region
    log in      naganousername      naganopassword
    click library
    impacted geo people should be       nagano-auto-         32200
    impacted geo building should be     nagano-auto-         8940

Impacted people/buildings Okazaki
    [Documentation]     Validate if the impacted number are correct for the region
    log in      okazakiusername      okazakipassword
    click library
    impacted geo people should be       okazaki-auto-         29900
    impacted geo building should be     okazaki-auto-         6810

Impacted people/buildings Okayama
    [Documentation]     Validate if the impacted number are correct for the region
    log in      okayamausername      okayamapassword
    click library
    impacted geo people should be       okayama-auto-         61200
    impacted geo building should be     okayama-auto-         15900

Library events with Chiba user
    [Documentation]     Test to validate the card appear correctly under Library. Validate if the layer functions works on the event when we open one.  
    log in                      chibausername      chibapassword
    click library
    click card with title       chiba-auto-
    click map display
    click show satellite
    click show map
    click map display
    slide hexagon opacity
    click all shelters
    click basic shelters
    click short term_shelters
    click wide area shelters
    return from seismic card
    log out

Library events with Kawasaki user
    [Documentation]     Test to validate the card appear correctly under Library. Validate if the layer functions works on the event when we open one.  
    log in                      kawasakiusername      kawasakipassword
    click library
    click card with title       kawasaki-auto-
    click map display
    click show satellite
    click show map
    click map display
    slide hexagon opacity
    click all shelters
    click basic shelters
    click short term_shelters
    click wide area shelters
    return from seismic card
    log out

Library events with KC user
    [Documentation]     Test to validate the card appear correctly under Library. Validate if the layer functions works on the event when we open one.
    log in                      kcusername      kcpassword
    click library
    click card with title       kc-auto-
    click map display
    click show satellite
    click show map
    click map display
    slide hexagon opacity
    click all shelters
    click basic shelters
    click short term_shelters
    click wide area shelters
    return from seismic card
    log out

Library events with Nagano user
    [Documentation]     Test to validate the card appear correctly under Library. Validate if the layer functions works on the event when we open one.  
    log in                      naganousername      naganopassword
    click library
    click card with title       nagano-auto-
    click map display
    click show satellite
    click show map
    click map display
    slide hexagon opacity
    click all shelters
    click basic shelters
    click short term_shelters
    click wide area shelters
    return from seismic card
    log out

Library events with Okayama user 
    [Documentation]     Test to validate the card appear correctly under Library. Validate if the layer functions works on the event when we open one.  
    log in                      okayamausername      okayamapassword
    click library
    click card with title       okayama-auto-
    click map display
    click show satellite
    click show map
    click map display
    slide hexagon opacity
    click all shelters
    click basic shelters
    click short term_shelters
    click wide area shelters
    return from seismic card
    log out

Library events with Okazaki user
    [Documentation]     Test to validate the card appear correctly under Library. Validate if the layer functions works on the event when we open one.  
    log in   okazakiusername      okazakipassword
    click library
    click card with title       okazaki-auto-
    click map display
    click show satellite
    click show map
    click map display
    slide hexagon opacity
    click all shelters
    click basic shelters
    click short term_shelters
    click wide area shelters
    return from seismic card
    log out



