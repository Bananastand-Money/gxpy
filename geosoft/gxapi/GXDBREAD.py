### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref
from .GXVA import GXVA
from .GXVV import GXVV


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXDBREAD:
    """
    GXDBREAD class.

    The `GXDBREAD <geosoft.gxapi.GXDBREAD>` class is used to open and read from databases. Very large lines
    are split into blocks and served up sequentially to prevent the over-use of virtual memory when channels are read into VVs or VAs.
    Individual data blocks are limited by default to 1 MB (which is user-alterable). Single lines smaller than the block size
    are served up whole, one block per line.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapDBREAD(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXDBREAD`
        
        :returns: A null `GXDBREAD`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXDBREAD` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXDBREAD`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Create Methods


    @classmethod
    def create(cls, db, line_lst):
        """
        Create a `GXDBREAD <geosoft.gxapi.GXDBREAD>` object
        Add channels using the `add_channel <geosoft.gxapi.GXDBREAD.add_channel>` method.channel.
        
        :param db:        Database input
        :param line_lst:  List of lines to process NAME = line name, VALUE = line symbol
        :type  db:        GXDB
        :type  line_lst:  GXLST

        :returns:         `GXDBREAD <geosoft.gxapi.GXDBREAD>` object
        :rtype:           GXDBREAD

        .. versionadded:: 8.5
        """
        ret_val = gxapi_cy.WrapDBREAD.create(GXContext._get_tls_geo(), db._wrapper, line_lst._wrapper)
        return GXDBREAD(ret_val)



    @classmethod
    def create_xy(cls, db, line_lst):
        """
        Create a `GXDBREAD <geosoft.gxapi.GXDBREAD>` object for a XY-located data. Add channels using the
        `add_channel <geosoft.gxapi.GXDBREAD.add_channel>` method.
        
        :param db:        Database input
        :param line_lst:  List of lines to process NAME = line name, VALUE = line symbol
        :type  db:        GXDB
        :type  line_lst:  GXLST

        :returns:         `GXDBREAD <geosoft.gxapi.GXDBREAD>` object
        :rtype:           GXDBREAD

        .. versionadded:: 8.5
        """
        ret_val = gxapi_cy.WrapDBREAD.create_xy(GXContext._get_tls_geo(), db._wrapper, line_lst._wrapper)
        return GXDBREAD(ret_val)



    @classmethod
    def create_xyz(cls, db, line_lst):
        """
        Create a `GXDBREAD <geosoft.gxapi.GXDBREAD>` object for a XYZ-located data.
        Add channels using the `add_channel <geosoft.gxapi.GXDBREAD.add_channel>` method.
        
        :param db:        Database input
        :param line_lst:  List of lines to process NAME = line name, VALUE = line symbol
        :type  db:        GXDB
        :type  line_lst:  GXLST

        :returns:         `GXDBREAD <geosoft.gxapi.GXDBREAD>` object
        :rtype:           GXDBREAD

        .. versionadded:: 8.5
        """
        ret_val = gxapi_cy.WrapDBREAD.create_xyz(GXContext._get_tls_geo(), db._wrapper, line_lst._wrapper)
        return GXDBREAD(ret_val)






    def add_channel(self, chan):
        """
        Add a data channel to the `GXDBREAD <geosoft.gxapi.GXDBREAD>` object.
        
        :param chan:    Channel handle (does not need to be locked, but can be.)
        :type  chan:    int

        :returns:       Channel index. Use for getting the correct `GXVV <geosoft.gxapi.GXVV>` or `GXVA <geosoft.gxapi.GXVA>` object.
        :rtype:         int

        .. versionadded:: 8.5
        """
        ret_val = self._wrapper.add_channel(chan)
        return ret_val




# Data Access Methods



    def get_vv(self, chan):
        """
        Get the `GXVV <geosoft.gxapi.GXVV>` handle for a channel.
        
        :param chan:    Index of channel to access.
        :type  chan:    int

        :returns:       `GXVV <geosoft.gxapi.GXVV>` handle
        :rtype:         GXVV

        .. versionadded:: 8.5

        **Note:**

        Call only for single-column (regular) channels. You can call the `get_chan_array_size <geosoft.gxapi.GXDBREAD.get_chan_array_size>`
        function to find the number fo columns in a given channel. The `GXVV <geosoft.gxapi.GXVV>` is filled anew for 
        each block served up.
        """
        ret_val = self._wrapper.get_vv(chan)
        return GXVV(ret_val)




    def get_va(self, chan):
        """
        Get the `GXVA <geosoft.gxapi.GXVA>` handle for an array channel.
        
        :param chan:    Index of channel to access.
        :type  chan:    int

        :returns:       `GXVA <geosoft.gxapi.GXVA>` handle
        :rtype:         GXVA

        .. versionadded:: 8.5

        **Note:**

        Call only for array (multi-column) channels. You can call the `get_chan_array_size <geosoft.gxapi.GXDBREAD.get_chan_array_size>`
        function to find the number fo columns in a given channel, or you can call `GXVA.col <geosoft.gxapi.GXVA.col>` on the returned `GXVA <geosoft.gxapi.GXVA>` handle.
        The `GXVA <geosoft.gxapi.GXVA>` is filled anew for each block served up.
        """
        ret_val = self._wrapper.get_va(chan)
        return GXVA(ret_val)




    def get_v_vx(self):
        """
        Get the X channel `GXVV <geosoft.gxapi.GXVV>` handle.
        

        :returns:       `GXVV <geosoft.gxapi.GXVV>` handle
        :rtype:         GXVV

        .. versionadded:: 8.5

        **Note:**

        Only available for the CreateXY or CreateXYZ methods.
        The `GXVV <geosoft.gxapi.GXVV>` is filled anew for each block served up.
        """
        ret_val = self._wrapper.get_v_vx()
        return GXVV(ret_val)




    def get_v_vy(self):
        """
        Get the Y channel `GXVV <geosoft.gxapi.GXVV>` handle.
        

        :returns:       `GXVV <geosoft.gxapi.GXVV>` handle
        :rtype:         GXVV

        .. versionadded:: 8.5

        **Note:**

        Only available for the CreateXY or CreateXYZ methods.
        The `GXVV <geosoft.gxapi.GXVV>` is filled anew for each block served up.
        """
        ret_val = self._wrapper.get_v_vy()
        return GXVV(ret_val)




    def get_v_vz(self):
        """
        Get the Z channel `GXVV <geosoft.gxapi.GXVV>` handle.
        

        :returns:       `GXVV <geosoft.gxapi.GXVV>` handle
        :rtype:         GXVV

        .. versionadded:: 8.5

        **Note:**

        Only available for the CreateXY or CreateXYZ methods.
        The `GXVV <geosoft.gxapi.GXVV>` is filled anew for each block served up.
        If the Z channel is an array channel, the returned `GXVV <geosoft.gxapi.GXVV>` is the "base" `GXVV <geosoft.gxapi.GXVV>` of the `GXVA <geosoft.gxapi.GXVA>` and contains all items sequentially.
        """
        ret_val = self._wrapper.get_v_vz()
        return GXVV(ret_val)




    def get_chan_array_size(self, chan):
        """
        Get the number of columns of data in a channel.
        
        :param chan:    Index of channel to access.
        :type  chan:    int

        :returns:       The number of columns (array size) for a channel
        :rtype:         int

        .. versionadded:: 8.5

        **Note:**

        Regular channels have one column of data. Array channels have more than one column of data.
        This function should be called to determine whether to use `get_vv <geosoft.gxapi.GXDBREAD.get_vv>` or `get_va <geosoft.gxapi.GXDBREAD.get_va>` to access data
        for a channel.
        """
        ret_val = self._wrapper.get_chan_array_size(chan)
        return ret_val




    def get_number_of_blocks_to_process(self):
        """
        Get the number of blocks to be served up.
        

        :returns:       The number of blocks to process in the selected lines.
        :rtype:         int

        .. versionadded:: 8.5

        **Note:**

        The selected lines are scanned. All lines where the served up data is less than the maximum block size for
        all channels are served as a single block. Any lines where any channel's data exceeds the maximum block size are split up into blocks.
        The value returned can be used as the progress message maximum iteration value.
        """
        ret_val = self._wrapper.get_number_of_blocks_to_process()
        return ret_val




# Processing



    def get_next_block(self, line, block, n_blocks):
        """
        Get the next block of data.
        
        :param line:      (returned) The index into the input selected line list of the line whose data is contained in the current block
        :param block:     (returned) The block index (0 to NBlocks-1) for the current line of data.
        :param n_blocks:  (returned) The number of blocks that the current line is split into.
        :type  line:      int_ref
        :type  block:     int_ref
        :type  n_blocks:  int_ref

        :returns:         Returns the current block index, or -1 if at end of file (no new data returned).
        :rtype:           int

        .. versionadded:: 8.5

        **Note:**

        The next block of data is read and copied into the channel `GXVV <geosoft.gxapi.GXVV>` and/or `GXVA <geosoft.gxapi.GXVA>` objects, accessed using
        the `get_vv <geosoft.gxapi.GXDBREAD.get_vv>` and `get_va <geosoft.gxapi.GXDBREAD.get_va>` functions.
        """
        ret_val, line.value, block.value, n_blocks.value = self._wrapper.get_next_block(line.value, block.value, n_blocks.value)
        return ret_val





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer