import bpy
import bmesh
import random
#for z in range(0, random.randint(3,8)):
# Creo el bloque inicial del edificio
bpy.ops.mesh.primitive_plane_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, 0))
#escalo el plano para hacerlo mas grande
bpy.context.object.scale[0] = 8
bpy.context.object.scale[1] = 8
bpy.context.object.scale[2] = 8
bpy.ops.object.editmode_toggle()
# Lo subdivido varias veces
bpy.ops.mesh.subdivide(smoothness=0)
bpy.ops.mesh.subdivide(smoothness=0)
bpy.ops.mesh.subdivide(smoothness=0)
bpy.ops.mesh.bevel(offset=0.103231)
bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
bpy.ops.mesh.select_similar(type='PERIMETER', threshold=0.01)

bpy.ops.mesh.select_all(action='INVERT')
bpy.ops.mesh.delete(type='FACE')

bpy.ops.object.editmode_toggle()
# selecciono caras para hacer las paredes
bpy.context.active_object.data.polygons[0].select = True
bpy.context.active_object.data.polygons[67].select = True
bpy.ops.object.editmode_toggle()
bpy.ops.mesh.select_similar(type='PERIMETER', threshold=0.01)
# selecciono caras aleatorias para que las paredes no sean siempre iguales
bpy.ops.mesh.select_random(seed=random.randint(10,20))
bpy.ops.mesh.select_all(action='INVERT')
bpy.ops.mesh.delete(type='FACE')
bpy.ops.mesh.select_all(action='TOGGLE')
bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, 2), "constraint_axis":(False, False, True), "constraint_orientation":'NORMAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
bpy.ops.mesh.select_all(action='TOGGLE')
bpy.ops.object.editmode_toggle()
# extruyo las ventanas
bpy.context.active_object.data.polygons[297].select = True
bpy.ops.object.editmode_toggle()
bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, 0), "constraint_axis":(False, False, True), "constraint_orientation":'NORMAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
bpy.ops.transform.resize(value=(0.505945, 0.505945, 0.505945), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, 0.178131), "constraint_axis":(False, False, True), "constraint_orientation":'NORMAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
bpy.ops.object.editmode_toggle()

#zocalo
bpy.context.active_object.data.polygons[0].select = True
bpy.ops.object.editmode_toggle()
bpy.ops.mesh.select_similar(type='COPLANAR', threshold=0.01)
bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"mirror":False}, TRANSFORM_OT_translate={"value":(0, -0, 0), "constraint_axis":(False, False, True), "constraint_orientation":'NORMAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
bpy.ops.mesh.inset(thickness=0.01)
bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, 0.100215), "constraint_axis":(False, False, True), "constraint_orientation":'NORMAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
bpy.ops.mesh.select_all(action='TOGGLE')
bpy.ops.object.editmode_toggle()

## ventanas
bpy.context.active_object.data.polygons[340].select = True
bpy.ops.object.editmode_toggle()
bpy.ops.mesh.select_similar(type='PERIMETER', threshold=0.01)
bpy.ops.mesh.inset(thickness=0.04)
bpy.ops.mesh.extrude_faces_move(MESH_OT_extrude_faces_indiv={"mirror":False}, TRANSFORM_OT_shrink_fatten={"value":-0.022, "use_even_offset":False, "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "release_confirm":False})
bpy.ops.mesh.delete(type='FACE')
bpy.ops.object.editmode_toggle()


# ahora el exterior
bpy.ops.mesh.primitive_plane_add(radius=1, view_align=False, enter_editmode=False, location=(0, 0, -0.4))
bpy.context.object.scale[0] = 8.2
bpy.context.object.scale[1] = 8.2
bpy.context.object.scale[2] = 8.2
bpy.ops.object.editmode_toggle()
bpy.ops.mesh.select_mode(use_extend=False, use_expand=False, type='FACE')
bpy.ops.mesh.subdivide(smoothness=0)
bpy.ops.mesh.subdivide(smoothness=0)
bpy.ops.mesh.subdivide(smoothness=0)
bpy.ops.mesh.bevel(offset=0.103231)
bpy.context.active_object.data.polygons[0].select = True
bpy.ops.mesh.select_similar(type='PERIMETER', threshold=0.01)
bpy.ops.mesh.select_all(action='TOGGLE')
bpy.ops.mesh.select_all(action='TOGGLE')
bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, 2.4), "constraint_axis":(False, False, True), "constraint_orientation":'NORMAL', "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False})
bpy.context.active_object.data.polygons[0].select = True
bpy.ops.mesh.select_similar(type='NORMAL', threshold=0.01)
bpy.ops.mesh.delete(type='FACE')
bpy.ops.object.editmode_toggle()
bpy.context.active_object.data.polygons[0].select = True
bpy.ops.object.editmode_toggle()
bpy.ops.mesh.select_similar(type='NORMAL', threshold=0.01)

bpy.ops.mesh.delete(type='FACE')
bpy.ops.object.editmode_toggle()
bpy.context.active_object.data.polygons[20].select = True
bpy.ops.object.editmode_toggle()
bpy.ops.mesh.select_similar(type='PERIMETER', threshold=0.01)

bpy.ops.mesh.inset(thickness=0.04)
bpy.ops.mesh.extrude_faces_move(MESH_OT_extrude_faces_indiv={"mirror":False}, TRANSFORM_OT_shrink_fatten={"value": 0.022, "use_even_offset":False, "mirror":False, "proportional":'DISABLED', "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "release_confirm":False})
bpy.ops.mesh.delete(type='FACE')
bpy.ops.object.editmode_toggle()
