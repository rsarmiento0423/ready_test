*** Settings ***
Documentation   Ready Staging Flood Tests
Library    ReadyHelpPage     ${ENVFILE}     ${BROWSER}      ${URL}
Default Tags    Ready     Staging     Sanity    Help    




*** Test Cases ***
Log in and verify the help page works correctly
    log in  chibausername      chibapassword
    click help
    validate footer social links
    verify_help_page
    search_for_article_name     Flood Map
    validate_actions_on_intercom_msg
