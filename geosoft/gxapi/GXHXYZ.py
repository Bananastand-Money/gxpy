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
class GXHXYZ:
    """
    GXHXYZ class.

    High Performance Data Point Storage. This is used
    to put Point data on a DAP server. It is compressed
    and uses a Quad-Tree design to allow very high speed
    data extraction. It is also multi-threaded.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapHXYZ(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXHXYZ`
        
        :returns: A null `GXHXYZ`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXHXYZ` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXHXYZ`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def create(cls, name):
        """
        Create a handle to an `GXHXYZ <geosoft.gxapi.GXHXYZ>` object
        
        :param name:  File Name
        :type  name:  str

        :returns:     `GXHXYZ <geosoft.gxapi.GXHXYZ>` Object
        :rtype:       GXHXYZ

        .. versionadded:: 5.1.3
        """
        ret_val = gxapi_cy.WrapHXYZ.create(GXContext._get_tls_geo(), name.encode())
        return GXHXYZ(ret_val)






    def get_meta(self, meta):
        """
        Get the metadata of a grid.
        
        :param meta:  `GXMETA <geosoft.gxapi.GXMETA>` object to save `GXHXYZ <geosoft.gxapi.GXHXYZ>`'s meta to
        :type  meta:  GXMETA

        .. versionadded:: 5.1.3
        """
        self._wrapper.get_meta(meta._wrapper)
        



    @classmethod
    def h_create_db(cls, db, gvv, name):
        """
        Make an `GXHXYZ <geosoft.gxapi.GXHXYZ>` from GDB
        
        :param db:    `GXDB <geosoft.gxapi.GXDB>` handle
        :param gvv:   `GXVV <geosoft.gxapi.GXVV>` of channels to export
        :param name:  Name of `GXHXYZ <geosoft.gxapi.GXHXYZ>` object
        :type  db:    GXDB
        :type  gvv:   GXVV
        :type  name:  str

        :returns:     `GXHXYZ <geosoft.gxapi.GXHXYZ>` object
        :rtype:       GXHXYZ

        .. versionadded:: 5.1.5
        """
        ret_val = gxapi_cy.WrapHXYZ.h_create_db(GXContext._get_tls_geo(), db._wrapper, gvv._wrapper, name.encode())
        return GXHXYZ(ret_val)



    @classmethod
    def h_create_sql(cls, template, x, y, z, ipj, name):
        """
        Make an `GXHXYZ <geosoft.gxapi.GXHXYZ>` from SQL Query
        
        :param template:  Template File Name
        :param x:         X field name
        :param y:         Y field name
        :param z:         Z field name
        :param ipj:       Projection of data values
        :param name:      Name of `GXHXYZ <geosoft.gxapi.GXHXYZ>` object
        :type  template:  str
        :type  x:         str
        :type  y:         str
        :type  z:         str
        :type  ipj:       GXIPJ
        :type  name:      str

        :returns:         `GXHXYZ <geosoft.gxapi.GXHXYZ>` object
        :rtype:           GXHXYZ

        .. versionadded:: 5.1.3
        """
        ret_val = gxapi_cy.WrapHXYZ.h_create_sql(GXContext._get_tls_geo(), template.encode(), x.encode(), y.encode(), z.encode(), ipj._wrapper, name.encode())
        return GXHXYZ(ret_val)




    def set_meta(self, meta):
        """
        Set the metadata of a grid.
        
        :param meta:  `GXMETA <geosoft.gxapi.GXMETA>` object to add to `GXHXYZ <geosoft.gxapi.GXHXYZ>`'s meta
        :type  meta:  GXMETA

        .. versionadded:: 5.1.3
        """
        self._wrapper.set_meta(meta._wrapper)
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer