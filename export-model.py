# Source: http://blenderscripting.blogspot.com/2011/05/blender-25-python-printing-vertex.html
import bpy  
  
current_obj = bpy.data.objects['Crate']
  
print("="*40) # printing marker
for face in current_obj.data.polygons:
    verts_in_face = face.vertices[:]
    print("face index", face.index)
    print("normal", face.normal)
    for vert in verts_in_face:
        local_point = current_obj.data.vertices[vert].co
        world_point = current_obj.matrix_world * local_point
        print("index: ", vert, ", world: ", world_point, ", local: ", local_point)