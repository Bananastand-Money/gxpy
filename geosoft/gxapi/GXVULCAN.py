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
class GXVULCAN:
    """
    GXVULCAN class.

    The `GXVULCAN <geosoft.gxapi.GXVULCAN>` class is used for importing Maptek® Vulcan block and triangulation files.
    """

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self._wrapper = None

    def __del__(self):
        self._wrapper = None

    def __init__(self, wrapper=None):
        self._wrapper = wrapper if wrapper else gxapi_cy.WrapVULCAN(GXContext._get_tls_geo(), 0)

    @classmethod
    def null(cls):
        """
        A null (undefined) instance of `GXVULCAN`
        
        :returns: A null `GXVULCAN`
        """
        return cls()

    def is_null(self):
        """
        Check if the instance of `GXVULCAN` is null (undefined)`
        
        :returns: True if this is a null (undefined) instance of `GXVULCAN`, False otherwise.
        """
        return self._wrapper.handle == 0

    def _internal_handle(self):
        return self._wrapper.handle


# Miscellaneous


    @classmethod
    def is_valid_triangulation_file(cls, triangulation_file):
        """
        Check if the given file can be opened as a Vulcan triangulation file.
        
        :param triangulation_file:  Triangulation file
        :type  triangulation_file:  str

        :returns:                   0 - No
                                    1 - Yes
        :rtype:                     int

        .. versionadded:: 8.4
        """
        ret_val = gxapi_cy.WrapVULCAN.is_valid_triangulation_file(GXContext._get_tls_geo(), triangulation_file.encode())
        return ret_val



    @classmethod
    def is_valid_block_model_file(cls, block_model_file):
        """
        Check if the given file can be opened as a Vulcan block model file.
        
        :param block_model_file:  Block model file
        :type  block_model_file:  str

        :returns:                 0 - No
                                  1 - Yes
        :rtype:                   int

        .. versionadded:: 8.4
        """
        ret_val = gxapi_cy.WrapVULCAN.is_valid_block_model_file(GXContext._get_tls_geo(), block_model_file.encode())
        return ret_val



    @classmethod
    def triangulation_to_view(cls, triangulation_file, ipj, mview, new_group_name):
        """
        Draw triangle edges in a Vulcan triangulation file to a 3D view in a map.
        
        :param triangulation_file:  Triangulation file
        :param ipj:                 Triangulation projection
        :param mview:               Destination `GXMVIEW <geosoft.gxapi.GXMVIEW>`
        :param new_group_name:      New group name
        :type  triangulation_file:  str
        :type  ipj:                 GXIPJ
        :type  mview:               GXMVIEW
        :type  new_group_name:      str

        .. versionadded:: 8.4
        """
        gxapi_cy.WrapVULCAN.triangulation_to_view(GXContext._get_tls_geo(), triangulation_file.encode(), ipj._wrapper, mview._wrapper, new_group_name.encode())
        



    @classmethod
    def get_block_model_variable_info(cls, block_model_file, query, lst):
        """
        Query a block model for the variable names and descriptions.
        
        :param block_model_file:  Block model file
        :param query:             `BLOCK_MODEL_VARIABLE_TYPE` Which variables to return.
        :param lst:               List used to return variable names/descriptions.
        :type  block_model_file:  str
        :type  query:             int
        :type  lst:               GXLST

        .. versionadded:: 8.4
        """
        gxapi_cy.WrapVULCAN.get_block_model_variable_info(GXContext._get_tls_geo(), block_model_file.encode(), query, lst._wrapper)
        



    @classmethod
    def get_block_model_string_variable_values(cls, block_model_file, variable_name, lst):
        """
        Query a block model for the values a string variable can assume.
        
        :param block_model_file:  Block model file
        :param variable_name:     Variable name
        :param lst:               List used to return variable names
        :type  block_model_file:  str
        :type  variable_name:     str
        :type  lst:               GXLST

        .. versionadded:: 8.4
        """
        gxapi_cy.WrapVULCAN.get_block_model_string_variable_values(GXContext._get_tls_geo(), block_model_file.encode(), variable_name.encode(), lst._wrapper)
        



    @classmethod
    def block_model_to_voxel(cls, block_model_file, ipj, variable_to_export, output_voxel_filename, remove_default_values, rock_code_filename):
        """
        Create a Geosoft voxel file from a Vulcan block model file.
        
        :param block_model_file:       Block model file
        :param ipj:                    Block model projection
        :param variable_to_export:     Variable to import
        :param output_voxel_filename:  Ouput voxel filename
        :param remove_default_values:  Remove default values from input? `GEO_BOOL`
        :param rock_code_filename:     Rock code file for string variable imports. Optional, unused for numeric variable imports.
        :type  block_model_file:       str
        :type  ipj:                    GXIPJ
        :type  variable_to_export:     str
        :type  output_voxel_filename:  str
        :type  remove_default_values:  int
        :type  rock_code_filename:     str

        .. versionadded:: 8.4
        """
        gxapi_cy.WrapVULCAN.block_model_to_voxel(GXContext._get_tls_geo(), block_model_file.encode(), ipj._wrapper, variable_to_export.encode(), output_voxel_filename.encode(), remove_default_values, rock_code_filename.encode())
        





### endblock ClassImplementation
### block ClassExtend
# NOTICE: The code generator will not replace the code in this block
### endblock ClassExtend


### block Footer
# NOTICE: The code generator will not replace the code in this block
### endblock Footer