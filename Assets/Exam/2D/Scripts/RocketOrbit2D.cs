using UnityEngine;

// Câu 2: the rocket flies in a circle AROUND the planet while the planet moves left -> right.
// Attach to the Rocket object and drag the Planet object into the "Planet" field.
public class RocketOrbit2D : MonoBehaviour
{
    [Tooltip("The centre of the orbit (the moving planet).")]
    public Transform planet;

    [Tooltip("Distance from the planet centre to the rocket, in world units.")]
    public float radius = 2.2f;

    [Tooltip("Degrees per second. 45 = one full circle every 8 seconds (slow).")]
    public float orbitSpeed = 45f;

    [Tooltip("Direction the rocket nose points in the original picture, in degrees (0 = right, 90 = up).")]
    public float spriteNoseAngle = 90f;

    private float angle; // current angle on the circle, in degrees

    void Start()
    {
        // Safety net: if the Inspector field was left empty, look for an object named "Planet".
        if (planet == null)
        {
            GameObject found = GameObject.Find("Planet");
            if (found != null) planet = found.transform;
            else Debug.LogError("RocketOrbit2D: drag the Planet object into the 'Planet' field.");
        }
    }

    // LateUpdate runs after PlanetMove2D.Update, so the rocket uses the planet's new position this frame.
    void LateUpdate()
    {
        if (planet == null) return;

        angle += orbitSpeed * Time.deltaTime;
        float rad = angle * Mathf.Deg2Rad;

        // Point on a circle: centre + (cos, sin) * radius
        Vector3 offset = new Vector3(Mathf.Cos(rad), Mathf.Sin(rad), 0f) * radius;
        transform.position = planet.position + offset;

        // Turn the nose along the direction of flight (the tangent of the circle = angle + 90 degrees).
        float flightAngle = angle + 90f;
        transform.rotation = Quaternion.Euler(0f, 0f, flightAngle - spriteNoseAngle);
    }
}
