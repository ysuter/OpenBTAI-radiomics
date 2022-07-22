#!/usr/bin/env python3

import pandas as pd

inp = "/home/yannick/Downloads/metas/pyrad_feat.csv"
out = "/home/yannick/Downloads/metas/pyrad_feat_metas.csv"

inpdata = pd.read_csv(inp)

# put patient, timepoint, and label info first
columns = inpdata.columns.values
cols_to_move = ['Patient', 'Timepoint', 'Label', 'Lesion', 'Segment']
inpdata = inpdata[ cols_to_move + [ col for col in inpdata.columns if col not in cols_to_move]]

# Redundant, since the columns are the same as "Image" and "Mask" after removing the full path
inpdata.drop(columns=["Imagefile", "Maskfile"], inplace=True)

inpdata.to_csv(out, index=None)
