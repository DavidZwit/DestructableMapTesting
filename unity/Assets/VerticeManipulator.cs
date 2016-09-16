using UnityEngine;
using System.Collections;

public class VerticeManipulator : MonoBehaviour {
    Mesh plane;
    Vector3[] vertices;

    void Start()
    {
        plane = GetComponent<MeshFilter>().sharedMesh;
    }

    void OnCollisionEnter(Collision col)
    {

        vertices = plane.vertices;
        Vector3[,] multy = ArrayEditor.ToTwoDem<Vector3>(vertices);

        Vector3 point = col.gameObject.transform.position + (new Vector3(10, 0, 10)/2);
        print(point);

        try { multy[Mathf.Abs((int)point.y) + 1, Mathf.Abs((int)point.z + 1)].y -= 5;
            print(col.rigidbody.velocity.y);
        }
        catch { print("not in range"); }

        Vector3[] returnArray = ArrayEditor.ToOneDem< Vector3 >(multy);

        plane.vertices = returnArray;
        plane.RecalculateBounds();
    }

    Vector3[] Generate2dArray(int xSize, int ySize)
    {
        Vector3[] verts = new Vector3[(xSize + 1) * (ySize + 1)];

        for ( int i = 0, y = 0; y <= ySize; y++) {
            for (int x = 0; x <= xSize; x++, i++) {

                verts[i] = new Vector3(x, 0, y);

            }
        }

        return verts;
    }

    public void Regenerate()
    {
        plane = GetComponent<MeshFilter>().sharedMesh;


        plane.vertices = Generate2dArray(10, 10);
        plane.RecalculateBounds();
        plane.RecalculateNormals();
    }
}
