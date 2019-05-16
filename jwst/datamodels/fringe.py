from .reference import ReferenceFileModel
from .dynamicdq import dynamic_mask


__all__ = ['FringeModel']


class FringeModel(ReferenceFileModel):
    """
    A data model for 2D fringe correction images.

    Parameters
    __________
    data : numpy float32 array
         The science data

    dq : numpy uint32 array
         Data quality array

    err : numpy float32 array
         Error array

    dq_def : numpy table
         DQ flag definitions
    """
    schema_url = "fringe.schema"

    def __init__(self, init=None, **kwargs):
        super(FringeModel, self).__init__(init=init, **kwargs)

        self.dq = dynamic_mask(self)

        # Implicitly create arrays
        self.dq = self.dq
        self.err = self.err
