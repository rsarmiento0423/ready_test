"""This little library is to help debugging Robot scripts.
    The library drops a python debugger as soon as the test fails
"""
#pylint: disable=W0125
#pylint: disable=R1721
import os
import pprint
import sys
import pdb
from robot.libraries.BuiltIn import BuiltIn


#For mac user might receive some error saying that can't load the lib _tkinter
#Then the user needs to install >> brew install python-tk


#Below are the libs for the Kubernetes sections#####
#import yaml

class DebugLib():
    """DebugLib class"""

    @staticmethod
    def insert_env_variable(variable,value):
        '''Can insert enviroment variable at moment of execution.
            Example is to use Test Setup inside robot tests like:
            Test Setup          insert env variable     ROBOT_DEBUG         TRUE
        '''
        #os.environ[variable] = [value]
        #import sys, pdb; pdb.Pdb(stdout=sys.__stdout__).set_trace()
        os.putenv(variable,value)

    ###Below is the debuglirary.
    ###To run in debug mode:
    #Windows
    #$Env:ROBOT_DEBUG = "TRUE"; robot -d output .

    #Linux/OSX
    #ROBOT_DEBUG=TRUE && robot -d output .
    ## OR direct create the env variable
    # export ROBOT_DEBUG=TRUE

    ###To run robot keywords inside the pdb, on terminal use:
    #BuiltIn().(robot keywords replacing _ in spaces)

    def __init__(self):
        """default to not import libs."""
        self.__imported_required_libraries = False

    # Let's us call 'Set Breakpoint' anyhwere in our robot framework code.
    # Will drop to `pdb` at which point we can run anything we like from python interpreter
    def set_breakpoint(self):
        """If it is in debug mode this will drop pdb inside terminal."""
        if self.__is_debug_mode():
            pdb.Pdb(stdout=sys.__stdout__).set_trace()

    # Can be performed on 'teardown'. Pauses using the Dialog library only if a
    # task has failed (SUITE_STATUS is set to 'FAIL')
    def pause_on_failure(self):
        """This will pause the test on a failure and throw a warning on the screen."""
        has_failed = BuiltIn().get_variable_value("${SUITE_STATUS}") == 'FAIL'
        if self.__is_debug_mode and has_failed:
            self.__import_required_libraries()
            BuiltIn().run_keyword(
                "Pause Execution", "Paused due to task failure, click OK to continue teardown")

    # Lets us pause using the Dialog library without dropping to `pdb`
    def pause_for_debug(self):
        """This will pause the test for debugging it."""
        if self.__is_debug_mode:
            self.__import_required_libraries()
            BuiltIn().run_keyword(
                "Pause Execution", "Paused execution for debugging, click OK to continue")
            #self.set_breakpoint()

    # Helper for letting us print out the current variables inside of `pdb`
    # Ex. `self.__print_variables()`
    @staticmethod
    def print_variables():
        """This will print all the variables the sessions has."""
        variables = {k: v for k, v in BuiltIn().get_variables().items()}
        pprint.pprint(variables)

    # Helper for letting us print out the environment variables inside of `pdb`
    # Ex. `self.__print_envs()`
    @staticmethod
    def print_envs():
        """This will print all the enviroment variables the session has."""
        variables = {k: v for k, v in os.environ.items()}
        pprint.pprint(variables)

    # Returns true when we are in development mode, ie. the ROBOT_DEBUG env is set to TRUE
    # This prevents us from accidentally setting a breakpoint and launching it in production
    @staticmethod
    def __is_debug_mode():
        """Checks if the sessions is in debug mode."""
        #import sys, pdb; pdb.Pdb(stdout=sys.__stdout__).set_trace()
        return os.environ['ROBOT_DEBUG'] == 'TRUE'

    # In order to use "Pause Execution" we need to import Dialog
    def __import_required_libraries(self):
        """This will import the required libraries when needed."""
        if not self.__imported_required_libraries:
            BuiltIn().import_library("Dialogs")
            self.__imported_required_libraries = True

    # To use Selenium Library inside the debugger.
    def selib(self, *args):
        """This will bring the Selenium Library to be executed while the test is paused."""
        #needs to return the success message of the click
        if not self.__imported_required_libraries:
            BuiltIn().import_library("SeleniumLibrary")
            BuiltIn().run_keyword(*args)

    # To use the RequestsLibrary inside the debugger:
    def requests(self,*args):
        """This will bring the Requests lib to be executed while the test is being exeuted."""
        if not self.__imported_required_libraries:
            BuiltIn().import_library("RequestsLibrary")
            BuiltIn().run_keyword(*args)
