using UnityEngine;
using System.Collections;

public class tmpTestScript : MonoBehaviour {

	void Start () {
        Vector3[] verts = GetComponent<MeshFilter>().sharedMesh.vertices;

        foreach (Vector3 point in verts)
        {
            print(point);
        }
	}
}
