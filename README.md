# gepAssetPipeline
Game Engine Programming Asset Pipeline. An export script for a particular mesh from blender using python

Command to run:
blender --background crate.blend --python export-model.py

Returns a list of all faces (triangles) that are present in the 'Crate' object in the scene. Also prints the index of the face, face normal and vertex data.

Vertex data:
  - Vertex Index
  - World Position for vertex
  - Local position for vertex
