using UnityEngine;
using System.Collections;
using UnityEditor;

[CustomEditor(typeof(VerticeManipulator))]
public class MapGeneratorEditor : Editor
{

    public override void OnInspectorGUI()
    {
        VerticeManipulator mapGen = (VerticeManipulator)target;

        if (DrawDefaultInspector())
        {
            mapGen.Regenerate();
        }

        if (GUILayout.Button("Generate"))
        {
            mapGen.Regenerate();
        }
    }
}
