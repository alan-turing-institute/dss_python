'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class IRegControls(Base):
    __slots__ = []

    def Reset(self):
        self.lib.RegControls_Reset()

    @property
    def AllNames(self):
        '''(read-only) Array of strings containing all RegControl names'''
        return self.get_string_array(self.lib.RegControls_Get_AllNames)

    @property
    def CTPrimary(self):
        '''CT primary ampere rating (secondary is 0.2 amperes)'''
        return self.lib.RegControls_Get_CTPrimary()

    @CTPrimary.setter
    def CTPrimary(self, Value):
        self.lib.RegControls_Set_CTPrimary(Value)

    @property
    def Count(self):
        '''(read-only) Number of RegControl objects in Active Circuit'''
        return self.lib.RegControls_Get_Count()

    def __len__(self):
        return self.lib.RegControls_Get_Count()

    @property
    def Delay(self):
        '''Time delay [s] after arming before the first tap change. Control may reset before actually changing taps.'''
        return self.lib.RegControls_Get_Delay()

    @Delay.setter
    def Delay(self, Value):
        self.lib.RegControls_Set_Delay(Value)

    @property
    def First(self):
        '''(read-only) Sets the first RegControl active. Returns 0 if none.'''
        return self.lib.RegControls_Get_First()

    @property
    def ForwardBand(self):
        '''Regulation bandwidth in forward direciton, centered on Vreg'''
        return self.lib.RegControls_Get_ForwardBand()

    @ForwardBand.setter
    def ForwardBand(self, Value):
        self.lib.RegControls_Set_ForwardBand(Value)

    @property
    def ForwardR(self):
        '''LDC R setting in Volts'''
        return self.lib.RegControls_Get_ForwardR()

    @ForwardR.setter
    def ForwardR(self, Value):
        self.lib.RegControls_Set_ForwardR(Value)

    @property
    def ForwardVreg(self):
        '''Target voltage in the forward direction, on PT secondary base.'''
        return self.lib.RegControls_Get_ForwardVreg()

    @ForwardVreg.setter
    def ForwardVreg(self, Value):
        self.lib.RegControls_Set_ForwardVreg(Value)

    @property
    def ForwardX(self):
        '''LDC X setting in Volts'''
        return self.lib.RegControls_Get_ForwardX()

    @ForwardX.setter
    def ForwardX(self, Value):
        self.lib.RegControls_Set_ForwardX(Value)

    @property
    def IsInverseTime(self):
        '''Time delay is inversely adjsuted, proportinal to the amount of voltage outside the regulating band.'''
        return self.lib.RegControls_Get_IsInverseTime() != 0

    @IsInverseTime.setter
    def IsInverseTime(self, Value):
        self.lib.RegControls_Set_IsInverseTime(Value)

    @property
    def IsReversible(self):
        '''Regulator can use different settings in the reverse direction.  Usually not applicable to substation transformers.'''
        return self.lib.RegControls_Get_IsReversible() != 0

    @IsReversible.setter
    def IsReversible(self, Value):
        self.lib.RegControls_Set_IsReversible(Value)

    @property
    def MaxTapChange(self):
        '''Maximum tap change per iteration in STATIC solution mode. 1 is more realistic, 16 is the default for a faster soluiton.'''
        return self.lib.RegControls_Get_MaxTapChange()

    @MaxTapChange.setter
    def MaxTapChange(self, Value):
        self.lib.RegControls_Set_MaxTapChange(Value)

    @property
    def MonitoredBus(self):
        '''Name of a remote regulated bus, in lieu of LDC settings'''
        return self.get_string(self.lib.RegControls_Get_MonitoredBus())

    @MonitoredBus.setter
    def MonitoredBus(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self.api_util.codec)

        self.lib.RegControls_Set_MonitoredBus(Value)

    @property
    def Name(self):
        '''
        (read) Get/set Active RegControl  name
        (write) Sets a RegControl active by name
        '''
        return self.get_string(self.lib.RegControls_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self.api_util.codec)

        self.lib.RegControls_Set_Name(Value)

    @property
    def Next(self):
        '''(read-only) Sets the next RegControl active. Returns 0 if none.'''
        return self.lib.RegControls_Get_Next()

    @property
    def PTratio(self):
        '''PT ratio for voltage control settings'''
        return self.lib.RegControls_Get_PTratio()

    @PTratio.setter
    def PTratio(self, Value):
        self.lib.RegControls_Set_PTratio(Value)

    @property
    def ReverseBand(self):
        '''Bandwidth in reverse direction, centered on reverse Vreg.'''
        return self.lib.RegControls_Get_ReverseBand()

    @ReverseBand.setter
    def ReverseBand(self, Value):
        self.lib.RegControls_Set_ReverseBand(Value)

    @property
    def ReverseR(self):
        '''Reverse LDC R setting in Volts.'''
        return self.lib.RegControls_Get_ReverseR()

    @ReverseR.setter
    def ReverseR(self, Value):
        self.lib.RegControls_Set_ReverseR(Value)

    @property
    def ReverseVreg(self):
        '''Target voltage in the revese direction, on PT secondary base.'''
        return self.lib.RegControls_Get_ReverseVreg()

    @ReverseVreg.setter
    def ReverseVreg(self, Value):
        self.lib.RegControls_Set_ReverseVreg(Value)

    @property
    def ReverseX(self):
        '''Reverse LDC X setting in volts.'''
        return self.lib.RegControls_Get_ReverseX()

    @ReverseX.setter
    def ReverseX(self, Value):
        self.lib.RegControls_Set_ReverseX(Value)

    @property
    def TapDelay(self):
        '''Time delay [s] for subsequent tap changes in a set. Control may reset before actually changing taps.'''
        return self.lib.RegControls_Get_TapDelay()

    @TapDelay.setter
    def TapDelay(self, Value):
        self.lib.RegControls_Set_TapDelay(Value)

    @property
    def TapNumber(self):
        '''Integer number of the tap that the controlled transformer winding is currentliy on.'''
        return self.lib.RegControls_Get_TapNumber()

    @TapNumber.setter
    def TapNumber(self, Value):
        self.lib.RegControls_Set_TapNumber(Value)

    @property
    def TapWinding(self):
        '''Tapped winding number'''
        return self.lib.RegControls_Get_TapWinding()

    @TapWinding.setter
    def TapWinding(self, Value):
        self.lib.RegControls_Set_TapWinding(Value)

    @property
    def Transformer(self):
        '''Name of the transformer this regulator controls'''
        return self.get_string(self.lib.RegControls_Get_Transformer())

    @Transformer.setter
    def Transformer(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self.api_util.codec)

        self.lib.RegControls_Set_Transformer(Value)

    @property
    def VoltageLimit(self):
        '''First house voltage limit on PT secondary base.  Setting to 0 disables this function.'''
        return self.lib.RegControls_Get_VoltageLimit()

    @VoltageLimit.setter
    def VoltageLimit(self, Value):
        self.lib.RegControls_Set_VoltageLimit(Value)

    @property
    def Winding(self):
        '''Winding number for PT and CT connections'''
        return self.lib.RegControls_Get_Winding()

    @Winding.setter
    def Winding(self, Value):
        self.lib.RegControls_Set_Winding(Value)

    def __iter__(self):
        idx = self.First
        while idx != 0:
            yield self
            idx = self.Next

