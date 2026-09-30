using UnityEngine;

// Câu 1b + Câu 2: moves the planet slowly from LEFT to RIGHT in 2D.
// Attach to the Planet object (a SpriteRenderer with the transparent Planet.png).
public class PlanetMove2D : MonoBehaviour
{
    [Tooltip("Speed in world units per second. Small value = slow movement.")]
    public float moveSpeed = 0.5f;

    [Tooltip("When the planet passes rightX it restarts at leftX, so the movement can be watched again.")]
    public bool loop = true;
    public float leftX = -7f;
    public float rightX = 7f;

    void Update()
    {
        // Vector3.right = (1, 0, 0): x increases every frame, so the planet moves left -> right.
        transform.Translate(Vector3.right * moveSpeed * Time.deltaTime, Space.World);

        if (loop && transform.position.x > rightX)
        {
            Vector3 p = transform.position;
            p.x = leftX;
            transform.position = p;
        }
    }
}
