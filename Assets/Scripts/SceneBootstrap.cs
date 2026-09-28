using UnityEngine;
public class SceneBootstrap : MonoBehaviour {
    public enum Mode { CustomInterface, PlayersInterface, ObjectSeparation }
    public Mode mode;
    void Awake() {
        if(mode==Mode.ObjectSeparation) gameObject.AddComponent<ObjectSeparationUI>();
        else gameObject.AddComponent<MathDuelUI>();
    }
}