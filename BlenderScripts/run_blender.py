import subprocess
import background


blender_file = "F:\\BlenderPro\\ast\\tp.blend"  # 空blender文件，主要是设置参数用
fbx_model = "F:\\BlenderPro\\ast\\test.fbx"
output_img = "F:\\BlenderPro\\ast\\render\\rd"  # 生成的是图片，blender视频不支持alpha通道

bld_args = [
    "E:\\Blender 4.0\\blender.exe",
    "--background",
    "--python", "F:\\Code\\Py\\BlenderScripts\\video.py",  # 脚本
    "--",
    blender_file,
    fbx_model,
    output_img
]

subprocess.run(args=bld_args)
background.gen(640, 360)
