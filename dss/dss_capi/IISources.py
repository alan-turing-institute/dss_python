'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class IISources(Base):
    __slots__ = []

    @property
    def AllNames(self):
        '''(read-only) Array of strings containing names of all ISOURCE elements.'''
        return self.get_string_array(self.lib.ISources_Get_AllNames)

    @property
    def Amps(self):
        '''Magnitude of the ISOURCE in amps'''
        return self.lib.ISources_Get_Amps()

    @Amps.setter
    def Amps(self, Value):
        self.lib.ISources_Set_Amps(Value)

    @property
    def AngleDeg(self):
        '''Phase angle for ISOURCE, degrees'''
        return self.lib.ISources_Get_AngleDeg()

    @AngleDeg.setter
    def AngleDeg(self, Value):
        self.lib.ISources_Set_AngleDeg(Value)

    @property
    def Count(self):
        '''(read-only) Count: Number of ISOURCE elements.'''
        return self.lib.ISources_Get_Count()

    def __len__(self):
        return self.lib.ISources_Get_Count()

    @property
    def First(self):
        '''(read-only) Set the First ISOURCE to be active; returns Zero if none.'''
        return self.lib.ISources_Get_First()

    @property
    def Frequency(self):
        '''The present frequency of the ISOURCE, Hz'''
        return self.lib.ISources_Get_Frequency()

    @Frequency.setter
    def Frequency(self, Value):
        self.lib.ISources_Set_Frequency(Value)

    @property
    def Name(self):
        '''
        (read) Get name of active ISOURCE
        (write) Set Active ISOURCE by name
        '''
        return self.get_string(self.lib.ISources_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self.api_util.codec)

        self.lib.ISources_Set_Name(Value)

    @property
    def Next(self):
        '''(read-only) Sets the next ISOURCE element to be the active one. Returns Zero if no more.'''
        return self.lib.ISources_Get_Next()

    def __iter__(self):
        idx = self.First
        while idx != 0:
            yield self
            idx = self.Next