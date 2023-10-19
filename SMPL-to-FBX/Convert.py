"""
   Copyright (C) 2017 Autodesk, Inc.
   All rights reserved.

   Use of this software is subject to the terms of the Autodesk license agreement
   provided at the time of installation or download, or which otherwise accompanies
   this software in either electronic or hard copy form.
 
"""

"""
SMPL-to-FBX是一个第三方项目，用于将本项目生成的，基于SMPL编码规则的动作缓存数据(.pkl)转换为blender等主流动画制作软件支持的.fbx形式
"""
import argparse
import os
import sys
sys.path
sys.path.append('.')

from tqdm import tqdm
from FbxReadWriter import FbxReadWrite
from SmplObject import SmplObjects


def getArg():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_dir", type=str, default="SMPL-to-FBX/motions")
    parser.add_argument(
        "--fbx_source_path",
        type=str,
        default="SMPL-to-FBX/ybot.fbx",
    )
    parser.add_argument("--output_dir", type=str, default="SMPL-to-FBX/fbx_out")

    return parser.parse_args()


if __name__ == "__main__":
    args = getArg()
    input_dir = args.input_dir
    fbx_source_path = args.fbx_source_path
    output_dir = args.output_dir

    smplObjects = SmplObjects(input_dir)
    for pkl_name, smpl_params in tqdm(smplObjects):
        try:
            fbxReadWrite = FbxReadWrite(fbx_source_path)
            fbxReadWrite.addAnimation(pkl_name, smpl_params)
            fbxReadWrite.writeFbx(output_dir, pkl_name)
        except Exception as e:
            fbxReadWrite.destroy()
            print("An error was thrown in the FBX conversion process")
            raise e
        finally:
            fbxReadWrite.destroy()
    # convert everything in output folder from ascii to binary
    # this line can be commented out if not directly importing to Blender
    out = os.system(f"wine SMPL-to-FBX/FbxFormatConverter.exe -c {output_dir} -binary")
    
