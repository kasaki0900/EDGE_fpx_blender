import bpy
import sys


blender_file = sys.argv[-3]
fbx_model = sys.argv[-2]
output = sys.argv[-1]

bpy.context.scene.render.engine = 'BLENDER_WORKBENCH'

# open .blend
bpy.ops.wm.open_mainfile(filepath=blender_file)

# fbx
bpy.ops.import_scene.fbx(filepath=fbx_model)

obj = bpy.data.objects.get("smpl")
obj.location = (0, 0, -2)

start = 0
end = 300

# render
scene = bpy.context.scene
scene.frame_start = start
scene.frame_end = end


scene.render.image_settings.file_format = 'PNG'
bpy.context.scene.render.fps = 15
scene.render.filepath = output

bpy.ops.render.render(animation=True)

