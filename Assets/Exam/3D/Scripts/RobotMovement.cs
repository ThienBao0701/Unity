using UnityEngine;

// Câu 3.2b: press W -> robot moves forward, press S -> robot moves backward.
// Attach to the Robot root object. "Forward" is the robot's blue Z axis (the side with the eyes).
public class RobotMovement : MonoBehaviour
{
    [Tooltip("Speed in world units per second.")]
    public float moveSpeed = 2f;

    void Update()
    {
        float direction = 0f;
        if (Input.GetKey(KeyCode.W)) direction += 1f; // forward
        if (Input.GetKey(KeyCode.S)) direction -= 1f; // backward

        // Space.Self: move along the robot's own forward axis.
        transform.Translate(Vector3.forward * direction * moveSpeed * Time.deltaTime, Space.Self);
    }
}
