'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class ILoadShapes(Base):
    __slots__ = []

    def New(self, Name):
        if type(Name) is not bytes:
            Name = Name.encode(self.api_util.codec)

        return self.lib.LoadShapes_New(Name)

    def Normalize(self):
        self.lib.LoadShapes_Normalize()

    @property
    def AllNames(self):
        '''(read-only) Array of strings containing names of all Loadshape objects currently defined.'''
        return self.get_string_array(self.lib.LoadShapes_Get_AllNames)

    @property
    def Count(self):
        '''(read-only) Number of Loadshape objects currently defined in Loadshape collection'''
        return self.lib.LoadShapes_Get_Count()

    def __len__(self):
        return self.lib.LoadShapes_Get_Count()

    @property
    def First(self):
        '''(read-only) Set the first loadshape active and return integer index of the loadshape. Returns 0 if none.'''
        return self.lib.LoadShapes_Get_First()

    @property
    def HrInterval(self):
        '''Fixed interval time value, hours.'''
        return self.lib.LoadShapes_Get_HrInterval()

    @HrInterval.setter
    def HrInterval(self, Value):
        self.lib.LoadShapes_Set_HrInterval(Value)

    @property
    def MinInterval(self):
        '''Fixed Interval time value, in minutes'''
        return self.lib.LoadShapes_Get_MinInterval()

    @MinInterval.setter
    def MinInterval(self, Value):
        self.lib.LoadShapes_Set_MinInterval(Value)

    @property
    def Name(self):
        '''
        (read) Get the Name of the active Loadshape
        (write) Set the active Loadshape by name
        '''
        return self.get_string(self.lib.LoadShapes_Get_Name())

    @Name.setter
    def Name(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self.api_util.codec)

        self.lib.LoadShapes_Set_Name(Value)

    @property
    def Next(self):
        '''(read-only) Advance active Loadshape to the next on in the collection. Returns 0 if no more loadshapes.'''
        return self.lib.LoadShapes_Get_Next()

    @property
    def Npts(self):
        '''
        (read) Get Number of points in active Loadshape.
        (write) Set number of points to allocate for active Loadshape.
        '''
        return self.lib.LoadShapes_Get_Npts()

    @Npts.setter
    def Npts(self, Value):
        self.lib.LoadShapes_Set_Npts(Value)

    @property
    def PBase(self):
        return self.lib.LoadShapes_Get_PBase()

    @PBase.setter
    def PBase(self, Value):
        self.lib.LoadShapes_Set_PBase(Value)

    Pbase = PBase

    @property
    def Pmult(self):
        '''
        (read) Array of Doubles for the P multiplier in the Loadshape.
        (write) Array of doubles containing the P array for the Loadshape.
        '''
        self.lib.LoadShapes_Get_Pmult_GR()
        return self.get_float64_gr_array()

    @Pmult.setter
    def Pmult(self, Value):
        Value, ValuePtr, ValueCount = self.prepare_float64_array(Value)
        self.lib.LoadShapes_Set_Pmult(ValuePtr, ValueCount)

    @property
    def QBase(self):
        '''Base for normalizing Q curve. If left at zero, the peak value is used.'''
        return self.lib.LoadShapes_Get_Qbase()

    @QBase.setter
    def QBase(self, Value):
        self.lib.LoadShapes_Set_Qbase(Value)

    Qbase = QBase

    @property
    def Qmult(self):
        '''Array of doubles containing the Q multipliers.'''
        self.lib.LoadShapes_Get_Qmult_GR()
        return self.get_float64_gr_array()

    @Qmult.setter
    def Qmult(self, Value):
        Value, ValuePtr, ValueCount = self.prepare_float64_array(Value)
        self.lib.LoadShapes_Set_Qmult(ValuePtr, ValueCount)

    @property
    def TimeArray(self):
        '''Time array in hours correscponding to P and Q multipliers when the Interval=0.'''
        self.lib.LoadShapes_Get_TimeArray_GR()
        return self.get_float64_gr_array()

    @TimeArray.setter
    def TimeArray(self, Value):
        Value, ValuePtr, ValueCount = self.prepare_float64_array(Value)
        self.lib.LoadShapes_Set_TimeArray(ValuePtr, ValueCount)

    @property
    def UseActual(self):
        '''T/F flag to let Loads know to use the actual value in the curve rather than use the value as a multiplier.'''
        return self.lib.LoadShapes_Get_UseActual() != 0

    @UseActual.setter
    def UseActual(self, Value):
        self.lib.LoadShapes_Set_UseActual(Value)

    @property
    def sInterval(self):
        return self.lib.LoadShapes_Get_sInterval()

    @sInterval.setter
    def sInterval(self, Value):
        self.lib.LoadShapes_Set_Sinterval(Value)

    Sinterval = sInterval

    def __iter__(self):
        idx = self.First
        while idx != 0:
            yield self
            idx = self.Next
