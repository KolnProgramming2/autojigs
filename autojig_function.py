import pymeshlab
import trimesh

def smoothing(v, f):
    '''
    Smoothing a mesh
    
    Input
    ---------
    v: {array-like} Array of mesh vertices
    
    f: {array-like} Array of mesh faces
    
    
    Output
    ---------
    v_smoothed: {array-like} Array of smoothed mesh vertices
    
    f_smoothed: {array-like} Array of smoothed mesh faces
    
    '''
    
    m = pymeshlab.Mesh(v, f)
    ms = pymeshlab.MeshSet()
    
    ms.add_mesh(m, "ini_mesh")
    ms.apply_filter('apply_coord_laplacian_smoothing')
    
    m_smoothed = ms.current_mesh()
    v_smoothed = m_smoothed.vertex_matrix()
    f_smoothed = m_smoothed.face_matrix()
    
    return v_smoothed, f_smoothed

def remesh(v, f):
    '''
    Remeshing a mesh
    
    Input
    ---------
    v: {array-like} Array of mesh vertices
    
    f: {array-like} Array of mesh faces
    
    
    Output
    ---------
    v_remeshed: {array-like} Array of remeshed mesh vertices
    
    f_remeshed: {array-like} Array of remeshed mesh faces
    
    '''
    m = pymeshlab.Mesh(v, f)
    ms = pymeshlab.MeshSet()
    
    ms.add_mesh(m, "ini_mesh")
    ms.apply_filter('meshing_isotropic_explicit_remeshing')
    
    m_remeshed = ms.current_mesh()
    v_remeshed = m_remeshed.vertex_matrix()
    f_remeshed = m_remeshed.face_matrix()
    
    return v_remeshed, f_remeshed

def save(v, f, file_path):
    '''
    Save a mesh
    
    Input
    ---------
    v: {array-like} Array of mesh vertices
    
    f: {array-like} Array of mesh faces
    
    file_path: {string} Path of the original mesh file
    
    '''
    m = pymeshlab.Mesh(v, f)
    ms = pymeshlab.MeshSet()
    ms.add_mesh(m, "ini_mesh")
    
    origin_file = file_path.split('/')[-1]
    file_name = origin_file.split('.')[0]+'_rs.stl'
    ms.save_current_mesh(file_name)

def main():
    path = input('Please input the file path:\n')
    mesh = trimesh.load(path)
    v = mesh.vertices
    f = mesh.faces
    
    v_remeshed, f_remeshed = remesh(v, f)
    print('Remesh finished.')
    
    v_smoothed, f_smoothed = smoothing(v_remeshed, f_remeshed)
    print('Smoothing finished.')
    
    save(v_smoothed, f_smoothed, path)
    
    
if __name__ == '__main__':
    main()
    
