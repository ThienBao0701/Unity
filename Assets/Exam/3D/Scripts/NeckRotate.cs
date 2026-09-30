using UnityEngine;

// Câu 3.2a: "Robot thực xoay tròn cổ của nó liên tục khi chương trình chạy."
// Attach to the robot's Neck object. The Head is a child of the Neck, so the head turns with it.
// Rotation starts automatically in Play Mode and never stops (no key needed).
public class NeckRotate : MonoBehaviour
{
    [Tooltip("Degrees per second around the vertical (Y) axis.")]
    public float rotateSpeed = 90f;

    void Update()
    {
        transform.Rotate(0f, rotateSpeed * Time.deltaTime, 0f, Space.Self);
    }
}
