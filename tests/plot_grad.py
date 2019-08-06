#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import h5py as h5
import matplotlib.pyplot as plt
import numpy as np


file = h5.File("SeisCL_gout.mat", "r")

print(np.max(file["gradvp"]))
plt.imshow(file["gradvp"][32:-32,1:-32], aspect="auto")
plt.show()
file.close()
