#!/usr/bin/env python3

import os
from glob import glob
import SimpleITK as sitk
import numpy as np
from tqdm import tqdm
import pandas as pd

rootdir = "/home/yannick/Downloads/metas"
segmentnames = {"1": "Contrast-enhancing", "2": "Necrosis"}

dirlist = sorted([elem for elem in os.listdir(rootdir) if os.path.isdir(os.path.join(rootdir, elem))])

batchdf = pd.DataFrame(data=[], columns=["Patient", "Timepoint", "Image", "Mask", "Imagefile", "Maskfile", "Lesion", "Segment", "Label"])

curridx = 0
for dir in dirlist:
    currdir = os.path.join(rootdir, dir, dir, "NIFTI")

    # get segmentation files
    segfiles = sorted(glob(os.path.join(currdir, "*msk*")))

    for seg in segfiles:
        segfname = os.path.split(seg)[-1].split("_msk.nii")[0]
        patient, timepoint = segfname.split("_")[0:2]

        # features need to be extracted by lesion
        segimg = sitk.ReadImage(seg)
        labellist = np.unique(sitk.GetArrayFromImage(segimg))
        labellist = labellist[labellist > 0]

        for label in labellist:
            lstr = str(label)
            lesion = lstr[:-1]
            segment = lstr[-1]
            segname = segmentnames[segment]

            currdict = {"Patient": dir,
                        "Timepoint": timepoint,
                        "Image": os.path.join(currdir, segfname + "_img.nii"),
                        "Mask": seg,
                        "Imagefile": segfname + "_img.nii",
                        "Maskfile": segfname + "_msk.nii",
                        "Lesion": int(lesion),
                        "Segment": segname,
                        "Label": int(label)
                        }
            currdf = pd.DataFrame(currdict, index=[curridx])
            batchdf = pd.concat([batchdf, currdf], ignore_index=True)
            batchdf.to_csv(os.path.join(rootdir, "pyrad_batchinput.csv"), index=None)
            curridx += 1

batchdf.to_csv(os.path.join(rootdir, "pyrad_batchinput.csv"), index=None)
#
#
#
#
# segfiles = glob(os.path.join(rootdir, "*", "*", "NIFTI", "*msk*"))
#
# labellist = []
#
# for seg in tqdm(segfiles):
#     img = sitk.ReadImage(seg)
#     labels = np.unique(sitk.GetArrayFromImage(img))
#     labellist.extend(labels)
#
# print(labellist)
# print(np.unique(labellist))
# labelarr = np.array(labellist)
# uniquelabeles = np.unique(labelarr[labelarr > 0])
# print(uniquelabeles)