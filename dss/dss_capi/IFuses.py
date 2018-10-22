'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class IFuses(Base):
    __slots__ = []

    def Close(self):
        self.lib.Fuses_Close()

    def IsBlown(self):
        return self.lib.Fuses_IsBlown() != 0

    def Open(self):
        self.lib.Fuses_Open()

    @property
    def AllNames(self):
        '''(read-only) Array of strings containing names of all Fuses in the circuit'''
        return self.get_string_array(self.lib.Fuses_Get_AllNames)

    @property
    def Count(self):
        '''(read-only) Number of Fuse elements in the circuit'''
        return self.lib.Fuses_Get_Count()

    def __len__(self):
        return self.lib.Fuses_Get_Count()

    @property
    def Delay(self):
        '''
        (read) A fixed delay time in seconds added to the fuse blowing time determined by the TCC curve. Default is 0.
        (write) Fixed delay time in seconds added to the fuse blowing time to represent fuse clear or other delay.
        '''
        return self.lib.Fuses_Get_Delay()

    @Delay.setter
    def Delay(self, Value):
        self.lib.Fuses_Set_Delay(Value)

    @property
    def First(self):
        '''(read-only) Set the first Fuse to be the active fuse. Returns 0 if none.'''
        return self.lib.Fuses_Get_First()

    @property
    def MonitoredObj(self):
        '''Full name of the circuit element to which the fuse is connected.'''
        return self.get_string(self.lib.Fuses_Get_MonitoredObj())

    @MonitoredObj.setter
    def MonitoredObj(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self.api_util.codec)

        self.lib.Fuses_Set_MonitoredObj(Value)

    @property
    def MonitoredTerm(self):
        '''
        (read) Terminal number to which the fuse is connected.
        (write) Number of the terminal to which the fuse is connected
        '''
        return self.lib.Fuses_Get_MonitoredTerm()

    @MonitoredTerm.setter
    def MonitoredTerm(self, Value):
        self.lib.Fuses_Set_MonitoredTerm(Value)

    @property
    def Name(self):
        '''
        (read) Get the name of the active Fuse element
        (write) Set the active Fuse element by name.
        '''
        return self.get_string(self.lib.Fuses_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self.api_util.codec)

        self.lib.Fuses_Set_Name(Value)

    @property
    def Next(self):
        '''(read-only) Advance the active Fuse element pointer to the next fuse. Returns 0 if no more fuses.'''
        return self.lib.Fuses_Get_Next()

    @property
    def NumPhases(self):
        '''(read-only) Number of phases, this fuse. '''
        return self.lib.Fuses_Get_NumPhases()

    @property
    def RatedCurrent(self):
        '''
        (read) Multiplier or actual amps for the TCCcurve object. Defaults to 1.0.  Multipliy current values of TCC curve by this to get actual amps.
        (write) Multiplier or actual fuse amps for the TCC curve. Defaults to 1.0. Has to correspond to the Current axis of TCCcurve object.
        '''
        return self.lib.Fuses_Get_RatedCurrent()

    @RatedCurrent.setter
    def RatedCurrent(self, Value):
        self.lib.Fuses_Set_RatedCurrent(Value)

    @property
    def SwitchedObj(self):
        '''
        (read) Full name of the circuit element switch that the fuse controls. Defaults to the MonitoredObj.
        (write) Full name of the circuit element switch that the fuse controls. Defaults to MonitoredObj.
        '''
        return self.get_string(self.lib.Fuses_Get_SwitchedObj())

    @SwitchedObj.setter
    def SwitchedObj(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self.api_util.codec)

        self.lib.Fuses_Set_SwitchedObj(Value)

    @property
    def SwitchedTerm(self):
        '''
        (read) Number of the terminal containing the switch controlled by the fuse.
        (write) Number of the terminal of the controlled element containing the switch controlled by the fuse.
        '''
        return self.lib.Fuses_Get_SwitchedTerm()

    @SwitchedTerm.setter
    def SwitchedTerm(self, Value):
        self.lib.Fuses_Set_SwitchedTerm(Value)

    @property
    def TCCcurve(self):
        '''Name of the TCCcurve object that determines fuse blowing.'''
        return self.get_string(self.lib.Fuses_Get_TCCcurve())

    @TCCcurve.setter
    def TCCcurve(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self.api_util.codec)

        self.lib.Fuses_Set_TCCcurve(Value)

    @property
    def idx(self):
        '''
        (read) Get/set active fuse by index into the list of fuses. 1 based: 1..count
        (write) Set Fuse active by index into the list of fuses. 1..count
        '''
        return self.lib.Fuses_Get_idx()

    @idx.setter
    def idx(self, Value):
        self.lib.Fuses_Set_idx(Value)

    def __iter__(self):
        idx = self.First
        while idx != 0:
            yield self
            idx = self.Next

