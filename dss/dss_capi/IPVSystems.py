'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class IPVSystems(Base):
    __slots__ = []

    @property
    def AllNames(self):
        '''(read-only) Vairant array of strings with all PVSystem names'''
        return self.get_string_array(self.lib.PVSystems_Get_AllNames)

    @property
    def Count(self):
        '''(read-only) Number of PVSystems'''
        return self.lib.PVSystems_Get_Count()

    def __len__(self):
        return self.lib.PVSystems_Get_Count()

    @property
    def First(self):
        '''(read-only) Set first PVSystem active; returns 0 if none.'''
        return self.lib.PVSystems_Get_First()

    @property
    def Irradiance(self):
        '''
        (read) Get the present value of the Irradiance property in W/sq-m
        (write) Set the present Irradiance value in W/sq-m
        '''
        return self.lib.PVSystems_Get_Irradiance()

    @Irradiance.setter
    def Irradiance(self, Value):
        self.lib.PVSystems_Set_Irradiance(Value)

    @property
    def Name(self):
        '''
        (read) Get the name of the active PVSystem
        (write) Set the name of the active PVSystem
        '''
        return self.get_string(self.lib.PVSystems_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self.api_util.codec)

        self.lib.PVSystems_Set_Name(Value)

    @property
    def Next(self):
        '''(read-only) Sets next PVSystem active; returns 0 if no more.'''
        return self.lib.PVSystems_Get_Next()

    @property
    def PF(self):
        '''
        (read) Get Power factor
        (write) Set PF
        '''
        return self.lib.PVSystems_Get_PF()

    @PF.setter
    def PF(self, Value):
        self.lib.PVSystems_Set_PF(Value)

    @property
    def RegisterNames(self):
        '''(read-only) Variant Array of PVSYSTEM energy meter register names'''
        return self.get_string_array(self.lib.PVSystems_Get_RegisterNames)

    @property
    def RegisterValues(self):
        '''(read-only) Array of doubles containing values in PVSystem registers.'''
        self.lib.PVSystems_Get_RegisterValues_GR()
        return self.get_float64_gr_array()

    @property
    def idx(self):
        '''
        (read) Get/set active PVSystem by index;  1..Count
        (write) Get/Set Active PVSystem by index:  1.. Count
        '''
        return self.lib.PVSystems_Get_idx()

    @idx.setter
    def idx(self, Value):
        self.lib.PVSystems_Set_idx(Value)

    @property
    def kVArated(self):
        '''
        (read) Get Rated kVA of the PVSystem
        (write) Set kva rated
        '''
        return self.lib.PVSystems_Get_kVArated()

    @kVArated.setter
    def kVArated(self, Value):
        self.lib.PVSystems_Set_kVArated(Value)

    @property
    def kW(self):
        '''(read-only) get kW output'''
        return self.lib.PVSystems_Get_kW()

    @property
    def kvar(self):
        '''
        (read) Get kvar value
        (write) Set kvar output value
        '''
        return self.lib.PVSystems_Get_kvar()

    @kvar.setter
    def kvar(self, Value):
        self.lib.PVSystems_Set_kvar(Value)

    def __iter__(self):
        idx = self.First
        while idx != 0:
            yield self
            idx = self.Next
