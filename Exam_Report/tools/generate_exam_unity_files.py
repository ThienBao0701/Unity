#!/usr/bin/env python3
"""Generates Unity 2022.3 YAML (folder/script/material metas, materials, 3 exam scenes).

Run from anywhere:  python3 gen_project.py /home/user/Unity
Sprite metas are written by process_images.py (they need the image size).
"""
import math
import os
import sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else "/home/user/Unity"
EX = os.path.join(ROOT, "Assets", "Exam")

G = {
    # folders
    "Assets/Exam": "5b1c2d3e4f5a46b7a8c9d0e1f2a3b401",
    "Assets/Exam/2D": "5b1c2d3e4f5a46b7a8c9d0e1f2a3b402",
    "Assets/Exam/2D/Scripts": "5b1c2d3e4f5a46b7a8c9d0e1f2a3b403",
    "Assets/Exam/2D/Sprites": "5b1c2d3e4f5a46b7a8c9d0e1f2a3b404",
    "Assets/Exam/2D/Scenes": "5b1c2d3e4f5a46b7a8c9d0e1f2a3b405",
    "Assets/Exam/3D": "5b1c2d3e4f5a46b7a8c9d0e1f2a3b406",
    "Assets/Exam/3D/Scripts": "5b1c2d3e4f5a46b7a8c9d0e1f2a3b407",
    "Assets/Exam/3D/Materials": "5b1c2d3e4f5a46b7a8c9d0e1f2a3b408",
    "Assets/Exam/3D/Scenes": "5b1c2d3e4f5a46b7a8c9d0e1f2a3b409",
    # scripts
    "PlanetMove2D": "8c4f0e7a1d2b4c3e9f5a6b7c8d9e0a11",
    "RocketOrbit2D": "8c4f0e7a1d2b4c3e9f5a6b7c8d9e0a12",
    "NeckRotate": "8c4f0e7a1d2b4c3e9f5a6b7c8d9e0a13",
    "RobotMovement": "8c4f0e7a1d2b4c3e9f5a6b7c8d9e0a14",
    # sprites
    "Planet": "9d2e1f3a4b5c46d7e8f9a0b1c2d3e4f1",
    "Rocket": "9d2e1f3a4b5c46d7e8f9a0b1c2d3e4f2",
    # materials
    "Robot_Orange": "6e7f8a9b0c1d42e3f4a5b6c7d8e9f0a1",
    "Robot_Silver": "6e7f8a9b0c1d42e3f4a5b6c7d8e9f0a2",
    "Robot_EyeDark": "6e7f8a9b0c1d42e3f4a5b6c7d8e9f0a3",
    "Robot_EyeLens": "6e7f8a9b0c1d42e3f4a5b6c7d8e9f0a4",
    "Floor_Grey": "6e7f8a9b0c1d42e3f4a5b6c7d8e9f0a5",
    # scenes
    "Cau1_PlanetMove2D": "4a5b6c7d8e9f40a1b2c3d4e5f6a7b8c1",
    "Cau2_RocketOrbit2D": "4a5b6c7d8e9f40a1b2c3d4e5f6a7b8c2",
    "Cau3_Robot3D": "4a5b6c7d8e9f40a1b2c3d4e5f6a7b8c3",
}

MESH = {"Cube": 10202, "Cylinder": 10206, "Sphere": 10207, "Capsule": 10208, "Plane": 10209}
BUILTIN_EXTRA = "0000000000000000e000000000000000"
BUILTIN_RES = "0000000000000000f000000000000000"


def write(rel, text):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def f(x):
    """Unity-style float formatting."""
    if abs(x) < 1e-9:
        return "0"
    s = ("%.7f" % x).rstrip("0").rstrip(".")
    return "0" if s in ("-0", "") else s


def quat_euler(x, y, z):
    """Unity Quaternion.Euler (rotation order Z, then X, then Y). Returns (x, y, z, w)."""
    def axis(ax, deg):
        h = math.radians(deg) / 2
        s, c = math.sin(h), math.cos(h)
        return {"x": (s, 0, 0, c), "y": (0, s, 0, c), "z": (0, 0, s, c)}[ax]

    def mul(a, b):
        ax, ay, az, aw = a
        bx, by, bz, bw = b
        return (aw * bx + ax * bw + ay * bz - az * by,
                aw * by - ax * bz + ay * bw + az * bx,
                aw * bz + ax * by - ay * bx + az * bw,
                aw * bw - ax * bx - ay * by - az * bz)

    return mul(mul(axis("y", y), axis("x", x)), axis("z", z))


def look_euler(pos, target):
    dx, dy, dz = (target[i] - pos[i] for i in range(3))
    yaw = math.degrees(math.atan2(dx, dz))
    pitch = math.degrees(math.atan2(-dy, math.hypot(dx, dz)))
    return (pitch, yaw, 0.0)


# ---------------------------------------------------------------- metas
FOLDER_META = """fileFormatVersion: 2
guid: {g}
folderAsset: yes
DefaultImporter:
  externalObjects: {{}}
  userData:
  assetBundleName:
  assetBundleVariant:
"""
SCRIPT_META = """fileFormatVersion: 2
guid: {g}
MonoImporter:
  externalObjects: {{}}
  serializedVersion: 2
  defaultReferences: []
  executionOrder: 0
  icon: {{instanceID: 0}}
  userData:
  assetBundleName:
  assetBundleVariant:
"""
SCENE_META = """fileFormatVersion: 2
guid: {g}
DefaultImporter:
  externalObjects: {{}}
  userData:
  assetBundleName:
  assetBundleVariant:
"""
MAT_META = """fileFormatVersion: 2
guid: {g}
NativeFormatImporter:
  externalObjects: {{}}
  mainObjectFileID: 2100000
  userData:
  assetBundleName:
  assetBundleVariant:
"""

for folder in [k for k in G if k.startswith("Assets/")]:
    write(folder + ".meta", FOLDER_META.format(g=G[folder]))

for name, sub in [("PlanetMove2D", "2D"), ("RocketOrbit2D", "2D"), ("NeckRotate", "3D"), ("RobotMovement", "3D")]:
    write(f"Assets/Exam/{sub}/Scripts/{name}.cs.meta", SCRIPT_META.format(g=G[name]))

# ---------------------------------------------------------------- materials (Built-in Standard shader)
MAT = """%YAML 1.1
%TAG !u! tag:unity3d.com,2011:
--- !u!21 &2100000
Material:
  serializedVersion: 8
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_Name: {name}
  m_Shader: {{fileID: 46, guid: 0000000000000000f000000000000000, type: 0}}
  m_Parent: {{fileID: 0}}
  m_ModifiedSerializedProperties: 0
  m_ValidKeywords: []
  m_InvalidKeywords: []
  m_LightmapFlags: 4
  m_EnableInstancingVariants: 0
  m_DoubleSidedGI: 0
  m_CustomRenderQueue: -1
  stringTagMap: {{}}
  disabledShaderPasses: []
  m_LockedProperties:
  m_SavedProperties:
    serializedVersion: 3
    m_TexEnvs:
    - _BumpMap:
        m_Texture: {{fileID: 0}}
        m_Scale: {{x: 1, y: 1}}
        m_Offset: {{x: 0, y: 0}}
    - _DetailAlbedoMap:
        m_Texture: {{fileID: 0}}
        m_Scale: {{x: 1, y: 1}}
        m_Offset: {{x: 0, y: 0}}
    - _DetailMask:
        m_Texture: {{fileID: 0}}
        m_Scale: {{x: 1, y: 1}}
        m_Offset: {{x: 0, y: 0}}
    - _DetailNormalMap:
        m_Texture: {{fileID: 0}}
        m_Scale: {{x: 1, y: 1}}
        m_Offset: {{x: 0, y: 0}}
    - _EmissionMap:
        m_Texture: {{fileID: 0}}
        m_Scale: {{x: 1, y: 1}}
        m_Offset: {{x: 0, y: 0}}
    - _MainTex:
        m_Texture: {{fileID: 0}}
        m_Scale: {{x: 1, y: 1}}
        m_Offset: {{x: 0, y: 0}}
    - _MetallicGlossMap:
        m_Texture: {{fileID: 0}}
        m_Scale: {{x: 1, y: 1}}
        m_Offset: {{x: 0, y: 0}}
    - _OcclusionMap:
        m_Texture: {{fileID: 0}}
        m_Scale: {{x: 1, y: 1}}
        m_Offset: {{x: 0, y: 0}}
    - _ParallaxMap:
        m_Texture: {{fileID: 0}}
        m_Scale: {{x: 1, y: 1}}
        m_Offset: {{x: 0, y: 0}}
    m_Ints: []
    m_Floats:
    - _BumpScale: 1
    - _Cutoff: 0.5
    - _DetailNormalMapScale: 1
    - _DstBlend: 0
    - _GlossMapScale: 1
    - _Glossiness: {gloss}
    - _GlossyReflections: 1
    - _Metallic: {metal}
    - _Mode: 0
    - _OcclusionStrength: 1
    - _Parallax: 0.02
    - _SmoothnessTextureChannel: 0
    - _SpecularHighlights: 1
    - _SrcBlend: 1
    - _UVSec: 0
    - _ZWrite: 1
    m_Colors:
    - _Color: {{r: {r}, g: {g}, b: {b}, a: 1}}
    - _EmissionColor: {{r: 0, g: 0, b: 0, a: 1}}
  m_BuildTextureStacks: []
"""
MATERIALS = {
    # name: (r, g, b, glossiness, metallic)
    "Robot_Orange": (1.0, 0.45, 0.05, 0.55, 0.0),   # bright orange body/head/arms
    "Robot_Silver": (0.78, 0.8, 0.82, 0.75, 0.6),   # hands, feet, neck, chest panel
    "Robot_EyeDark": (0.08, 0.08, 0.1, 0.6, 0.2),   # camera housing of the eyes
    "Robot_EyeLens": (0.35, 0.8, 1.0, 0.95, 0.0),   # camera lens
    "Floor_Grey": (0.55, 0.57, 0.6, 0.2, 0.0),
}
for name, (r, g, b, gl, me) in MATERIALS.items():
    write(f"Assets/Exam/3D/Materials/{name}.mat",
          MAT.format(name=name, r=f(r), g=f(g), b=f(b), gloss=f(gl), metal=f(me)))
    write(f"Assets/Exam/3D/Materials/{name}.mat.meta", MAT_META.format(g=G[name]))


# ---------------------------------------------------------------- scene builder
class Scene:
    def __init__(self):
        self.next_id = 100
        self.blocks = []
        self.roots = []
        self.children = {}   # transform id -> [child transform ids]
        self.tr_blocks = {}  # transform id -> dict

    def nid(self):
        self.next_id += 1
        return self.next_id

    def go(self, name, parent=None, pos=(0, 0, 0), euler=(0, 0, 0), scale=(1, 1, 1), components=()):
        """Create GameObject + Transform. components: list of (classId, id, text_without_header)."""
        gid, tid = self.nid(), self.nid()
        comp_ids = [tid] + [c[1] for c in components]
        comp_list = "\n".join("  - component: {fileID: %d}" % c for c in comp_ids)
        self.blocks.append(f"""--- !u!1 &{gid}
GameObject:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  serializedVersion: 6
  m_Component:
{comp_list}
  m_Layer: 0
  m_Name: {name}
  m_TagString: {"MainCamera" if name == "Main Camera" else "Untagged"}
  m_Icon: {{fileID: 0}}
  m_NavMeshLayer: 0
  m_StaticEditorFlags: 0
  m_IsActive: 1
""")
        q = quat_euler(*euler)
        self.tr_blocks[tid] = dict(gid=gid, pos=pos, q=q, euler=euler, scale=scale,
                                   parent=parent)
        self.children.setdefault(tid, [])
        if parent is None:
            self.roots.append(tid)
        else:
            self.children[parent].append(tid)
        for cls, cid, body in components:
            self.blocks.append(body.replace("@GO@", str(gid)))
        return tid

    # component factories ------------------------------------------------
    HEAD = """  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {fileID: 0}
  m_PrefabInstance: {fileID: 0}
  m_PrefabAsset: {fileID: 0}
  m_GameObject: {fileID: @GO@}
"""

    def mesh(self, mesh_name, mat_guid, shadows=True):
        fid, rid = self.nid(), self.nid()
        mf = f"--- !u!33 &{fid}\nMeshFilter:\n{self.HEAD}  m_Mesh: {{fileID: {MESH[mesh_name]}, guid: {BUILTIN_EXTRA}, type: 0}}\n"
        mr = f"--- !u!23 &{rid}\nMeshRenderer:\n{self.HEAD}" + self.renderer_common(
            f"{{fileID: 2100000, guid: {mat_guid}, type: 2}}", 1 if shadows else 0, 1 if shadows else 0, 0)
        return [(33, fid, mf), (23, rid, mr)]

    @staticmethod
    def renderer_common(mat_ref, cast, receive, order):
        return f"""  m_Enabled: 1
  m_CastShadows: {cast}
  m_ReceiveShadows: {receive}
  m_DynamicOccludee: 1
  m_StaticShadowCaster: 0
  m_MotionVectors: 1
  m_LightProbeUsage: 1
  m_ReflectionProbeUsage: 1
  m_RayTracingMode: 2
  m_RayTraceProcedural: 0
  m_RenderingLayerMask: 1
  m_RendererPriority: 0
  m_Materials:
  - {mat_ref}
  m_StaticBatchInfo:
    firstSubMesh: 0
    subMeshCount: 0
  m_StaticBatchRoot: {{fileID: 0}}
  m_ProbeAnchor: {{fileID: 0}}
  m_LightProbeVolumeOverride: {{fileID: 0}}
  m_ScaleInLightmap: 1
  m_ReceiveGI: 1
  m_PreserveUVs: 0
  m_IgnoreNormalsForChartDetection: 0
  m_ImportantGI: 0
  m_StitchLightmapSeams: 1
  m_SelectedEditorRenderState: 3
  m_MinimumChartSize: 4
  m_AutoUVMaxDistance: 0.5
  m_AutoUVMaxAngle: 89
  m_LightmapParameters: {{fileID: 0}}
  m_SortingLayerID: 0
  m_SortingLayer: 0
  m_SortingOrder: {order}
  m_AdditionalVertexStreams: {{fileID: 0}}
"""

    def sprite(self, sprite_guid, order):
        sid = self.nid()
        body = f"--- !u!212 &{sid}\nSpriteRenderer:\n{self.HEAD}" + self.renderer_common(
            f"{{fileID: 10754, guid: {BUILTIN_RES}, type: 0}}", 0, 0, order).replace(
            "  m_AdditionalVertexStreams: {fileID: 0}\n", "") + f"""  m_Sprite: {{fileID: 21300000, guid: {sprite_guid}, type: 3}}
  m_Color: {{r: 1, g: 1, b: 1, a: 1}}
  m_FlipX: 0
  m_FlipY: 0
  m_DrawMode: 0
  m_Size: {{x: 1, y: 1}}
  m_AdaptiveModeThreshold: 0.5
  m_SpriteTileMode: 0
  m_WasSpriteAssigned: 1
  m_MaskInteraction: 0
  m_SpriteSortPoint: 0
"""
        return [(212, sid, body)]

    def script(self, script_guid, fields):
        mid = self.nid()
        extra = "".join(f"  {k}: {v}\n" for k, v in fields)
        body = f"""--- !u!114 &{mid}
MonoBehaviour:
{self.HEAD}  m_Enabled: 1
  m_EditorHideFlags: 0
  m_Script: {{fileID: 11500000, guid: {script_guid}, type: 3}}
  m_Name:
  m_EditorClassIdentifier:
{extra}"""
        return [(114, mid, body)]

    def camera(self, bg, ortho, size=5, fov=60):
        cid, aid = self.nid(), self.nid()
        cam = f"""--- !u!20 &{cid}
Camera:
{self.HEAD}  m_Enabled: 1
  serializedVersion: 2
  m_ClearFlags: 2
  m_BackGroundColor: {{r: {f(bg[0])}, g: {f(bg[1])}, b: {f(bg[2])}, a: 0}}
  m_projectionMatrixMode: 1
  m_GateFitMode: 2
  m_FOVAxisMode: 0
  m_Iso: 200
  m_ShutterSpeed: 0.005
  m_Aperture: 16
  m_FocusDistance: 10
  m_FocalLength: 50
  m_BladeCount: 5
  m_Curvature: {{x: 2, y: 11}}
  m_BarrelClipping: 0.25
  m_Anamorphism: 0
  m_SensorSize: {{x: 36, y: 24}}
  m_LensShift: {{x: 0, y: 0}}
  m_NormalizedViewPortRect:
    serializedVersion: 2
    x: 0
    y: 0
    width: 1
    height: 1
  near clip plane: 0.3
  far clip plane: 1000
  field of view: {f(fov)}
  orthographic: {1 if ortho else 0}
  orthographic size: {f(size)}
  m_Depth: -1
  m_CullingMask:
    serializedVersion: 2
    m_Bits: 4294967295
  m_RenderingPath: -1
  m_TargetTexture: {{fileID: 0}}
  m_TargetDisplay: 0
  m_TargetEye: 3
  m_HDR: 1
  m_AllowMSAA: 1
  m_AllowDynamicResolution: 0
  m_ForceIntoRT: 0
  m_OcclusionCulling: 1
  m_StereoConvergence: 10
  m_StereoSeparation: 0.022
"""
        al = f"--- !u!81 &{aid}\nAudioListener:\n{self.HEAD}  m_Enabled: 1\n"
        return [(20, cid, cam), (81, aid, al)]

    def dir_light(self):
        lid = self.nid()
        body = f"""--- !u!108 &{lid}
Light:
{self.HEAD}  m_Enabled: 1
  serializedVersion: 10
  m_Type: 1
  m_Shape: 0
  m_Color: {{r: 1, g: 0.95686275, b: 0.8392157, a: 1}}
  m_Intensity: 1.1
  m_Range: 10
  m_SpotAngle: 30
  m_InnerSpotAngle: 21.80208
  m_CookieSize: 10
  m_Shadows:
    m_Type: 2
    m_Resolution: -1
    m_CustomResolution: -1
    m_Strength: 1
    m_Bias: 0.05
    m_NormalBias: 0.4
    m_NearPlane: 0.2
    m_CullingMatrixOverride:
      e00: 1
      e01: 0
      e02: 0
      e03: 0
      e10: 0
      e11: 1
      e12: 0
      e13: 0
      e20: 0
      e21: 0
      e22: 1
      e23: 0
      e30: 0
      e31: 0
      e32: 0
      e33: 1
    m_UseCullingMatrixOverride: 0
  m_Cookie: {{fileID: 0}}
  m_DrawHalo: 0
  m_Flare: {{fileID: 0}}
  m_RenderMode: 0
  m_CullingMask:
    serializedVersion: 2
    m_Bits: 4294967295
  m_RenderingLayerMask: 1
  m_Lightmapping: 4
  m_LightShadowCasterMode: 0
  m_AreaSize: {{x: 1, y: 1}}
  m_BounceIntensity: 1
  m_ColorTemperature: 6570
  m_UseColorTemperature: 0
  m_BoundingSphereOverride: {{x: 0, y: 0, z: 0, w: 0}}
  m_UseBoundingSphereOverride: 0
  m_UseViewFrustumForShadowCasterCull: 1
  m_ShadowRadius: 0
  m_ShadowAngle: 0
"""
        return [(108, lid, body)]

    # output -------------------------------------------------------------
    def render(self, ambient):
        out = ["%YAML 1.1\n%TAG !u! tag:unity3d.com,2011:\n"]
        out.append(f"""--- !u!29 &1
OcclusionCullingSettings:
  m_ObjectHideFlags: 0
  serializedVersion: 2
  m_OcclusionBakeSettings:
    smallestOccluder: 5
    smallestHole: 0.25
    backfaceThreshold: 100
  m_SceneGUID: 00000000000000000000000000000000
  m_OcclusionCullingData: {{fileID: 0}}
--- !u!104 &2
RenderSettings:
  m_ObjectHideFlags: 0
  serializedVersion: 9
  m_Fog: 0
  m_FogColor: {{r: 0.5, g: 0.5, b: 0.5, a: 1}}
  m_FogMode: 3
  m_FogDensity: 0.01
  m_LinearFogStart: 0
  m_LinearFogEnd: 300
  m_AmbientSkyColor: {{r: {f(ambient)}, g: {f(ambient)}, b: {f(ambient + 0.03)}, a: 1}}
  m_AmbientEquatorColor: {{r: 0.114, g: 0.125, b: 0.133, a: 1}}
  m_AmbientGroundColor: {{r: 0.047, g: 0.043, b: 0.035, a: 1}}
  m_AmbientIntensity: 1
  m_AmbientMode: 3
  m_SubtractiveShadowColor: {{r: 0.42, g: 0.478, b: 0.627, a: 1}}
  m_SkyboxMaterial: {{fileID: 10304, guid: {BUILTIN_RES}, type: 0}}
  m_HaloStrength: 0.5
  m_FlareStrength: 1
  m_FlareFadeSpeed: 3
  m_HaloTexture: {{fileID: 0}}
  m_SpotCookie: {{fileID: 10001, guid: {BUILTIN_EXTRA}, type: 0}}
  m_DefaultReflectionMode: 0
  m_DefaultReflectionResolution: 128
  m_ReflectionBounces: 1
  m_ReflectionIntensity: 1
  m_CustomReflection: {{fileID: 0}}
  m_Sun: {{fileID: 0}}
  m_IndirectSpecularColor: {{r: 0, g: 0, b: 0, a: 1}}
  m_UseRadianceAmbientProbe: 0
""")
        out.extend(self.blocks)
        for tid, t in self.tr_blocks.items():
            px, py, pz = t["pos"]
            qx, qy, qz, qw = t["q"]
            ex, ey, ez = t["euler"]
            sx, sy, sz = t["scale"]
            kids = self.children[tid]
            kid_txt = "m_Children: []" if not kids else "m_Children:\n" + "\n".join(
                "  - {fileID: %d}" % k for k in kids)
            out.append(f"""--- !u!4 &{tid}
Transform:
  m_ObjectHideFlags: 0
  m_CorrespondingSourceObject: {{fileID: 0}}
  m_PrefabInstance: {{fileID: 0}}
  m_PrefabAsset: {{fileID: 0}}
  m_GameObject: {{fileID: {t['gid']}}}
  serializedVersion: 2
  m_LocalRotation: {{x: {f(qx)}, y: {f(qy)}, z: {f(qz)}, w: {f(qw)}}}
  m_LocalPosition: {{x: {f(px)}, y: {f(py)}, z: {f(pz)}}}
  m_LocalScale: {{x: {f(sx)}, y: {f(sy)}, z: {f(sz)}}}
  m_ConstrainProportionsScale: 0
  {kid_txt}
  m_Father: {{fileID: {t['parent'] or 0}}}
  m_LocalEulerAnglesHint: {{x: {f(ex)}, y: {f(ey)}, z: {f(ez)}}}
""")
        roots = "\n".join("  - {fileID: %d}" % r for r in self.roots)
        out.append(f"""--- !u!1660057539 &9223372036854775807
SceneRoots:
  m_ObjectHideFlags: 0
  m_Roots:
{roots}
""")
        return "".join(out)


def transform_ref(tid):
    return "{fileID: %d}" % tid


# ---------------------------------------------------------------- 2D scenes
BG_2D = (0.80, 0.90, 1.0)   # light sky blue: shows that the sprites have NO white box behind them
PLANET_START_X = -7


def scene_2d(with_rocket):
    s = Scene()
    s.go("Main Camera", pos=(0, 0, -10), components=s.camera(BG_2D, ortho=True, size=5))
    planet = s.go("Planet", pos=(PLANET_START_X, 0, 0), components=(
        s.sprite(G["Planet"], order=0) +
        s.script(G["PlanetMove2D"], [("moveSpeed", "0.5"), ("loop", "1"),
                                     ("leftX", "-7"), ("rightX", "7")])))
    if with_rocket:
        s.go("Rocket", pos=(PLANET_START_X + 2.2, 0, 0), components=(
            s.sprite(G["Rocket"], order=1) +
            s.script(G["RocketOrbit2D"], [("planet", transform_ref(planet)), ("radius", "2.2"),
                                          ("orbitSpeed", "45"),
                                          ("spriteNoseAngle", ROCKET_NOSE_ANGLE)])))
    return s.render(ambient=0.5)


# Nose direction of the rocket in Rocket.png (degrees, 0 = right, 90 = up); set by process_images.py.
ROCKET_NOSE_ANGLE = os.environ.get("ROCKET_NOSE_ANGLE", "45")

write("Assets/Exam/2D/Scenes/Cau1_PlanetMove2D.unity", scene_2d(False))
write("Assets/Exam/2D/Scenes/Cau1_PlanetMove2D.unity.meta", SCENE_META.format(g=G["Cau1_PlanetMove2D"]))
write("Assets/Exam/2D/Scenes/Cau2_RocketOrbit2D.unity", scene_2d(True))
write("Assets/Exam/2D/Scenes/Cau2_RocketOrbit2D.unity.meta", SCENE_META.format(g=G["Cau2_RocketOrbit2D"]))

# ---------------------------------------------------------------- 3D scene (robot)
s = Scene()
ORANGE, SILVER, DARK, LENS = (G[k] for k in ("Robot_Orange", "Robot_Silver", "Robot_EyeDark", "Robot_EyeLens"))

cam_pos = (2.5, 2.3, 4.3)
s.go("Main Camera", pos=cam_pos, euler=look_euler(cam_pos, (0, 1.15, 0)),
     components=s.camera((0.72, 0.82, 0.92), ortho=False, fov=50))
s.go("Directional Light", euler=(50, -30, 0), pos=(0, 3, 0), components=s.dir_light())
s.go("Floor", scale=(3, 1, 3), components=s.mesh("Plane", G["Floor_Grey"]))

# Robot root stands on the floor (y = 0) and faces +Z (its forward / blue axis).
robot = s.go("Robot", components=s.script(G["RobotMovement"], [("moveSpeed", "2")]))

# Body: orange cylinder, radius 0.5, height 1.2 (y 0.5 .. 1.7) -> compact, cylindrical.
s.go("Body", parent=robot, pos=(0, 1.1, 0), scale=(1, 0.6, 1), components=s.mesh("Cylinder", ORANGE))
# Chest panel: plain small rectangle on the front (exam: no inner chest details needed).
s.go("ChestPanel", parent=robot, pos=(0, 1.2, 0.49), scale=(0.46, 0.3, 0.06), components=s.mesh("Cube", SILVER))

# Neck (rotates continuously -> Câu 3.2a). Head is its child so it turns with the neck.
# Neck is an unscaled pivot; visible shapes are children so nothing gets squashed or skewed.
neck = s.go("Neck", parent=robot, pos=(0, 1.7, 0),
            components=s.script(G["NeckRotate"], [("rotateSpeed", "90")]))
s.go("NeckShape", parent=neck, pos=(0, 0.08, 0), scale=(0.24, 0.08, 0.24), components=s.mesh("Cylinder", SILVER))

# Head: rounded (sphere) with two large camera-like eyes on the front (+Z).
head = s.go("Head", parent=neck, pos=(0, 0.5, 0))
s.go("HeadShape", parent=head, scale=(0.8, 0.7, 0.8), components=s.mesh("Sphere", ORANGE))
for side, x in (("LeftEye", -0.17), ("RightEye", 0.17)):
    eye = s.go(side, parent=head, pos=(x, 0.03, 0.34))
    # camera housing: a dark disc facing forward (cylinder turned 90 degrees on X)
    s.go("CameraHousing", parent=eye, euler=(90, 0, 0), scale=(0.24, 0.05, 0.24), components=s.mesh("Cylinder", DARK))
    # camera lens: light-blue glossy sphere in the middle of the housing
    s.go("Lens", parent=eye, pos=(0, 0, 0.06), scale=(0.13, 0.13, 0.13), components=s.mesh("Sphere", LENS))

# Arms: long orange arms with round silver hands. Each arm is a shoulder pivot (rotate it to move the arm).
# LeftArm is raised in a greeting (waving) pose like the reference picture; RightArm hangs down.
for side, x, z_angle in (("LeftArm", -0.6, -150), ("RightArm", 0.6, 10)):
    arm = s.go(side, parent=robot, pos=(x, 1.55, 0), euler=(0, 0, z_angle))
    s.go("Shoulder", parent=arm, scale=(0.2, 0.2, 0.2), components=s.mesh("Sphere", SILVER))
    s.go("ArmShape", parent=arm, pos=(0, -0.4, 0), scale=(0.12, 0.4, 0.12), components=s.mesh("Cylinder", ORANGE))
    s.go("Hand", parent=arm, pos=(0, -0.86, 0), scale=(0.22, 0.22, 0.22), components=s.mesh("Sphere", SILVER))

# Legs: short and round, with round flat feet (đế tròn) -> stands on a flat floor.
for side, x in (("LeftLeg", -0.22), ("RightLeg", 0.22)):
    leg = s.go(side, parent=robot, pos=(x, 0, 0))
    s.go("LegShape", parent=leg, pos=(0, 0.3, 0), scale=(0.2, 0.2, 0.2), components=s.mesh("Cylinder", ORANGE))
    s.go("Foot", parent=leg, pos=(0, 0.05, 0.03), scale=(0.34, 0.05, 0.38), components=s.mesh("Cylinder", SILVER))

write("Assets/Exam/3D/Scenes/Cau3_Robot3D.unity", s.render(ambient=0.42))
write("Assets/Exam/3D/Scenes/Cau3_Robot3D.unity.meta", SCENE_META.format(g=G["Cau3_Robot3D"]))
print("generated OK")
