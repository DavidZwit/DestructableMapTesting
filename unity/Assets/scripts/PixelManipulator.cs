using UnityEngine;
using System.Collections;

public class PixelManipulator : MonoBehaviour {

    SpriteRenderer img;
        
    void Start()
    {
        img = GetComponent<SpriteRenderer>();

        Texture2D tex = img.sprite.texture;

        tex.SetPixel(50, 50, Color.green);

        tex.Apply();
    }
}
