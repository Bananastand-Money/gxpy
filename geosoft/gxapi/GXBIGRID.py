### extends 'class_empty.py'
### block ClassImports
# NOTICE: Do not edit anything here, it is generated code
from . import gxapi_cy
from geosoft.gxapi import GXContext, float_ref, int_ref, str_ref


### endblock ClassImports

### block Header
# NOTICE: The code generator will not replace the code in this block
### endblock Header

### block ClassImplementation
# NOTICE: Do not edit anything here, it is generated code
class GXBIGRID:
    """
    GXBIGRID class.

    The Bigrid class is used to grid data using a optimized algorithm that
    assumes data is collected in semi-straight lines.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapBIGRID(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXBIGRID`
        
        :returns: A null `GXBIGRID`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXBIGRID` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXBIGRID`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous



    def clear(self):
        """
        Clears all the parameters in a `GXBIGRID <geosoft.gxapi.GXBIGRID>` object
        

        .. versionadded:: 5.0
        """
        self._wrapper.clear()
        



    @classmethod
    def create(cls):
        """
        Create a handle to a Bigrid object
        

        :returns:    `GXBIGRID <geosoft.gxapi.GXBIGRID>` Object
        :rtype:      GXBIGRID

        .. versionadded:: 5.0

        **Note:**

        The Bigrid object is initially empty. It will store the
        control file parameters which the Bigrid program needs
        to execute. Use the LoadParms_BIGRID method to get the
        control file parameters into the `GXBIGRID <geosoft.gxapi.GXBIGRID>` object.
        """
        ret_val = gxapi_cy.WrapBIGRID.create(GXContext._get_tls_geo())
        return GXBIGRID(ret_val)






    def load_parms(self, file):
        """
        Retrieves a Bigrid object's control parameters from a file,
        or sets the parameters to default if the file doesn't exist.
        
        :param file:    Name of file to get the parameter settings from
        :type  file:    str

        :returns:       0 - Ok
                        1 - Error
        :rtype:         int

        .. versionadded:: 5.0

        **Note:**

        If the control file name passed into this function is a file
        which does not exist, then the defaults for a Bigrid control
        file will be generated and put into the `GXBIGRID <geosoft.gxapi.GXBIGRID>` object.
        Otherwise, the control file's settings are retrieved from
        the file and loaded into the `GXBIGRID <geosoft.gxapi.GXBIGRID>` object.
        """
        ret_val = self._wrapper.load_parms(file.encode())
        return ret_val




    def load_warp(self, title, cell, warp):
        """
        Load a warp projection.
        
        :param title:   New grid title
        :param cell:    New grid cell size as a string, blank for default
        :param warp:    Warp projection file name
        :type  title:   str
        :type  cell:    str
        :type  warp:    str

        :returns:       0 - Ok
                        1 - Error
        :rtype:         int

        .. versionadded:: 5.0
        """
        ret_val = self._wrapper.load_warp(title.encode(), cell.encode(), warp.encode())
        return ret_val




    def run(self, zchan, in_dat, out_dat):
        """
        Executes the Bigrid program, using the input channel and
        output file parameters.
        
        :param zchan:    Not used, pass as ""
        :param in_dat:   Handle to source `GXDAT <geosoft.gxapi.GXDAT>` object (from database)
        :param out_dat:  Handle to output grid file `GXDAT <geosoft.gxapi.GXDAT>`
        :type  zchan:    str
        :type  in_dat:   GXDAT
        :type  out_dat:  GXDAT

        .. versionadded:: 5.0
        """
        self._wrapper.run(zchan.encode(), in_dat._wrapper, out_dat._wrapper)
        




    def run2(self, zchan, in_dat, out_dat, ipj):
        """
        Executes the Bigrid program, using the input channel and
        output file parameters with a projection handle.
        
        :param zchan:    Not used, pass as ""
        :param in_dat:   Handle to source `GXDAT <geosoft.gxapi.GXDAT>` object (from database)
        :param out_dat:  Handle to output grid file `GXDAT <geosoft.gxapi.GXDAT>`
        :param ipj:      `GXIPJ <geosoft.gxapi.GXIPJ>` handle of the projection system
        :type  zchan:    str
        :type  in_dat:   GXDAT
        :type  out_dat:  GXDAT
        :type  ipj:      GXIPJ

        .. versionadded:: 6.3
        """
        self._wrapper.run2(zchan.encode(), in_dat._wrapper, out_dat._wrapper, ipj._wrapper)
        




    def save_parms(self, name):
        """
        Puts the Bigrid object's control parameters back into
        its control file.
        
        :param name:    Name of file to put the parameter settings into
        :type  name:    str

        .. versionadded:: 5.0

        **Note:**

        If the control file did not previously exist, it will be
        created. Otherwise, the old file will be overwritten.
        """
        self._wrapper.save_parms(name.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer